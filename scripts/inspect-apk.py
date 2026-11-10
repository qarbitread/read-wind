#!/usr/bin/env python3
"""Read real Android binary XML metadata with the Python standard library.

python3 scripts/inspect-apk.py /path/app.apk --update-config
python3 scripts/inspect-apk.py --url --update-config
No Android build tools, APK execution, or third-party Python packages required.
"""
import argparse
import hashlib
import json
import struct
import tempfile
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config/release.json"


def manifest_values(blob):
    strings, values, pos = [], {}, 8
    u16 = lambda i: struct.unpack_from("<H", blob, i)[0]
    u32 = lambda i: struct.unpack_from("<I", blob, i)[0]
    string = lambda i: strings[i] if i < len(strings) else None

    def length8(offset):
        first = blob[offset]
        return ((((first & 127) << 8) | blob[offset + 1], offset + 2)
                if first & 128 else (first, offset + 1))

    while pos < len(blob):
        kind, header_size, size = struct.unpack_from("<HHI", blob, pos)
        if not size or pos + size > len(blob):
            raise ValueError("Invalid binary Android manifest")
        if kind == 1:
            count, flags = u32(pos + 8), u32(pos + 16)
            start = pos + u32(pos + 20)
            for i in range(count):
                offset = start + u32(pos + header_size + i * 4)
                if flags & 256:
                    _, offset = length8(offset)
                    length, offset = length8(offset)
                    strings.append(blob[offset:offset + length].decode("utf-8"))
                else:
                    length, offset = u16(offset), offset + 2
                    if length & 32768:
                        length, offset = ((length & 32767) << 16) | u16(offset), offset + 2
                    strings.append(blob[offset:offset + length * 2].decode("utf-16le"))
        elif kind == 0x102:
            element = string(u32(pos + 20))
            if element in ("manifest", "uses-sdk"):
                attr_start, attr_size, attr_count = u16(pos + 24), u16(pos + 26), u16(pos + 28)
                for i in range(attr_count):
                    offset = pos + 16 + attr_start + i * attr_size
                    name, raw, typ, val = string(u32(offset + 4)), u32(offset + 8), blob[offset + 15], u32(offset + 16)
                    values[name] = string(raw) if raw != 0xffffffff else string(val) if typ == 3 else val
        pos += size
    return values


def inspect(apk):
    with zipfile.ZipFile(apk) as archive:
        manifest = manifest_values(archive.read("AndroidManifest.xml"))
    fingerprint = hashlib.sha256()
    with apk.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            fingerprint.update(chunk)
    version = manifest.get("versionName")
    if not isinstance(version, str):
        raise ValueError("versionName is a resource reference; resolve it with Android aapt2 before publishing")
    sdk = manifest.get("minSdkVersion", 1)
    android_versions = {21: "5.0", 22: "5.1", 23: "6.0", 24: "7.0", 25: "7.1", 26: "8.0", 27: "8.1", 28: "9", 29: "10", 30: "11", 31: "12", 32: "12L", 33: "13", 34: "14", 35: "15", 36: "16"}
    if sdk not in android_versions:
        raise ValueError(f"Map API level {sdk} to its real Android version before publishing")
    return {"version": version, "versionCode": manifest.get("versionCode"),
            "filename": f"JAIHO777-{version}.apk", "sizeBytes": apk.stat().st_size,
            "minSdk": sdk, "minimumAndroid": android_versions[sdk],
            "packageName": manifest.get("package"), "sha256": fingerprint.hexdigest(),
            "inspectedAt": datetime.now(timezone.utc).date().isoformat()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apk", nargs="?")
    parser.add_argument("--url", action="store_true", help="Download the HTTPS APK URL in config/release.json")
    parser.add_argument("--update-config", action="store_true")
    args = parser.parse_args()
    config = json.loads(CONFIG.read_text())
    with tempfile.TemporaryDirectory(prefix="jaiho777-inspect-") as temporary:
        if args.url:
            url = config["url"]
            if not url.startswith("https://"):
                parser.error("APK URL must use HTTPS")
            apk = Path(temporary) / "source.apk"
            request = urllib.request.Request(url, headers={"Accept-Encoding": "identity"})
            with urllib.request.urlopen(request, timeout=60) as response, apk.open("wb") as file:
                if not response.geturl().startswith("https://"):
                    raise ValueError("Refusing an insecure redirect")
                for chunk in iter(lambda: response.read(1024 * 1024), b""):
                    file.write(chunk)
        elif args.apk:
            apk = Path(args.apk)
        else:
            parser.error("Provide an APK path or --url")
        metadata = inspect(apk)
        print(json.dumps(metadata, indent=2))
        if args.update_config:
            config.update(metadata)
            CONFIG.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
