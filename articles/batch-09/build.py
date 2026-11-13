#!/usr/bin/env python3
"""Batch 09 — 4 pro fresh inline articles for Adminsafebet / new JAIHO777."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PUB = ROOT.parent.parent / 'publish' / 'batch-09'
LOGO = 'https://www.prosafeimg.com/uploads/20260731/6a6c6e378c7f6.png'
APK = 'https://d3iha5lcurdryc.cloudfront.net/jaiho777_119CBDGML2F.apk'
IMG = [
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiTgKqGijA7FzBpM7XQ1WGSreZ0wpuX2PFTjRFr11wy5pJGiAmB5n77xDHR6HYZgtHTLc35pOkmwU9EDKhkAmItDXcg9uKHCAzkJA94ywjbfHdAoonCm5giNGDYkXVyyx-ev6gxh8UQcUVNb5Xhee7ZRoyvraxnvR8Mnt1-c1lYF1w1w9fdo66XSVb1Wol/s700/p156.6_700x500.webp',
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjB9yc6ap1H819WFGJEmpzh4lduzVBEnFQmCwdFgQof9KkPwkOyb0CVNETFdm3iJROJ3aUiyIDsrGrqjiDh7gYM7YTO-dXHYdIpE0Cp36jlINCtnkYL9NMsU6PZatrEq9k83Enar2HoCjKLWI68M4I-ztvZKQsfwy9-z3EMFtvQ4ynXhlNaYlS9vmp9oGI7/s700/P157.2_850x1280_700x500.webp',
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3NTLt4eBtOy4lhRlrdxqYVrVULvZoroGM4RyvCZCv2mcqk-7DxDwNGCQUg-o7qWrIXAcGBO3RDVc9kFGCFkI1tzbAiuJdwp7daEb9fL7zhVj71x7pWflqfLVxQUuyT1aY1WhfnyVptZxI_Acolg365jIariIGFFmYRqKiE9x5olPjZ1ZQ_Ti86HECulud/s700/P157.5_700x500.webp',
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_BGxH02stU3r3TtnYLoc9py6oxBuESYIpPJdORbPNs8cu7DBBisBo1qKvUxQjOYPlFbcKhVSyTjdMirncfl6BpLpSuR2EDPSCAW0-AkAF41VUmNCTeRWijve-OecnzgwLJ2YPYZEt2k3aWhPhG7OzGS4Q5iqQYkhKQjJfIdj84bzQxc6STMYaYkLJJgV_/s700/P157.2_700x500.webp',
]


def ok(html, name):
    if '"' in html or '<style' in html.lower() or re.search(r'<br\b', html, re.I) or '&nbsp;' in html:
        raise SystemExit(f'{name}: forbidden')
    if 'adminsafebet' in html.lower() or 'jaiho777a_' in html:
        raise SystemExit(f'{name}: wrong url/apk')
    if APK not in html:
        raise SystemExit(f'{name}: missing apk')
    n = len(re.sub(r'<[^>]+>', ' ', html).split())
    if n < 500:
        raise SystemExit(f'{name}: {n} words')
    print(f'OK {name}: {n} words')


def cta(label, bg, fg, shadow, radius='0', extra=''):
    return (
        f"<a href='{APK}' title='{label}' style='display:inline-block;margin:10px 0 0;padding:14px 24px;"
        f"background:{bg};color:{fg};font-family:Arial,Helvetica,sans-serif;font-size:15px;font-weight:800;"
        f"text-decoration:none;letter-spacing:0.3px;border-radius:{radius};box-shadow:5px 5px 0 {shadow};{extra}'>{label}</a>"
    )


# 1 Product drop / watch-catalog copper — New Games
def art1():
    return f"""<article style='max-width:980px;margin:0 auto;box-sizing:border-box;padding:0;background:#f7f4ef;color:#1c1917;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.7;overflow:hidden'>
