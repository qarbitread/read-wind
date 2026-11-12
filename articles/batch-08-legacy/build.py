#!/usr/bin/env python3
"""Batch 08 — 3 fresh inline HTML articles for Prosafebet / legacy JAIHO777."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PUB = ROOT.parent.parent / 'publish' / 'batch-08-legacy'
LOGO = 'https://www.prosafeimg.com/uploads/20260731/6a6c6e378c7f6.png'
APK = 'https://d3iha5lcurdryc.cloudfront.net/jaiho777a_J6NJ4881PJ3.apk'
IMG = [
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdcgafzjHl3N4j6hiUMfnSvCk3Y9VhCtZzbeKF6s6-Gl_eaJhA-ipMTkVWbUO1rB0Ag45nB-SZBA9rnNM3Q4lB_20cc_tEgPuUimara6TYv4e8RtYmytEI-PcN2H7GPON9DTnoKi1q5TATBIiWWDSX7CZgncayrc4zR_khaMT4yNr5fgO7LSlAFAbpW4Vw/s700/5_p156.4_700x500.webp',
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYUvl5PbYEtT1bRLcBX_TS6nG30wa-2-pYkd4vW9uR637swYWIPSToniPNVZxiR4HSC0Bu8qPUZQP2FyMhck1Q29gNhXw_Nsg1ZEnhbLk62huk9BhTwAYRW-LiZCjxoS2TNP5TUD1nCuir8x3-uOuAkEfYD4DYROv2_P0JMeaNNixTQF1F-wvKI_YMDOAr/s700/6_p156.1_700x500.webp',
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYOxgODu4dOJl4INoAv17zDbUNTSDv5kLQdeNmmtdOcanvgcoap5Tz791AYr6vr3mdNEFrs1pTQITLzpI770PXQU6taWvEUmY9bho7K7WIxBZz1Eb6MUHzzTJl3tZVo9mwEcPhvPiGCiFUXF4SPJ99It8JJ85ZpaSGc_C315BmlslWyprlnVHQeVMw3pY2/s700/7_P077.1_700x500.webp',
]


def ok(html, name):
    if '"' in html or '<style' in html.lower() or re.search(r'<br\b', html, re.I) or '&nbsp;' in html:
        raise SystemExit(f'{name}: forbidden token')
    if 'prosafebet.com/admin' in html.lower() or 'jaiho777_119' in html:
        raise SystemExit(f'{name}: wrong apk/admin')
    if APK not in html:
        raise SystemExit(f'{name}: missing legacy apk')
    n = len(re.sub(r'<[^>]+>', ' ', html).split())
    if n < 500:
        raise SystemExit(f'{name}: {n} words')
    print(f'OK {name}: {n} words')


def cta(label, bg, fg, shadow, radius='0', extra=''):
    return (
        f"<a href='{APK}' title='{label}' style='display:inline-block;margin:10px 0 0;padding:14px 24px;"
        f"background:{bg};color:{fg};font-family:Arial,Helvetica,sans-serif;font-size:15px;font-weight:800;"
        f"text-decoration:none;letter-spacing:0.4px;border-radius:{radius};box-shadow:5px 5px 0 {shadow};{extra}'>{label}</a>"
    )


# 1 Cyber magazine — charcoal + fuchsia + ice — Wild Ape mega win spotlight
def art1():
    return f"""<article style='max-width:980px;margin:0 auto;box-sizing:border-box;padding:0;background:#0d0d12;color:#f2f2f7;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.7;overflow:hidden'>
<div style='padding:14px 16px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #2a2a35'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:30px;width:auto;display:block'><span style='font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#ff4fd8'>JAIHO777 / NIGHT DESK</span></div>
<span style='background:#ff4fd8;color:#0d0d12;padding:7px 12px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border-radius:999px'>MEGA WIN SPOTLIGHT</span>
</div>
<div style='padding:clamp(22px,4vw,40px) 16px 8px;text-align:left;max-width:820px;margin:0 auto'>
<p style='margin:0 0 8px;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#8be9ff'>MEMBER SHOWCASE · WILD APE II EX</p>
<h1 style='margin:0 0 12px;font-size:clamp(30px,5.4vw,48px);line-height:1.08;letter-spacing:-0.8px;color:#ffffff'>Wild Ape II EX on JAIHO777: What a ₹2.66 Lakh Mega Win Showcase Should Teach Loyal Players</h1>
<p style='margin:0 0 16px;font-size:17px;color:#c8c8d6'>UID 622***428 hit the highlight reel. Steal the discipline lessons — not the fantasy that every spin reprints a neon jackpot.</p>
<p style='margin:0 0 18px'>{cta('OPEN OFFICIAL APP','#ff4fd8','#0d0d12','#8a1f72','999px')}</p>
</div>
<figure style='max-width:760px;margin:0 auto 22px;padding:0;border:1px solid #2a2a35;box-sizing:border-box'>
<img src='{IMG[0]}' alt='JAIHO777 Wild Ape II EX mega win showcase showing Rs 266000 and masked UID' title='Wild Ape II EX mega win' style='width:100%;height:auto;display:block;margin:0'>
<figcaption style='margin:0;padding:10px 14px;background:#16161f;color:#9a9ab0;font-size:12px'>Showcase art: MEGA WIN · ₹266,000 · Wild Ape II EX — celebration content, not a promise.</figcaption>
</figure>
<nav style='display:flex;flex-wrap:wrap;gap:12px;justify-content:center;padding:0 12px 20px'>
<a href='#what-it-is' style='color:#8be9ff;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>WHAT IT IS</a>
<a href='#lessons' style='color:#8be9ff;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>LESSONS</a>
<a href='#faq-ape' style='color:#8be9ff;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>FAQ</a>
</nav>
<div style='padding:0 16px 36px;max-width:820px;margin:0 auto'>
<section id='what-it-is'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#ff4fd8'>What this neon spotlight is — and is not</h2>
<p style='margin:0 0 14px;color:#d7d7e4'>Legacy JAIHO777 players already know highlight reels travel fast on Telegram. A masked UID, cyber city glow, cigar-cool ape energy, and ₹266,000 in gold type. As member-story coverage, we treat it as a showcase. It proves memorable sessions happen on Wild Ape II EX. It does not prove your next ten minutes will match that number.</p>
<p style='margin:0 0 14px;color:#d7d7e4'>Mature readers in Mumbai and Bengaluru can hold two thoughts at once: clap for the shot, still respect variance. Mega win art is marketing atmosphere. Your UPI balance is reality.</p>
</section>
<section id='lessons'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#ff4fd8'>Lessons loyal players should actually steal</h2>
<ul style='margin:0 0 16px;padding:0;list-style:none'>
<li style='margin:0 0 10px;padding:14px;background:#16161f;border-left:4px solid #ff4fd8;border-radius:0 14px 14px 0'><strong>Bankroll first</strong> — big showcases usually sit on long participation, not one reckless all-in.</li>
<li style='margin:0 0 10px;padding:14px;background:#16161f;border-left:4px solid #ff4fd8;border-radius:0 14px 14px 0'><strong>Game familiarity</strong> — learn Wild Ape II EX volatility before chasing screenshots.</li>
<li style='margin:0 0 10px;padding:14px;background:#16161f;border-left:4px solid #ff4fd8;border-radius:0 14px 14px 0'><strong>Stop rules</strong> — leave with money and with sleep.</li>
<li style='margin:0 0 0;padding:14px;background:#16161f;border-left:4px solid #ff4fd8;border-radius:0 14px 14px 0'><strong>Official builds only</strong> — neon art means nothing on a tampered APK.</li>
</ul>
<p style='margin:0 0 14px;color:#d7d7e4'>Hinglish: “Inspire ho, confuse mat ho.” Set a spotlight budget you can lose without rewriting rent day. Install via the official legacy CTA, confirm the title in the lobby, and treat any win above plan as a reason for cash discipline — not ego broadcasts.</p>
<p style='margin:0 0 14px;color:#d7d7e4'>Mute chats that mock small withdrawals. Mute friends who demand you double it. Keep a personal ledger. Instant withdrawal expectations still follow KYC and banking hours even after a neon night. 24/7 support helps; calm screenshots help more.</p>
<p style='margin:0 0 14px;color:#d7d7e4'>If the banner hits your group chat, reply with process: official install, tiny stake, hard timer. That answer protects the circle better than another fire emoji. Showcase culture should reduce confusion, not multiply reckless clones of someone else’s highlight reel.</p>
<p style='margin:0 0 14px;color:#d7d7e4'>Wild Ape II EX can be entertainment. It cannot be a salary plan. Loyal JAIHO777 players win the long season by protecting process while still enjoying modern lobby energy.</p>
<p style='margin:0 0 14px;color:#d7d7e4'>If you feel inspired, translate inspiration into a controlled experiment: official legacy install, smallest comfortable stake, hard timer, no alcohol, no revenge clicks after a near miss. If the session stays fun, great. If it starts feeling like homework for a screenshot, stop. Highlight reels are content. Your Paytm balance is reality.</p>
<p style='margin:0 0 14px;color:#d7d7e4'>Celebrate privately before you broadcast. Keep support paths official. And remember: a masked UID flex is atmosphere. It is not an assignment for your next deposit on a week when rent is already tight.</p>
<p style='margin:0 0 18px'>{cta('PLAY ON LEGACY APK','#8be9ff','#0d0d12','#2a6f7c','999px')}</p>
</section>
<section id='faq-ape'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#ff4fd8'>FAQ</h2>
<p style='margin:0 0 6px;font-weight:800;color:#ffffff'>Can I target the same ₹266,000 outcome?</p>
<p style='margin:0 0 12px;color:#d7d7e4'>No. Outcomes vary widely. This is showcase coverage.</p>
<p style='margin:0 0 6px;font-weight:800;color:#ffffff'>Is Wild Ape II EX always in the lobby?</p>
<p style='margin:0 0 12px;color:#d7d7e4'>Catalogs rotate. Check the live list after install.</p>
<p style='margin:0 0 6px;font-weight:800;color:#ffffff'>Safe download path?</p>
<p style='margin:0 0 0;color:#d7d7e4'>Only the official JAIHO777 legacy APK button here.</p>
</section>
</div>
</article>"""


# 2 Adventure travel / jungle brochure — emerald + sunrise gold — 180% deposit
def art2():
    return f"""<article style='max-width:960px;margin:0 auto;box-sizing:border-box;padding:clamp(18px,4vw,36px);background:#f3faf4;color:#14352a;font-family:Georgia,Times,serif;font-size:17px;line-height:1.8;border-top:8px solid #0b6e4f'>