<div style='padding:14px 18px;display:flex;align-items:center;justify-content:space-between;background:#1c1917'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:30px;width:auto;display:block'><span style='color:#e7c6a5;font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase'>JAIHO777 / LOBBY DROP</span></div>
<span style='color:#1c1917;background:#e07a3d;padding:7px 12px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>NEW GAMES</span>
</div>
<div style='padding:clamp(22px,4vw,40px) 18px 10px'>
<p style='margin:0 0 8px;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#e07a3d'>PRODUCT FEATURE · INDIA CASH GAMES</p>
<h1 style='margin:0 0 12px;max-width:18ch;font-size:clamp(30px,5.2vw,46px);line-height:1.08;letter-spacing:-0.8px;color:#1c1917'>New Games on JAIHO777 Just Dropped — Immortal Wolf, Wild Ape II EX & Inky Gold</h1>
<p style='margin:0 0 16px;max-width:42ch;font-size:17px;color:#4a4038'>A clean lobby brief for players who want fresh titles without drowning in stiff brochure copy. Play now energy, big-win curiosity, official install only.</p>
<p style='margin:0 0 18px'>{cta('PLAY THE NEW DROP','#e07a3d','#ffffff','#8a4518','2px')}</p>
</div>
<figure style='margin:0 18px 24px;padding:0;border:1px solid #d9cfc3;background:#ffffff;box-sizing:border-box'>
<img src='{IMG[0]}' alt='JAIHO777 new games banner featuring Immortal Wolf Wild Ape II EX and Inky Gold' title='JAIHO777 new games available' style='width:100%;height:auto;display:block;margin:0'>
<figcaption style='margin:0;padding:10px 14px;font-size:12px;color:#6b5e54;background:#f0ebe4'>Campaign cue: New games available on JAIHO777 — play now, get big win mood.</figcaption>
</figure>
<nav style='display:flex;flex-wrap:wrap;gap:12px;justify-content:center;padding:0 12px 20px'>
<a href='#lineup' style='color:#e07a3d;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>LINEUP</a>
<a href='#how-to-try' style='color:#e07a3d;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>HOW TO TRY</a>
<a href='#faq-games' style='color:#e07a3d;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>FAQ</a>
</nav>
<div style='padding:0 18px 36px'>
<section id='lineup'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#1c1917'>What the new-games lineup is signalling</h2>
<p style='margin:0 0 14px;color:#3a322c'>Pirate-cabin treasure art sells adventure. Under that gloss, JAIHO777 is pointing progressive Indian players toward three distinct lobby personalities: Immortal Wolf for fiery intensity, Wild Ape II EX for neon attitude, and Inky Gold for playful pirate chaos. A modern product drop should read like a catalog — clear SKUs, clear next step — not like a dusty pamphlet.</p>
<p style='margin:0 0 14px;color:#3a322c'>Get big win language is mood, not math. Real cash games and earning games still carry risk. Treat new titles as exploration nights with surplus funds, not as recovery tools after a bad week in Mumbai or Bengaluru.</p>
<ul style='margin:0 0 16px;padding:0;list-style:none'>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-left:4px solid #e07a3d'><strong>Immortal Wolf</strong> — high-heat visual energy for players who like intense sessions.</li>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-left:4px solid #e07a3d'><strong>Wild Ape II EX</strong> — street-cool lobby presence with neon framing.</li>
<li style='margin:0 0 0;padding:14px;background:#ffffff;border-left:4px solid #e07a3d'><strong>Inky Gold</strong> — lighter pirate character energy for short evening tries.</li>
</ul>
</section>
<section id='how-to-try'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#1c1917'>How to try the drop without looking amateur</h2>
<p style='margin:0 0 14px;color:#3a322c'>Install only via the official JAIHO777 APK. Open the lobby, confirm each title is live on your account, and pick one game for a timed sample. Hinglish rule: “Naya game try karo, budget todd ke nahi.” Use UPI / Paytm / PhonePe / Google Pay from entertainment surplus. Keep 24/7 support paths official if something fails to load.</p>
<p style='margin:0 0 14px;color:#3a322c'>A professional session plan is short: twenty to forty minutes, one title, one stop-loss. If Immortal Wolf feels too hot, switch to Inky Gold — do not revenge-jump stakes. Catalog curiosity should feel like browsing a premium drop, not like sprinting through a maze of clone APKs.</p>
<p style='margin:0 0 14px;color:#3a322c'>Share the banner with friends if you want, but share the caution too: official install, age-legal play, no OTP to strangers. That is how a new-games story stays cool in family and hostel chats across Delhi and Hyderabad.</p>
<p style='margin:0 0 14px;color:#3a322c'>Bottom line: the lobby refreshed. Your rules should not dissolve. Play now is a CTA. Process is the product loyalty move for progressive Indian cash-game audiences.</p>
<p style='margin:0 0 14px;color:#3a322c'>When you compare Immortal Wolf, Wild Ape II EX, and Inky Gold side by side, treat them like three different evening outfits. One is loud and fiery, one is street-cool neon, one is playful pirate mischief. Rotating through them on separate nights keeps curiosity high without stacking three learning curves into a single messy session. Progressive Indian players who document stake size and stop time in Notes already outperform impulse browsers who open every new tile at once.</p>
<p style='margin:0 0 14px;color:#3a322c'>Network hygiene matters too. Prefer trusted Wi-Fi or a stable mobile data plan before installing or updating. Mid-download interruptions create panic and push people toward random mirror links. If Google Play Protect or your phone OS warns about unknown sources, enable them only for the install window, then tighten settings again. That small habit is part of looking professional online, not paranoid.</p>
<p style='margin:0 0 14px;color:#3a322c'>Brand loyalty is earned when new-game nights still leave you with rent money, exam prep energy, and a clear head for tomorrow. JAIHO777 can keep dropping titles. You keep deciding which drop deserves your surplus. That mutual respect is what separates a cool product feature story from stiff gambling lectures nobody finishes.</p>
<p style='margin:0 0 18px'>{cta('DOWNLOAD & EXPLORE','#1c1917','#f7f4ef','#e07a3d','2px')}</p>
</section>
<section id='faq-games'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#1c1917'>FAQ</h2>
<div style='display:flex;flex-wrap:wrap;gap:10px'>
<div style='flex:1 1 240px;padding:14px;background:#ffffff;border:1px solid #e5ddd3'><strong style='display:block;margin:0 0 6px'>Are all three games always live?</strong><span style='color:#555'>Check the live lobby after install — catalogs can rotate.</span></div>
<div style='flex:1 1 240px;padding:14px;background:#ffffff;border:1px solid #e5ddd3'><strong style='display:block;margin:0 0 6px'>Does new equal guaranteed profit?</strong><span style='color:#555'>No. New titles still involve risk.</span></div>
<div style='flex:1 1 240px;padding:14px;background:#ffffff;border:1px solid #e5ddd3'><strong style='display:block;margin:0 0 6px'>Safe download?</strong><span style='color:#555'>Only the official APK button in this article.</span></div>
</div>
</section>
</div>
</article>"""


# 2 Membership portal / fintech green — WhatsApp gifts
def art2():
    return f"""<article style='max-width:960px;margin:0 auto;box-sizing:border-box;padding:clamp(18px,3.8vw,36px);background:#f4fbf6;color:#10241a;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.7;border-top:8px solid #128c7e'>
<header style='display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px;padding:0 0 16px;margin:0 0 18px;border-bottom:1px solid #cfe8dc'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:30px;width:auto;display:block'><span style='font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#128c7e'>JAIHO777 / MEMBER PORTAL</span></div>
<p style='margin:0;padding:8px 12px;background:#25d366;color:#10241a;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border-radius:999px'>WHATSAPP REWARDS</p>
</header>
<p style='margin:0 0 8px;text-align:center;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#0e7a6b'>MEMBERSHIP FEATURE · DAILY UNLOCKS</p>
<h1 style='margin:0 0 12px;text-align:center;font-size:clamp(28px,5vw,44px);line-height:1.12;color:#10241a'>More Gifts on JAIHO777 Means More Reasons to Join — If You Treat WhatsApp Rewards Like a Channel, Not a Trap</h1>
<p style='margin:0 auto 16px;max-width:720px;text-align:center;color:#3d5c4e'>Exclusive daily WhatsApp rewards are a modern loyalty lane for Indian earning-game fans who want follow-and-unlock convenience with adult boundaries.</p>
<p style='margin:0 0 22px;text-align:center'>{cta('FOLLOW & UNLOCK PATH','#128c7e','#ffffff','#0a5c52','999px')}</p>
<figure style='max-width:720px;margin:0 auto 24px;padding:10px;background:#ffffff;border-radius:24px;border:1px solid #cfe8dc;box-sizing:border-box'>
<img src='{IMG[1]}' alt='JAIHO777 WhatsApp rewards banner more gifts more reasons to join exclusive daily unlocks' title='JAIHO777 WhatsApp rewards' style='width:100%;height:auto;display:block;margin:0;border-radius:16px'>
<figcaption style='margin:0;padding:10px 6px 2px;font-size:12px;color:#3d5c4e;text-align:center'>Creative cue: more gifts, exclusive daily WhatsApp rewards, follow and unlock.</figcaption>
</figure>
<nav style='display:flex;flex-wrap:wrap;gap:10px;justify-content:center;padding:0 0 18px'>
<a href='#why-wa' style='text-decoration:none;background:#ffffff;color:#128c7e;padding:8px 12px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border:2px solid #25d366'>WHY WHATSAPP</a>
<a href='#safe-join' style='text-decoration:none;background:#ffffff;color:#128c7e;padding:8px 12px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border:2px solid #25d366'>SAFE JOIN</a>
<a href='#faq-wa' style='text-decoration:none;background:#ffffff;color:#128c7e;padding:8px 12px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border:2px solid #25d366'>FAQ</a>
</nav>
<section id='why-wa'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0e7a6b'>Why WhatsApp reward lanes feel current in India</h2>
<p style='margin:0 0 14px;color:#2f4a3c'>India already lives inside WhatsApp — family groups, cricket updates, festival forwards. JAIHO777’s more-gifts creative borrows that habit: emerald palace mood, daily unlock language, follow-and-claim convenience. For progressive players, a channel-based reward rhythm can feel cleaner than random SMS spam — if authenticity stays tight.</p>
<p style='margin:0 0 14px;color:#2f4a3c'>Exclusive daily WhatsApp rewards are still promotional tools. They do not guarantee profit in real cash games. Treat gifts as optional extras after you install the official APK and verify the invite path from trusted in-app notices.</p>
</section>
<section id='safe-join'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0e7a6b'>A professional join checklist</h2>
<ul style='margin:0 0 16px;padding:0;list-style:none'>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:16px'><strong>1</strong> — Download only via the official JAIHO777 CTA on this page.</li>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:16px'><strong>2</strong> — Open in-app notices for the correct WhatsApp follow path.</li>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:16px'><strong>3</strong> — Never share OTP, PIN, or remote-access apps with anyone promising gifts.</li>
<li style='margin:0 0 0;padding:14px;background:#ffffff;border-radius:16px'><strong>4</strong> — Claim with a surplus budget; UPI convenience is not a green light to overfund.</li>
</ul>
<p style='margin:0 0 14px;color:#2f4a3c'>Hinglish: “Follow karo, filter on rakhna.” Clone channels thrive on FOMO. Official campaigns push you toward the app experience, not toward leaking banking life. If a chat asks for payment outside the wallet, exit.</p>
<p style='margin:0 0 14px;color:#2f4a3c'>Membership-portal energy works when the brand respects consent and clarity. More reasons to join should include trust signals: readable reward history, 24/7 support tone, KYC-aware withdrawals. Palace glow is packaging. Process is the product.</p>
<p style='margin:0 0 14px;color:#2f4a3c'>For players in Pune hostels and Chennai flats, daily unlocks can become a morning ritual like chai — peek, claim if eligible, move on. Skip any day that feels pressured. Cadence is healthy only when you can ignore a gift without guilt.</p>
<p style='margin:0 0 14px;color:#2f4a3c'>Think of WhatsApp rewards as a newsletter with benefits. You open it when you have bandwidth. You mute it when life gets loud. You never treat a missed claim as a personal failure. That mindset keeps the emerald palace creative feeling premium instead of needy. Membership portals win when they respect your calendar, not when they flood every unread badge.</p>
<p style='margin:0 0 14px;color:#2f4a3c'>If a friend forwards a screenshot of exclusive daily WhatsApp rewards, ask for the install path first. Screenshots can be edited. Official APK + in-app notice + verified channel is the triangle. Anything outside that triangle is noise. Progressive India audiences already know phishing stories from banking WhatsApp forwards — apply the same filter to gaming gifts.</p>
<p style='margin:0 0 14px;color:#2f4a3c'>Closing note: more gifts, more reasons to join — yes. More blind trust — no. JAIHO777 can host the loyalty lane. You host the decision to follow, claim, or walk away for a week without drama.</p>
<p style='margin:0 0 18px;text-align:center'>{cta('JOIN VIA OFFICIAL APP','#25d366','#10241a','#128c7e','999px')}</p>
</section>
<section id='faq-wa'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0e7a6b'>FAQ</h2>
<p style='margin:0 0 6px;font-weight:800'>Are WhatsApp rewards automatic forever?</p>
<p style='margin:0 0 12px;color:#2f4a3c'>No. Check live eligibility and official channel instructions.</p>
<p style='margin:0 0 6px;font-weight:800'>Do gifts guarantee winnings?</p>
<p style='margin:0 0 12px;color:#2f4a3c'>No. Promotional value is not a profit promise.</p>
<p style='margin:0 0 6px;font-weight:800'>Where to start safely?</p>
<p style='margin:0 0 0;color:#2f4a3c'>Official APK first, then verified in-app follow path only.</p>
</section>
</article>"""


# 3 Cinematic runway poster — crimson + asphalt — Aviator mega win
def art3():
    return f"""<article style='max-width:980px;margin:0 auto;box-sizing:border-box;padding:0;background:#0f0f10;color:#f5f0ea;font-family:Impact,Haettenschweiler,Arial Black,sans-serif;overflow:hidden'>