<header style='display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px;padding:0 0 16px;margin:0 0 18px;border-bottom:2px solid #f4a261'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:32px;width:auto;display:block'><span style='font-family:Arial,Helvetica,sans-serif;font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#0b6e4f'>JAIHO777 / VALUE DESK</span></div>
<p style='margin:0;padding:8px 12px;background:#f4a261;color:#14352a;font-family:Arial,Helvetica,sans-serif;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border-radius:8px'>UP TO 180%</p>
</header>
<p style='margin:0 0 8px;text-align:center;font-family:Arial,Helvetica,sans-serif;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#c0763a'>EDITORIAL · DEPOSIT MORE?</p>
<h1 style='margin:0 0 12px;text-align:center;font-size:clamp(28px,5vw,44px);line-height:1.12;color:#0b6e4f'>Deposit More on JAIHO777? Only If Up to 180% Extra Value Survives Your Fine-Print Check</h1>
<p style='margin:0 auto 16px;max-width:720px;text-align:center;color:#3d5c4e'>A mature take for loyal wallets: dragon-jungle hype is fine — blind recharges are not.</p>
<p style='margin:0 0 22px;text-align:center'>{cta('RECHARGE AFTER YOU READ','#0b6e4f','#f3faf4','#f4a261','12px')}</p>
<figure style='max-width:720px;margin:0 auto 26px;padding:8px;background:#ffffff;border:3px solid #0b6e4f;border-radius:18px;box-sizing:border-box'>
<img src='{IMG[1]}' alt='JAIHO777 deposit bonus banner unlock up to 180 percent extra value with dragon adventure art' title='JAIHO777 180 percent deposit bonus' style='width:100%;height:auto;display:block;margin:0;border-radius:12px'>
<figcaption style='margin:0;padding:10px 6px 2px;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#3d5c4e;text-align:center'>Campaign cue: deposit more, unlock extra value — get up to 180% deposit bonus.</figcaption>
</figure>
<nav style='display:flex;flex-wrap:wrap;gap:12px;justify-content:center;padding:0 0 18px'>
<a href='#honest' style='font-family:Arial,Helvetica,sans-serif;color:#0b6e4f;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>HONEST TAKE</a>
<a href='#compare' style='font-family:Arial,Helvetica,sans-serif;color:#0b6e4f;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>COMPARE FIRST</a>
<a href='#faq-dep' style='font-family:Arial,Helvetica,sans-serif;color:#0b6e4f;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>FAQ</a>
</nav>
<section id='honest'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0b6e4f'>The honest take on 180% energy</h2>
<p style='margin:0 0 14px'>Indian cash-game veterans have seen every percentage. Up to 180% is theater until wagering rules, eligible games, and caps appear. JAIHO777’s dragon-jungle creative does excitement well: deposit more, unlock extra value, recharge and activate. The editorial job is quieter — tell loyal players how to evaluate without getting hypnotized.</p>
<p style='margin:0 0 14px'>If you play from Hyderabad or Ahmedabad with a fixed weekly entertainment budget, a bigger percentage helps only when it improves a top-up you already planned. It becomes dangerous when the banner invents a top-up you did not need.</p>
</section>
<section id='compare'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0b6e4f'>What experienced players compare before activating</h2>
<ul style='margin:0 0 16px;padding:0;list-style:none'>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:14px;border-top:4px solid #f4a261'><strong style='font-family:Arial,Helvetica,sans-serif;color:#c0763a'>Value math</strong> — compare percentage against playthrough and game weighting.</li>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:14px;border-top:4px solid #f4a261'><strong style='font-family:Arial,Helvetica,sans-serif;color:#c0763a'>Payment friction</strong> — UPI, Paytm, PhonePe, Google Pay clarity beats cute dragons.</li>
<li style='margin:0 0 0;padding:14px;background:#ffffff;border-radius:14px;border-top:4px solid #f4a261'><strong style='font-family:Arial,Helvetica,sans-serif;color:#c0763a'>Support readiness</strong> — 24/7 tone and withdrawal trust matter after activation.</li>
</ul>
<p style='margin:0 0 14px'>Schedule FOMO. Decide one recharge window. If the lane is live then, fine. If not, skip. Bonuses are tools, not guarantees. Download the official legacy APK, read the reward panel, screenshot terms, then top up with a calm head.</p>
<p style='margin:0 0 14px'>Hinglish rule: “Bonus bada hai, dimaag bada rakhna.” Beginners should not max deposits just to unlock a headline. Desire born from golden eggs should wait overnight. Desire that survives sleep is usually safer.</p>
<p style='margin:0 0 14px'>Bottom line for loyal wallets: evaluate playthrough, payment friction, and KYC-aware withdrawals first. Then enjoy the adventure art. That order is how long-running JAIHO777 players stay long-running instead of burning out after one hyped recharge.</p>
<p style='margin:0 0 14px'>If the live offer truly improves a deposit already on your weekly plan, activate. If the banner alone created the urge, wait. Extra value that costs your peace is not value.</p>
<p style='margin:0 0 14px'>Adventure art can stay colorful without becoming a trap. Think of the 180% lane like a limited travel upgrade: nice when it fits the itinerary, silly when it forces a trip you cannot afford. Screenshot the live terms. Ask support only inside the app. Never share OTPs with strangers promising secret recharge codes.</p>
<p style='margin:0 0 14px'>That is the mature JAIHO777 reading of deposit more unlock extra value — excitement second, verification first. Loyal players already know the brand. What they need now is a clean decision framework, not louder dragons.</p>
<p style='margin:0 0 14px'>Simple overnight rule: only activate when the recharge amount was written in your weekly plan before you saw the banner. If the dragons wrote the number for you, wait until morning.</p>
<p style='margin:0 0 18px;text-align:center'>{cta('ACTIVATE ON OFFICIAL APK','#f4a261','#14352a','#0b6e4f','999px')}</p>
</section>
<section id='faq-dep'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0b6e4f'>FAQ</h2>
<p style='margin:0 0 6px;font-family:Arial,Helvetica,sans-serif;font-weight:800'>Is 180% automatic for every deposit?</p>
<p style='margin:0 0 12px'>No. Creatives say up to 180%. Final value depends on live rules.</p>
<p style='margin:0 0 6px;font-family:Arial,Helvetica,sans-serif;font-weight:800'>Does a bigger bonus guarantee winnings?</p>
<p style='margin:0 0 12px'>Absolutely not. Real cash games still vary.</p>
<p style='margin:0 0 6px;font-family:Arial,Helvetica,sans-serif;font-weight:800'>Where to install?</p>
<p style='margin:0 0 0'>Use only the JAIHO777 legacy APK button in this article.</p>
</section>
</article>"""


# 3 Sunny product campaign — sky blue + sunny yellow — Chicken Road mega win
def art3():
    return f"""<article style='max-width:960px;margin:0 auto;box-sizing:border-box;padding:0;background:#eef9ff;color:#1d3557;font-family:Trebuchet MS,Arial,Helvetica,sans-serif;font-size:16px;line-height:1.7;overflow:hidden'>