<div style='padding:12px 16px;display:flex;align-items:center;justify-content:space-between;border-bottom:3px solid #9b1d20;font-family:Arial,Helvetica,sans-serif'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:28px;width:auto;display:block'><span style='font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#ffb4a8'>JAIHO777 / RUNWAY DESK</span></div>
<span style='background:#9b1d20;color:#ffffff;padding:6px 10px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>AVIATOR SPOTLIGHT</span>
</div>
<div style='padding:clamp(20px,4vw,38px) 16px 8px;background:linear-gradient(180deg,#1a1010 0%,#0f0f10 70%)'>
<p style='margin:0 0 8px;font-family:Arial,Helvetica,sans-serif;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#ffb4a8'>MEMBER SHOWCASE · UONO AVIATOR 2</p>
<h1 style='margin:0 0 12px;font-size:clamp(32px,5.8vw,52px);line-height:0.98;text-transform:uppercase;letter-spacing:0.5px;color:#ffffff'>Uono Aviator 2 on JAIHO777: A 134.6x / ₹2.69 Lakh Mega Win Reel — Read the Runway Lights Before You Chase</h1>
<p style='margin:0 0 16px;max-width:740px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.65;font-weight:400;color:#d9cfc6'>UID 134***862 made the cinematic banner. Steal timing discipline — not the fantasy that every flight lands on gold.</p>
<p style='margin:0 0 18px'>{cta('TAKE OFF ON OFFICIAL APP','#9b1d20','#ffffff','#5a0f12','0')}</p>
</div>
<figure style='margin:0;padding:0;border-top:3px solid #9b1d20;border-bottom:3px solid #9b1d20'>
<img src='{IMG[2]}' alt='JAIHO777 Uono Aviator 2 mega win showcase with 134.6x and Rs 269200' title='Uono Aviator 2 mega win' style='width:100%;height:auto;display:block;margin:0'>
<figcaption style='margin:0;padding:10px 14px;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#b9a9a0;background:#141414'>Showcase: 134.6x · ₹269,200 · Uono Aviator 2 — highlight reel, not a flight plan for everyone.</figcaption>
</figure>
<nav style='display:flex;flex-wrap:wrap;gap:14px;justify-content:center;padding:12px;font-family:Arial,Helvetica,sans-serif;background:#141414'>
<a href='#reel' style='color:#ffb4a8;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>THE REEL</a>
<a href='#runway' style='color:#ffb4a8;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>RUNWAY RULES</a>
<a href='#faq-av' style='color:#ffb4a8;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>FAQ</a>
</nav>
<div style='padding:clamp(18px,3vw,32px) 16px 36px;font-family:Arial,Helvetica,sans-serif;font-weight:400;line-height:1.7'>
<section id='reel'>
<h2 style='margin:0 0 10px;font-family:Impact,Haettenschweiler,Arial Black,sans-serif;font-size:clamp(24px,3.5vw,32px);text-transform:uppercase;color:#ffb4a8;letter-spacing:1px'>What this mega win reel is selling</h2>
<p style='margin:0 0 14px;color:#ddd2c8'>Crash-style aviator energy sells timing, tension, and cinematic multipliers. JAIHO777’s Uono Aviator 2 showcase leans into that: runway sunset, phone UI, crown banner, ₹269,200 flex. As member coverage, clap for the shot. As personal strategy, remember multipliers cut both ways.</p>
<p style='margin:0 0 14px;color:#ddd2c8'>Hinglish: “Flight dekh ke plan mat uda dena.” Progressive Indian players from Delhi to Goa already understand FOMO. The professional move is converting inspiration into a capped experiment — not into an all-night chase after a forwarded screenshot.</p>
</section>
<section id='runway'>
<h2 style='margin:0 0 10px;font-family:Impact,Haettenschweiler,Arial Black,sans-serif;font-size:clamp(24px,3.5vw,32px);text-transform:uppercase;color:#ffb4a8;letter-spacing:1px'>Runway rules for loyal wallets</h2>
<ul style='margin:0 0 16px;padding:0;list-style:none'>
<li style='margin:0 0 8px;padding:12px 14px;background:#1a1515;border-left:4px solid #9b1d20'><strong style='color:#ffb4a8'>Official tower only</strong> — legacy? No. New-site APK from this page only.</li>
<li style='margin:0 0 8px;padding:12px 14px;background:#1a1515;border-left:4px solid #9b1d20'><strong style='color:#ffb4a8'>Pre-write stakes</strong> — decide bet size before the plane moves.</li>
<li style='margin:0 0 0;padding:12px 14px;background:#1a1515;border-left:4px solid #9b1d20'><strong style='color:#ffb4a8'>Hard landing time</strong> — end the session even if the next multiplier looks tempting.</li>
</ul>
<p style='margin:0 0 14px;color:#ddd2c8'>UPI / Paytm / PhonePe / Google Pay top-ups belong to surplus entertainment money. KYC still gates withdrawals after a loud night. 24/7 support helps with account issues; it cannot reverse a late cash-out decision you regret.</p>
<p style='margin:0 0 14px;color:#ddd2c8'>If friends demand you match ₹269,200, mute the noise. Showcase culture should teach timing and restraint. Aviator formats punish hesitation and greed with equal efficiency. Keep the movie-poster vibes; keep the bankroll adult.</p>
<p style='margin:0 0 14px;color:#ddd2c8'>Confirm Uono Aviator 2 is live in your lobby after install. Sample on the smallest comfortable stake. Exit while you still respect yourself. That is how a cinematic spotlight stays professional instead of becoming a crash story about your wallet.</p>
<p style='margin:0 0 14px;color:#ddd2c8'>Cinematic reels travel faster than caution notes. When a friend in Ahmedabad or Kochi forwards the 134.6x frame, reply with a stake plan, not only applause. That tiny social push keeps showcase culture from becoming peer pressure. Progressive players can celebrate a UID without treating it like a syllabus.</p>
<p style='margin:0 0 14px;color:#ddd2c8'>Hardware reality: play on a charged phone with notifications muted for banking apps you do not need mid-round. Split attention is how late cash-outs happen. If the runway lights of the creative look exciting, let that excitement stay visual — keep your thumb rules boring and written. Boring rules are how cinematic nights stay affordable.</p>
<p style='margin:0 0 14px;color:#ddd2c8'>Final frame: JAIHO777 can keep publishing mega-win posters. You keep publishing your own stop time. That is the only credit roll that matters after the plane leaves the screen.</p>
<p style='margin:0 0 14px;color:#ddd2c8'>If you still feel restless after a short sample, switch to a calmer lobby title instead of doubling Aviator stakes. Changing games is a valid cool-down. Changing stake size upward after a loss is not. That distinction keeps member-showcase energy inspiring instead of contagious in the worst way.</p>
<p style='margin:0 0 18px'>{cta('OPEN JAIHO777 RUNWAY','#ffffff','#0f0f10','#9b1d20','0')}</p>
</section>
<section id='faq-av'>
<h2 style='margin:0 0 10px;font-family:Impact,Haettenschweiler,Arial Black,sans-serif;font-size:clamp(24px,3.5vw,32px);text-transform:uppercase;color:#ffb4a8;letter-spacing:1px'>FAQ</h2>
<p style='margin:0 0 6px;font-weight:800;color:#ffffff'>Can I aim for the same 134.6x?</p>
<p style='margin:0 0 12px;color:#ddd2c8'>No. Multipliers vary. This is a showcase, not a target sheet.</p>
<p style='margin:0 0 6px;font-weight:800;color:#ffffff'>Is Aviator always available?</p>
<p style='margin:0 0 12px;color:#ddd2c8'>Check the live lobby after installing the official APK.</p>
<p style='margin:0 0 6px;font-weight:800;color:#ffffff'>Safe download?</p>
<p style='margin:0 0 0;color:#ddd2c8'>Only the JAIHO777 APK button in this article.</p>
</section>
</div>
</article>"""


# 4 Console UI / streaming slate + tangerine — Mystery box
def art4():
    return f"""<article style='max-width:960px;margin:0 auto;box-sizing:border-box;padding:0;background:#121826;color:#e8eef8;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.7;overflow:hidden'>