<div style='padding:14px 16px;display:flex;align-items:center;justify-content:space-between;background:#1d3557'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:30px;width:auto;display:block;background:#ffffff;border-radius:8px;padding:2px'><span style='color:#a8dadc;font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase'>JAIHO777 / STREET DESK</span></div>
<span style='background:#ffd60a;color:#1d3557;padding:8px 12px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border-radius:999px'>CHICKEN ROAD 3</span>
</div>
<div style='padding:clamp(20px,4vw,36px) 16px 6px;text-align:center;background:radial-gradient(circle at top,#ffffff 0%,#eef9ff 75%)'>
<p style='margin:0 0 8px;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#457b9d'>MEMBER STORY · MEGA WIN SPOTLIGHT</p>
<h1 style='margin:0 0 12px;font-size:clamp(30px,5.2vw,46px);line-height:1.1;color:#1d3557'>Chicken Road 3 on JAIHO777: A ₹41,700 Mega Win Moment — and the Caution Sign Loyal Players Should Read</h1>
<p style='margin:0 auto 16px;max-width:700px;color:#457b9d'>UID 215***861 made the sunny street banner. Enjoy the vibe, keep the bankroll rules brighter than the coins.</p>
<p style='margin:0 0 16px'>{cta('GET THE LEGACY APP','#ffd60a','#1d3557','#1d3557','999px')}</p>
</div>
<figure style='max-width:740px;margin:0 auto 20px;padding:10px;background:#1d3557;border-radius:24px;box-sizing:border-box'>
<img src='{IMG[2]}' alt='JAIHO777 Chicken Road 3 mega win showcase with Rs 41700 and masked UID' title='Chicken Road 3 mega win' style='width:100%;height:auto;display:block;margin:0;border-radius:16px'>
<figcaption style='margin:0;padding:10px 6px 2px;color:#a8dadc;font-size:12px;text-align:center'>Showcase: MEGA WIN · ₹41,700 · Chicken Road 3 — fun spotlight, not a forecast.</figcaption>
</figure>
<nav style='display:flex;flex-wrap:wrap;gap:10px;justify-content:center;padding:0 12px 18px'>
<a href='#story' style='text-decoration:none;background:#ffffff;color:#1d3557;padding:8px 12px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border:2px solid #4cc9f0'>THE STORY</a>
<a href='#caution' style='text-decoration:none;background:#ffffff;color:#1d3557;padding:8px 12px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border:2px solid #4cc9f0'>CAUTION SIGN</a>
<a href='#faq-ch' style='text-decoration:none;background:#ffffff;color:#1d3557;padding:8px 12px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border:2px solid #4cc9f0'>FAQ</a>
</nav>
<div style='padding:0 16px 34px'>
<section id='story'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#1d3557'>The sunny member-story texture</h2>
<p style='margin:0 0 14px;color:#2f4d6f'>Chicken Road 3 creatives lean playful: yellow bird energy, cobblestone street, floating coins, caution sign with a chicken silhouette. That lightness is modern. It does not make outcomes certain. A ₹41,700 mega win for a masked UID is a highlight reel for JAIHO777 communities — useful for mood, useless as a homework target.</p>
<p style='margin:0 0 14px;color:#2f4d6f'>Loyal players in Delhi PGs and Kochi cafes can celebrate without confusing inspiration with instruction. Hinglish: “Maza aaya, math mat bhoolna.” Real cash games remain risky whether the art is neon night or sunny afternoon.</p>
</section>
<section id='caution'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#1d3557'>Read the caution sign before you cross</h2>
<ul style='margin:0 0 16px;padding:0;list-style:none'>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:18px;border:2px dashed #ffd60a'><strong style='color:#e63946'>Official lane only</strong> — install the legacy APK from this page, not random mirrors.</li>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:18px;border:2px dashed #ffd60a'><strong style='color:#e63946'>Tiny experiment</strong> — if inspired, start with a surplus-only stake and a hard timer.</li>
<li style='margin:0 0 0;padding:14px;background:#ffffff;border-radius:18px;border:2px dashed #ffd60a'><strong style='color:#e63946'>No revenge traffic</strong> — near-misses are not a green light to double.</li>
</ul>
<p style='margin:0 0 14px;color:#2f4d6f'>Payment habits stay ordinary: UPI, Paytm, PhonePe, Google Pay when available — always from entertainment surplus. Withdrawal trust still depends on KYC. 24/7 support is for account friction, not for rewriting variance after a showcase screenshot hits your group.</p>
<p style='margin:0 0 14px;color:#2f4d6f'>If friends forward the ₹41,700 banner, reply with the caution sign energy: celebrate, then protect process. Chicken Road 3 can be a short joyful session on JAIHO777. It should not become an all-afternoon argument with your future rent money.</p>
<p style='margin:0 0 14px;color:#2f4d6f'>Product-style close: confirm the game is live in your lobby after install, learn the pace on the smallest comfortable stake, and exit while the street still feels sunny. Mega win art will keep circulating. Your discipline has to be rebuilt by you.</p>
<p style='margin:0 0 14px;color:#2f4d6f'>That is the modern member-story format for a legacy brand audience — warm, clear, and adult. No stiff brochure tone. No fake certainty. Just a bright spotlight with a readable stop line.</p>
<p style='margin:0 0 14px;color:#2f4d6f'>Parents or older cousins who see the chicken banner may ask what it means. Explain simply: a playful game spotlight inside a real cash game app, with age rules and no guaranteed outcomes. That sentence travels better through family chats than raw hype alone.</p>
<p style='margin:0 0 14px;color:#2f4d6f'>Cross when the light is green in your own plan — surplus funds, clear timer, official APK. Otherwise wait on the curb. The street will still be sunny tomorrow; forced top-ups rarely are.</p>
<p style='margin:0 0 18px;text-align:center'>{cta('OPEN JAIHO777 NOW','#4cc9f0','#1d3557','#1d3557','18px')}</p>
</section>
<section id='faq-ch'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#1d3557'>FAQ</h2>
<div style='display:flex;flex-direction:column;gap:10px'>
<div style='padding:12px 14px;background:#ffffff;border-radius:14px'><strong style='display:block;margin:0 0 4px'>Can I aim for the same ₹41,700?</strong><span style='color:#457b9d'>No responsible desk would promise that. Results vary.</span></div>
<div style='padding:12px 14px;background:#ffffff;border-radius:14px'><strong style='display:block;margin:0 0 4px'>Is Chicken Road 3 always available?</strong><span style='color:#457b9d'>Check the live JAIHO777 lobby after install.</span></div>
<div style='padding:12px 14px;background:#ffffff;border-radius:14px'><strong style='display:block;margin:0 0 4px'>Where is the correct APK?</strong><span style='color:#457b9d'>Only the legacy package button in this article.</span></div>
</div>
</section>
</div>
</article>"""


META = [
    {
        'file': '01-wild-ape-mega-win.html',
        'title': 'Wild Ape II EX on JAIHO777: What a ₹2.66 Lakh Mega Win Showcase Should Teach Loyal Players',
        'keywords': 'Wild Ape II EX spotlight, mega win member story, neon lobby discipline, loyal cash game lessons',
        'description': 'A JAIHO777 Wild Ape II EX ₹266,000 showcase decoded for loyal players—steal bankroll lessons, not copy-paste jackpot fantasy.',
        'fn': art1,
    },
    {
        'file': '02-deposit-180-bonus.html',
        'title': 'Deposit More on JAIHO777? Only If Up to 180% Extra Value Survives Your Fine-Print Check',
        'keywords': '180 percent deposit bonus, recharge activate value, playthrough before top up, mature wallet evaluation',
        'description': 'Mature editorial on JAIHO777’s up-to-180% deposit pitch—what loyal Indian players should compare before recharging.',
        'fn': art2,
    },
    {
        'file': '03-chicken-road-mega-win.html',
        'title': 'Chicken Road 3 on JAIHO777: A ₹41,700 Mega Win Moment — and the Caution Sign Loyal Players Should Read',
        'keywords': 'Chicken Road 3 win story, sunny mega win spotlight, caution before chase, short session cash games',
        'description': 'Chicken Road 3 ₹41,700 mega win coverage for JAIHO777 regulars—keep the sunny vibe, read the caution sign, protect process.',
        'fn': art3,
    },
]


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    PUB.mkdir(parents=True, exist_ok=True)
    (PUB / 'per-artikel').mkdir(parents=True, exist_ok=True)
    all_parts = [
        'JAIHO777 BATCH 08 — PROSAFEBET (SITUS LAMA)',
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
        '# Batch 08 Legacy — Fresh inline articles\n\n'
        'Copy-paste: `../../publish/batch-08-legacy/`\n\n'
        '3 artikel (3 gambar). APK situs lama. Full inline CSS.\n',
        encoding='utf-8',
    )
    (PUB / 'README.md').write_text(
        '# Batch 08 Legacy Copy Pack\n\n'
        '- `COPY-PASTE-SEMUA-ARTIKEL.txt`\n'
        '- `per-artikel/artikel-01.txt` ... `artikel-03.txt`\n',
        encoding='utf-8',
    )
    print('DONE')


if __name__ == '__main__':
    main()