<div style='padding:14px 16px;display:flex;align-items:center;justify-content:space-between;background:#0b101a;border-bottom:1px solid #243044'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:30px;width:auto;display:block'><span style='font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#ff7a00'>JAIHO777 / REVEAL UI</span></div>
<span style='background:#ff7a00;color:#121826;padding:7px 12px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border-radius:8px'>MYSTERY BOX</span>
</div>
<div style='display:flex;flex-wrap:wrap'>
<div style='flex:1 1 300px;padding:clamp(20px,4vw,36px);box-sizing:border-box'>
<p style='margin:0 0 8px;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#ff7a00'>REWARD SPOTLIGHT</p>
<h1 style='margin:0 0 12px;font-size:clamp(28px,5vw,42px);line-height:1.1;color:#ffffff'>The Big Reveal on JAIHO777 Starts With Mystery Box Bonuses — Open for Surprise, Not for Blind Hope</h1>
<p style='margin:0 0 16px;color:#b7c3d6'>Exclusive mystery box bonuses are built for curiosity. Keep the console-cool vibe, keep the surprise adult, keep the install official.</p>
<p style='margin:0'>{cta('OPEN YOUR BOX PATH','#ff7a00','#121826','#a34d00','12px')}</p>
</div>
<figure style='flex:1 1 300px;margin:0;padding:0;background:#0b101a'>
<img src='{IMG[3]}' alt='JAIHO777 mystery box bonuses the big reveal exclusive surprise gifts banner' title='JAIHO777 mystery box bonuses' style='width:100%;height:auto;display:block;margin:0'>
<figcaption style='margin:0;padding:10px 14px;font-size:12px;color:#8b9bb3;background:#0b101a'>Creative: the big reveal starts here — exclusive mystery box bonuses.</figcaption>
</figure>
</div>
<nav style='display:flex;flex-wrap:wrap;gap:12px;justify-content:center;padding:12px;background:#0b101a;border-top:1px solid #243044;border-bottom:1px solid #243044'>
<a href='#what-box' style='color:#ff7a00;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>WHAT IT IS</a>
<a href='#how-open' style='color:#ff7a00;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>HOW TO OPEN</a>
<a href='#faq-box' style='color:#ff7a00;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>FAQ</a>
</nav>
<div style='padding:clamp(18px,3vw,32px) 16px 36px'>
<section id='what-box'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#ff7a00'>What mystery box bonuses actually are</h2>
<p style='margin:0 0 14px;color:#c9d4e6'>Mystery boxes sell discovery. JAIHO777’s big-reveal creative layers ape swagger, glowing crates, and open-your-box urgency. For progressive Indian audiences, that UI language feels closer to a gaming console drop than to an old paper coupon. Cool. Still: surprise contents are promotional — not guaranteed profit printers.</p>
<p style='margin:0 0 14px;color:#c9d4e6'>Exclusive mystery box bonuses can include varied reward types depending on live rules. Read the panel before you tap. Discover the surprise after you set a budget. Hinglish: “Box kholo, dimaag band mat karo.”</p>
</section>
<section id='how-open'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#ff7a00'>How to open like a pro</h2>
<ul style='margin:0 0 16px;padding:0;list-style:none'>
<li style='margin:0 0 10px;padding:14px;background:#1a2233;border-radius:14px;border:1px solid #2c3a55'><strong>Install clean</strong> — official JAIHO777 APK only.</li>
<li style='margin:0 0 10px;padding:14px;background:#1a2233;border-radius:14px;border:1px solid #2c3a55'><strong>Verify eligibility</strong> — live event window and account state matter.</li>
<li style='margin:0 0 10px;padding:14px;background:#1a2233;border-radius:14px;border:1px solid #2c3a55'><strong>Cap the reveal</strong> — one session limit; UPI surplus only.</li>
<li style='margin:0 0 0;padding:14px;background:#1a2233;border-radius:14px;border:1px solid #2c3a55'><strong>Exit clean</strong> — do not reopen the wallet just because the glow looked cinematic.</li>
</ul>
<p style='margin:0 0 14px;color:#c9d4e6'>Streaming-platform layouts win when CTAs are obvious and rules are readable. Keep Paytm / PhonePe / Google Pay inside entertainment money. Use 24/7 support only through official in-app routes. Never send OTP to strangers promising denser mystery boxes.</p>
<p style='margin:0 0 14px;color:#c9d4e6'>Compared with static deposit menus, mystery boxes win on curiosity. Compared with careful planners, a fixed coupon may feel calmer. Many regulars use both: claim a structured boost, then treat the big reveal as optional dessert. That hybrid keeps the UI exciting without turning every night into a loot-chase spiral.</p>
<p style='margin:0 0 14px;color:#c9d4e6'>Professional close: open the box for surprise, close the app for your future self. JAIHO777 can host the reveal. You host the boundaries.</p>
<p style='margin:0 0 14px;color:#c9d4e6'>Mystery UI also invites comparison shopping. Some nights a fixed welcome boost feels clearer. Some nights a surprise crate feels more fun. Neither choice is morally superior. What matters is documenting which promo type you actually enjoy versus which type makes you chase. Progressive Indian earners who journal those preferences waste less surplus on vibes they secretly dislike.</p>
<p style='margin:0 0 14px;color:#c9d4e6'>If the big reveal creative shows floating diamonds and rupee coins, treat them as art direction. Art is allowed to exaggerate. Your wallet is not allowed to. Open one eligible box, screenshot the result for your own records if you like tracking, then leave the lobby. That workflow looks modern, calm, and professional — the opposite of stiff panic tapping.</p>
<p style='margin:0 0 14px;color:#c9d4e6'>Last beat: exclusive mystery box bonuses are a reward spotlight, not a lifestyle. Keep the console-cool aesthetic. Keep the surprise. Keep the exit. That is how JAIHO777’s reveal stays exciting tomorrow instead of exhausting tonight.</p>
<p style='margin:0 0 14px;color:#c9d4e6'>Share the reveal creative with friends if you want, but share the checklist too: official APK, eligibility read, surplus budget, hard stop. Cool branding without cool process is just noise. Process is what makes the big reveal look professional in a crowded Indian gaming feed.</p>
<p style='margin:0 0 18px'>{cta('DOWNLOAD & DISCOVER','#ffffff','#121826','#ff7a00','12px')}</p>
</section>
<section id='faq-box'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#ff7a00'>FAQ</h2>
<div style='display:flex;flex-direction:column;gap:10px'>
<div style='padding:12px 14px;background:#1a2233;border-radius:12px'><strong style='display:block;margin:0 0 4px;color:#ffffff'>Are mystery box contents guaranteed?</strong><span style='color:#b7c3d6'>No. Contents and odds follow live promo rules.</span></div>
<div style='padding:12px 14px;background:#1a2233;border-radius:12px'><strong style='display:block;margin:0 0 4px;color:#ffffff'>Is the reveal always on?</strong><span style='color:#b7c3d6'>Event windows vary — check in-app after install.</span></div>
<div style='padding:12px 14px;background:#1a2233;border-radius:12px'><strong style='display:block;margin:0 0 4px;color:#ffffff'>Where to download safely?</strong><span style='color:#b7c3d6'>Use only the official APK button here.</span></div>
</div>
</section>
</div>
</article>"""


META = [
    {
        'file': '01-new-games-drop.html',
        'title': 'New Games on JAIHO777 Just Dropped — Immortal Wolf, Wild Ape II EX & Inky Gold',
        'keywords': 'new lobby titles India, Immortal Wolf cash games, Wild Ape II EX try, Inky Gold short session',
        'description': 'JAIHO777 new-games drop brief: Immortal Wolf, Wild Ape II EX, Inky Gold—how to sample the lineup with a clean official install.',
        'fn': art1,
    },
    {
        'file': '02-whatsapp-rewards.html',
        'title': 'More Gifts on JAIHO777 Means More Reasons to Join — If You Treat WhatsApp Rewards Like a Channel, Not a Trap',
        'keywords': 'exclusive daily WhatsApp rewards, follow unlock gifts, membership reward channel, safe join checklist India',
        'description': 'How JAIHO777 WhatsApp reward lanes work for Indian players—more gifts, daily unlocks, and a safe follow-and-claim checklist.',
        'fn': art2,
    },
    {
        'file': '03-aviator-mega-win.html',
        'title': 'Uono Aviator 2 on JAIHO777: A 134.6x / ₹2.69 Lakh Mega Win Reel — Read the Runway Lights Before You Chase',
        'keywords': 'Uono Aviator 2 spotlight, crash game discipline, mega win showcase India, timing over FOMO',
        'description': 'Uono Aviator 2 ₹269,200 / 134.6x showcase on JAIHO777 decoded—keep cinematic vibes, write stakes first, land on time.',
        'fn': art3,
    },
    {
        'file': '04-mystery-box-reveal.html',
        'title': 'The Big Reveal on JAIHO777 Starts With Mystery Box Bonuses — Open for Surprise, Not for Blind Hope',
        'keywords': 'mystery box bonuses India, exclusive reveal rewards, open box surprise promo, console-style cash game UI',
        'description': 'JAIHO777 mystery box bonuses explained—big reveal energy with pro open rules, eligibility checks, and surplus-only play.',
        'fn': art4,
    },
]


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    PUB.mkdir(parents=True, exist_ok=True)
    (PUB / 'per-artikel').mkdir(parents=True, exist_ok=True)
    all_parts = [
        'JAIHO777 BATCH 09 — ADMINSAFEBET (SITUS BARU)',
        '',
        f'APK: {APK}',
        '',
        'Format: tabel Title/Keywords/Description lalu HTML inline penuh (tanpa tag style).',
        '',
    ]
    meta_bits = []
    for i, m in enumerate(META, 1):
        html = m['fn']().strip()
        while '\n\n\n' in html:
            html = html.replace('\n\n\n', '\n\n')
        ok(html, m['file'])
        (ROOT / m['file']).write_text(html + '\n', encoding='utf-8')
        table = (
            '| Article Title | Keywords | Description |\n'
            '|---|---|---|\n'
            f"| {m['title']} | {m['keywords']} | {m['description']} |"
        )
        (PUB / 'per-artikel' / f'artikel-{i:02d}.txt').write_text(f'{table}\n\n{html}\n', encoding='utf-8')
        all_parts += ['=' * 72, f'ARTIKEL {i}', '=' * 72, '', table, '', html, '']
        meta_bits.append(f'ARTIKEL {i}\n{table}\n')
    (PUB / 'COPY-PASTE-SEMUA-ARTIKEL.txt').write_text('\n'.join(all_parts), encoding='utf-8')
    (ROOT / 'METADATA.txt').write_text('\n'.join(meta_bits), encoding='utf-8')
    (ROOT / 'README.md').write_text(
        '# Batch 09 — Pro fresh inline articles\n\n'
        'Copy-paste: `../../publish/batch-09/`\n\n'
        '4 artikel. Full inline CSS. Title/Keywords/Description dibedakan.\n',
        encoding='utf-8',
    )
    (PUB / 'README.md').write_text(
        '# Batch 09 Copy Pack\n\n'
        '- `COPY-PASTE-SEMUA-ARTIKEL.txt`\n'
        '- `per-artikel/artikel-01.txt` ... `artikel-04.txt`\n',
        encoding='utf-8',
    )
    print('DONE')


if __name__ == '__main__':
    main()
