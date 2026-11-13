#!/usr/bin/env python3
"""Batch 10 — Prosafebet / legacy JAIHO777 — 4 pro inline articles."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PUB = ROOT.parent.parent / 'publish' / 'batch-10-legacy'
LOGO = 'https://www.prosafeimg.com/uploads/20260731/6a6c6e378c7f6.png'
APK = 'https://d3iha5lcurdryc.cloudfront.net/jaiho777a_J6NJ4881PJ3.apk'
IMG = [
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVATWp3rcjWCaz8g3pOlCAX9C_Mxy5gUF0f6zEwCAchfJoST2oshYSO7qSUzHQTRyle1QVf76ZKDWuHCHDgVckC1uZJ6gcS7RiTgXx20HQS-45hIH3x_HQtMf7_C7USIBLurSd4D6e5X1ti8uELMTdXrS0aQ-RzvJ0L_WCBL5_y4KsIjFc4kFzvb0GTDaL/s700/P157.1_850x1280_700x500.webp',
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8liF8Jl8mpy-y0DFpWIWpJZp4IFS-twt40ebfTwygim1EpSCDTpjTRxgpLl7dZJGUhtbM48JXkz_inIMtQoILoZSKfqoXV3sb1BkHg93anhSasvaSgA30vrNV6Svn-d8rv8jBf2xRVMnz9QYjJgnWsbsstMH6PLVu8Y8HUce7jEN206e4TfMYSOze7YMn/s700/P157.3_700x500.webp',
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjP9_jrOFqFPbPmFm8xugQ2tsfkwfAmHXwhe4w3soz-GYeBZB8mEIqdtib2ILmkkN04kbrMlgmq39Wfd4CzNNT3zomdSTEmpfPsjGEHxwH8E84dWJYclZ23goh_Uxt4RHPbM0V8k_8FMmcFraDOVgYuQdfZlZsJbyCWCp2rDIYNZsS2uzgXJyeYXqH_jhc-/s700/P157.4_700x500.webp',
    'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEO0_bam0KZ95XGfXSWobisNN1HSE27Pn3LvoBKsWfvohAmifWE7qUqZNWgaveE9f0dlyv8nfURV06SmcdXksWKaeSKdMXnWkcNjXFf_Cex1TKPSmvEBKUrILDfdGo5Z5Dgktpgufsrg8YRzgViwaRiICdxmLwWSqGy9TUpx67KtM1wxfJSs474YjBIsu_/s700/P157.5-1_700x500.webp',
]


def ok(html, name):
    if '"' in html or '<style' in html.lower() or re.search(r'<br\b', html, re.I) or '&nbsp;' in html:
        raise SystemExit(f'{name}: forbidden')
    if 'adminsafebet' in html.lower() or 'jaiho777_119' in html or 'prosafebet.com/admin' in html.lower():
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


# 1 Newsroom / channel desk — Telegram secret codes (ink + telegram blue)
def art1():
    return f"""<article style='max-width:940px;margin:0 auto;box-sizing:border-box;padding:0;background:#f3f6f9;color:#0f1a24;font-family:Georgia,Times New Roman,serif;font-size:16px;line-height:1.72;overflow:hidden;border:1px solid #d5dee8'>
<div style='padding:12px 16px;display:flex;align-items:center;justify-content:space-between;background:#0f1a24;font-family:Arial,Helvetica,sans-serif'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:28px;width:auto;display:block'><span style='color:#8ec8ff;font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase'>JAIHO777 LEGACY · CHANNEL DESK</span></div>
<span style='background:#229ed9;color:#ffffff;padding:6px 11px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>TELEGRAM CODES</span>
</div>
<div style='padding:clamp(20px,4vw,34px) 18px 8px'>
<p style='margin:0 0 8px;font-family:Arial,Helvetica,sans-serif;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#229ed9'>FEATURE STORY · LOYAL PLAYER BRIEF</p>
<h1 style='margin:0 0 12px;font-size:clamp(28px,5vw,42px);line-height:1.12;color:#0f1a24'>Don’t Miss Today’s Secret Code on JAIHO777 — Fresh Promo Codes Daily on Telegram, Without Getting Played</h1>
<p style='margin:0 0 14px;font-family:Arial,Helvetica,sans-serif;font-size:16px;color:#3a4a5a'>For legacy regulars who already know the lobby: today’s secret code is a channel habit, not a stranger’s DM. Follow, unlock, verify — then play with surplus only.</p>
<p style='margin:0 0 16px;font-family:Arial,Helvetica,sans-serif'>{cta('UNLOCK VIA OFFICIAL APK','#229ed9','#ffffff','#0d5f86','4px')}</p>
</div>
<figure style='margin:0 18px 20px;padding:0;border:1px solid #c8d4e0;background:#ffffff;box-sizing:border-box'>
<img src='{IMG[0]}' alt='JAIHO777 secret code Telegram promo banner with follow and unlock rewards creative' title='JAIHO777 Telegram secret codes' style='width:100%;height:auto;display:block;margin:0'>
<figcaption style='margin:0;padding:10px 12px;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#5a6a7a'>Creative cue: don’t miss today’s secret code — fresh promo codes daily on Telegram.</figcaption>
</figure>
<nav style='display:flex;flex-wrap:wrap;gap:12px;justify-content:center;padding:0 12px 18px;font-family:Arial,Helvetica,sans-serif'>
<a href='#why-code' style='color:#229ed9;text-decoration:none;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>WHY CODES</a>
<a href='#verify' style='color:#229ed9;text-decoration:none;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>VERIFY</a>
<a href='#faq-tg' style='color:#229ed9;text-decoration:none;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>FAQ</a>
</nav>
<div style='padding:0 18px 34px'>
<section id='why-code'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0f1a24'>Why secret-code days still matter for legacy players</h2>
<p style='margin:0 0 14px;color:#2a3846'>Loyal Indian cash-game audiences already live on Telegram for cricket updates and festival forwards. JAIHO777’s “don’t miss today’s secret code” creative rides that habit with castle-night art and follow-and-unlock language. Mature play means treating codes as optional boosts — never as a reason to fund from rent money in Mumbai or Delhi.</p>
<p style='margin:0 0 14px;color:#2a3846'>Hinglish for the hostel group: “Code mil gaya toh theek, OTP mat dena.” Fresh promo codes daily on Telegram only help if the channel and the APK are authentic. Clone channels thrive on FOMO. Your edge is verification, not speed.</p>
</section>
<section id='verify'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0f1a24'>A newsroom-style verify checklist</h2>
<ul style='margin:0 0 16px;padding:0;list-style:none;font-family:Arial,Helvetica,sans-serif'>
<li style='margin:0 0 10px;padding:12px 14px;background:#ffffff;border-left:4px solid #229ed9'><strong>1</strong> — Install only the legacy JAIHO777 APK from this page.</li>
<li style='margin:0 0 10px;padding:12px 14px;background:#ffffff;border-left:4px solid #229ed9'><strong>2</strong> — Open in-app notices for the correct Telegram follow path.</li>
<li style='margin:0 0 10px;padding:12px 14px;background:#ffffff;border-left:4px solid #229ed9'><strong>3</strong> — Redeem inside the wallet panel; never pay a “code seller.”</li>
<li style='margin:0 0 0;padding:12px 14px;background:#ffffff;border-left:4px solid #229ed9'><strong>4</strong> — Cap the session. UPI / Paytm / PhonePe / Google Pay from surplus only.</li>
</ul>
<p style='margin:0 0 14px;color:#2a3846'>Feature-story truth: secret codes reward attention, not recklessness. If a chat asks for remote access, PIN, or KYC photos outside the app, exit. 24/7 support belongs inside official help routes — not in random DMs promising denser codes.</p>
<p style='margin:0 0 14px;color:#2a3846'>Progressive regulars in Bangalore and Hyderabad treat daily codes like a morning newspaper column — skim, claim if eligible, move on. Missing one day is not a crisis. Chasing a missed code with a double deposit is. That distinction keeps Telegram loyalty lanes feeling professional instead of needy.</p>
<p style='margin:0 0 14px;color:#2a3846'>When friends forward the ape-and-castle banner, ask for the install path first. Screenshots can be edited. Official APK + in-app notice + verified channel is the triangle. Anything outside that triangle is noise dressed as urgency.</p>
<p style='margin:0 0 14px;color:#2a3846'>Closing beat for loyal wallets: follow and unlock your rewards after you respect your stop-loss. JAIHO777 can host today’s secret code. You host the decision to redeem, play short, and leave with tomorrow intact.</p>
<p style='margin:0 0 14px;color:#2a3846'>Network hygiene still counts. Prefer stable Wi-Fi or data before install. Enable unknown sources only for the install window, then tighten settings again. Small habits separate mature legacy players from impulse browsers who click every mirror link after a festival forward.</p>
<p style='margin:0 0 14px;color:#2a3846'>If the code window expires, do not hunt grey-market sellers. Wait for the next official drop. Patience is a trust signal you give yourself — and it pairs better with earning games than panic tapping ever will.</p>
<p style='margin:0 0 18px;font-family:Arial,Helvetica,sans-serif'>{cta('DOWNLOAD LEGACY APP','#0f1a24','#ffffff','#229ed9','4px')}</p>
</section>
<section id='faq-tg'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0f1a24'>FAQ</h2>
<p style='margin:0 0 6px;font-family:Arial,Helvetica,sans-serif;font-weight:800'>Are Telegram codes guaranteed daily forever?</p>
<p style='margin:0 0 12px;color:#2a3846'>No. Check live channel posts and in-app eligibility.</p>
<p style='margin:0 0 6px;font-family:Arial,Helvetica,sans-serif;font-weight:800'>Do codes guarantee profit?</p>
<p style='margin:0 0 12px;color:#2a3846'>No. Promo value is not a win promise in real cash games.</p>
<p style='margin:0 0 6px;font-family:Arial,Helvetica,sans-serif;font-weight:800'>Safe start?</p>
<p style='margin:0 0 0;color:#2a3846'>Legacy APK on this page, then verified Telegram path only.</p>
</section>
</div>
</article>"""


# 2 IPL sports countdown — Weekly bonus arrives TOMORROW (saffron + charcoal)
def art2():
    return f"""<article style='max-width:980px;margin:0 auto;box-sizing:border-box;padding:0;background:#101214;color:#f2f2f0;font-family:Arial Black,Impact,Arial,sans-serif;overflow:hidden'>
<div style='padding:12px 16px;display:flex;align-items:center;justify-content:space-between;border-bottom:4px solid #ff6b00;font-family:Arial,Helvetica,sans-serif'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:28px;width:auto;display:block'><span style='font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#ffb380'>JAIHO777 LEGACY · COUNTDOWN DESK</span></div>
<span style='background:#ff6b00;color:#101214;padding:6px 10px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>T-MINUS BONUS</span>
</div>
<div style='padding:clamp(18px,4vw,36px) 16px 10px;background:linear-gradient(135deg,#1a1210 0%,#101214 55%,#151820 100%)'>
<p style='margin:0 0 8px;font-family:Arial,Helvetica,sans-serif;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#ff6b00'>EDITORIAL OPINION · WEEKLY DROP</p>
<h1 style='margin:0 0 12px;font-size:clamp(30px,5.5vw,48px);line-height:0.98;text-transform:uppercase;letter-spacing:0.4px;color:#ffffff'>Your Weekly Bonus Arrives Tomorrow on JAIHO777 — Exclusive Rewards Are Coming, So Get Ready Without Going Reckless</h1>
<p style='margin:0 0 16px;max-width:720px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.65;font-weight:400;color:#d5d0c8'>Fire-wolf energy sells the countdown. Mature legacy players steal the preparation — not the fantasy that tomorrow prints free money.</p>
<p style='margin:0 0 16px;font-family:Arial,Helvetica,sans-serif;font-weight:400'>{cta('GET READY ON OFFICIAL APK','#ff6b00','#101214','#8a3a00','0')}</p>
</div>
<figure style='margin:0;padding:0;border-top:4px solid #ff6b00;border-bottom:4px solid #ff6b00'>
<img src='{IMG[1]}' alt='JAIHO777 weekly bonus arrives tomorrow exclusive rewards coming fire wolf banner' title='JAIHO777 weekly bonus tomorrow' style='width:100%;height:auto;display:block;margin:0'>
<figcaption style='margin:0;padding:10px 14px;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#b9b0a6;background:#16181c'>Broadcast cue: weekly bonus arrives tomorrow — exclusive rewards, log in and claim readiness.</figcaption>
</figure>
<nav style='display:flex;flex-wrap:wrap;gap:14px;justify-content:center;padding:12px;font-family:Arial,Helvetica,sans-serif;background:#16181c'>
<a href='#take' style='color:#ff6b00;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>THE TAKE</a>
<a href='#prep' style='color:#ff6b00;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>PREP LIST</a>
<a href='#faq-wb' style='color:#ff6b00;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>FAQ</a>
</nav>
<div style='padding:clamp(18px,3vw,32px) 16px 36px;font-family:Arial,Helvetica,sans-serif;font-weight:400;line-height:1.7'>
<section id='take'>
<h2 style='margin:0 0 10px;font-family:Arial Black,Impact,Arial,sans-serif;font-size:clamp(22px,3.4vw,30px);text-transform:uppercase;color:#ff6b00;letter-spacing:1px'>Editorial take: tomorrow is a calendar, not a blank cheque</h2>
<p style='margin:0 0 14px;color:#ddd6ce'>Sports-broadcast branding loves countdowns — IPL toss clocks, WTC final timers, Diwali sale ticks. JAIHO777’s “weekly bonus arrives tomorrow” creative borrows that pulse: volcanic wolf, exclusive rewards ribbon, get-ready-to-log-in CTA. Opinion from a loyal-player desk: anticipation is healthy; overfunding the night before is not.</p>
<p style='margin:0 0 14px;color:#ddd6ce'>Hinglish: “Kal aayega bonus, aaj budget todd ke mat baith.” Real cash games and earning games still carry risk after any claim. Exclusive rewards are coming for eligible accounts — not for every screenshot forward in a Goa hostel chat.</p>
</section>
<section id='prep'>
<h2 style='margin:0 0 10px;font-family:Arial Black,Impact,Arial,sans-serif;font-size:clamp(22px,3.4vw,30px);text-transform:uppercase;color:#ff6b00;letter-spacing:1px'>Prep list before the claim window</h2>
<ul style='margin:0 0 16px;padding:0;list-style:none'>
<li style='margin:0 0 8px;padding:12px 14px;background:#1a1c20;border-left:5px solid #ff6b00'><strong style='color:#ffb380'>Confirm the app</strong> — legacy APK only from this article.</li>
<li style='margin:0 0 8px;padding:12px 14px;background:#1a1c20;border-left:5px solid #ff6b00'><strong style='color:#ffb380'>Read eligibility</strong> — weekly windows and KYC states vary.</li>
<li style='margin:0 0 8px;padding:12px 14px;background:#1a1c20;border-left:5px solid #ff6b00'><strong style='color:#ffb380'>Pre-write stakes</strong> — decide stop-loss before the fire-wolf hype hits.</li>
<li style='margin:0 0 0;padding:12px 14px;background:#1a1c20;border-left:5px solid #ff6b00'><strong style='color:#ffb380'>Sleep first</strong> — tired thumbs make expensive late claims.</li>
</ul>
<p style='margin:0 0 14px;color:#ddd6ce'>UPI convenience is not a green light. Paytm, PhonePe, and Google Pay should move entertainment surplus only. Instant withdrawal storytelling still sits behind KYC and fair-play checks. 24/7 support can fix login friction; it cannot rewrite a reckless top-up.</p>
<p style='margin:0 0 14px;color:#ddd6ce'>Compared with random midweek drops, a weekly cadence helps disciplined regulars. Compared with FOMO forwards, a written plan wins. Progressive India audiences from Chennai to Jaipur already know tournament calendars — apply the same calm to bonus calendars.</p>
<p style='margin:0 0 14px;color:#ddd6ce'>If friends demand you “load heavy tonight so tomorrow hits harder,” mute that noise. Exclusive rewards arriving tomorrow reward presence and eligibility, not sleep deprivation. Get ready to log in and claim — then leave while you still respect the week ahead.</p>
<p style='margin:0 0 14px;color:#ddd6ce'>Final whistle: JAIHO777 can run the countdown creative. You run the clock on your wallet. That is how a fiery weekly teaser stays cool for loyal players instead of becoming another stiff regret story.</p>
<p style='margin:0 0 14px;color:#ddd6ce'>One more broadcast note: when the claim button lights up, treat it like a powerplay over — short, intentional, finished. Stretching a weekly bonus into an all-night chase is how exclusive rewards lose their shine. Log the claim, play a capped sample, walk.</p>
<p style='margin:0 0 14px;color:#ddd6ce'>Hardware reality for the countdown night: charge the phone, mute non-essential banking alerts, and keep a glass of water nearby instead of a second coffee that stretches the session. Tired loyalty is still loyalty — it does not need to become a highlight reel of regret. Exclusive rewards are coming for players who show up clear-headed.</p>
<p style='margin:0 0 14px;color:#ddd6ce'>If the teaser creative shows diamonds and gift boxes, treat them as art direction. Art exaggerates. Your wallet should not. Get ready to log in, claim what you are eligible for, and protect the rest of the week like a professional desk protects a match calendar.</p>
<p style='margin:0 0 18px'>{cta('LOG IN READY — INSTALL','#ffffff','#101214','#ff6b00','0')}</p>
</section>
<section id='faq-wb'>
<h2 style='margin:0 0 10px;font-family:Arial Black,Impact,Arial,sans-serif;font-size:clamp(22px,3.4vw,30px);text-transform:uppercase;color:#ff6b00;letter-spacing:1px'>FAQ</h2>
<p style='margin:0 0 6px;font-weight:800;color:#ffffff'>Is the weekly bonus identical every week?</p>
<p style='margin:0 0 12px;color:#ddd6ce'>No. Check live rules after install.</p>
<p style='margin:0 0 6px;font-weight:800;color:#ffffff'>Does “arrives tomorrow” mean guaranteed profit?</p>
<p style='margin:0 0 12px;color:#ddd6ce'>No. It signals a promo window, not a payout promise.</p>
<p style='margin:0 0 6px;font-weight:800;color:#ffffff'>Where to prepare safely?</p>
<p style='margin:0 0 0;color:#ddd6ce'>Install the legacy JAIHO777 APK from this page only.</p>
</section>
</div>
</article>"""


# 3 Nautical chart / ship log — Weekly bonus IS HERE (navy + seafoam + parchment)
def art3():
    return f"""<article style='max-width:960px;margin:0 auto;box-sizing:border-box;padding:clamp(16px,3.5vw,32px);background:#f7f3ea;color:#0a2540;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.7;border-top:10px solid #0a2540'>
<header style='display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px;padding:0 0 14px;margin:0 0 16px;border-bottom:2px dashed #7fdbda'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:30px;width:auto;display:block'><span style='font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#0a2540'>JAIHO777 LEGACY · SHIP LOG</span></div>
<p style='margin:0;padding:8px 12px;background:#0a2540;color:#7fdbda;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>CLAIM WINDOW OPEN</p>
</header>
<p style='margin:0 0 8px;text-align:center;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#0d7377'>COMPARISON BRIEF · WEEKLY BONUS LIVE</p>
<h1 style='margin:0 0 12px;text-align:center;font-size:clamp(28px,4.8vw,42px);line-height:1.12;color:#0a2540'>Your Weekly Bonus Is Here on JAIHO777 — Exclusive Rewards Available Today, If You Claim Like a Captain Not a Looter</h1>
<p style='margin:0 auto 16px;max-width:700px;text-align:center;color:#3d4f5f'>Pirate-cabin treasure art says the window is live. A mature comparison: structured weekly claims beat impulse “log in and spray” nights every time.</p>
<p style='margin:0 0 20px;text-align:center'>{cta('LOG IN & CLAIM PATH','#0d7377','#ffffff','#084a4d','8px')}</p>
<figure style='max-width:720px;margin:0 auto 22px;padding:12px;background:#ffffff;border:2px solid #0a2540;box-sizing:border-box'>
<img src='{IMG[2]}' alt='JAIHO777 weekly bonus is here exclusive rewards available today pirate octopus claim banner' title='JAIHO777 weekly bonus is here' style='width:100%;height:auto;display:block;margin:0'>
<figcaption style='margin:0;padding:10px 4px 0;font-size:12px;color:#3d4f5f;text-align:center'>Ship-log cue: weekly bonus is here — exclusive rewards available today.</figcaption>
</figure>
<nav style='display:flex;flex-wrap:wrap;gap:10px;justify-content:center;padding:0 0 18px'>
<a href='#compare' style='text-decoration:none;background:#ffffff;color:#0a2540;padding:8px 12px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border:2px solid #7fdbda'>COMPARE</a>
<a href='#claim-map' style='text-decoration:none;background:#ffffff;color:#0a2540;padding:8px 12px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border:2px solid #7fdbda'>CLAIM MAP</a>
<a href='#faq-here' style='text-decoration:none;background:#ffffff;color:#0a2540;padding:8px 12px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border:2px solid #7fdbda'>FAQ</a>
</nav>
<section id='compare'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0d7377'>Weekly claim vs midweek chaos</h2>
<p style='margin:0 0 14px;color:#2c3e4e'>When exclusive rewards are available today, FOMO spikes. Comparison for loyal JAIHO777 players: a weekly claim with a written stake plan usually beats three random midweek top-ups driven by group-chat screenshots. The octopus-pirate creative is fun packaging. Process is the product loyalty move.</p>
<p style='margin:0 0 14px;color:#2c3e4e'>Versus competitor clones that spam “claim now or lose forever,” a calm ship-log approach wins: install authentic APK, read the panel, claim if eligible, play a capped sample, exit. That is how Goa weekend energy stays recreational instead of becoming a hangover for your UPI balance.</p>
</section>
<section id='claim-map'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0d7377'>Claim map for captains</h2>
<ul style='margin:0 0 16px;padding:0;list-style:none'>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:0;border:1px solid #c9d6c8'><strong>Dock</strong> — download the legacy APK from this page only.</li>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border:1px solid #c9d6c8'><strong>Read the chart</strong> — eligibility, expiry, wagering notes if listed.</li>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border:1px solid #c9d6c8'><strong>Claim once</strong> — log in and claim without stacking panic deposits.</li>
<li style='margin:0 0 0;padding:14px;background:#ffffff;border:1px solid #c9d6c8'><strong>Sail short</strong> — surplus funds via UPI / Paytm / PhonePe / Google Pay only.</li>
</ul>
<p style='margin:0 0 14px;color:#2c3e4e'>Hinglish: “Bonus aa gaya, dimaag mat doobana.” Instant withdrawal stories still sit behind KYC. 24/7 support helps with account friction — not with reversing a night you stretched past your stop time.</p>
<p style='margin:0 0 14px;color:#2c3e4e'>Progressive players in Pune and Kolkata who treat “available today” as a calendar item — not a personality test — keep brand trust intact. Share the banner if you want; share the claim map too. Cool creative without cool process is just noise on a parchment page.</p>
<p style='margin:0 0 14px;color:#2c3e4e'>If the panel says you are not eligible yet, wait. Forcing a deposit to “unlock” a weekly bonus that is not yours yet is how exclusive rewards become expensive lessons. Captains wait for clear water.</p>
<p style='margin:0 0 14px;color:#2c3e4e'>Close the log: your weekly bonus is here. Claim like you mean to return next week. JAIHO777 can host the treasure cabin. You host the boundaries that keep earning games adult.</p>
<p style='margin:0 0 14px;color:#2c3e4e'>One more chart note for Diwali-week and IPL-week overlaps: festival FOMO stacks easily. If a weekly bonus lands on a loud social night, shrink the session further. Celebration calendars and claim calendars should not both empty the same wallet in one evening.</p>
<p style='margin:0 0 14px;color:#2c3e4e'>When comparing JAIHO777’s live weekly window with random “flash claim” spam from unknown sites, authenticity wins. Unknown sites sell urgency; legacy regulars buy process. Log in and claim your bonus now only after the APK, the panel, and the surplus check all pass. That triad is the real exclusive reward.</p>
<p style='margin:0 0 14px;color:#2c3e4e'>Share the pirate-cabin banner with friends if you like the art. Share the claim map in the same message. Cool branding without cool process is how stiff regret stories start — and this ship log is written to avoid that ending.</p>
<p style='margin:0 0 18px;text-align:center'>{cta('CLAIM ON LEGACY APP','#0a2540','#7fdbda','#0d7377','8px')}</p>
</section>
<section id='faq-here'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#0d7377'>FAQ</h2>
<p style='margin:0 0 6px;font-weight:800'>Is “is here” the same as last week’s teaser?</p>
<p style='margin:0 0 12px;color:#2c3e4e'>This creative signals the live claim window — always re-check in-app rules.</p>
<p style='margin:0 0 6px;font-weight:800'>Do exclusive rewards guarantee wins?</p>
<p style='margin:0 0 12px;color:#2c3e4e'>No. Promotional value is not a profit promise.</p>
<p style='margin:0 0 6px;font-weight:800'>Safe download?</p>
<p style='margin:0 0 0;color:#2c3e4e'>Only the legacy JAIHO777 APK button in this article.</p>
</section>
</article>"""


# 4 Street editorial / sunny magazine — Chicken Road 3 mega win
def art4():
    return f"""<article style='max-width:960px;margin:0 auto;box-sizing:border-box;padding:0;background:#fafaf8;color:#141414;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.7;overflow:hidden'>
<div style='padding:14px 16px;display:flex;align-items:center;justify-content:space-between;background:#141414'>
<div style='display:flex;align-items:center;gap:10px'><img src='{LOGO}' alt='JAIHO777 logo' title='JAIHO777' style='height:30px;width:auto;display:block'><span style='color:#f5d547;font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase'>JAIHO777 LEGACY · STREET EDIT</span></div>
<span style='background:#f5d547;color:#141414;padding:7px 12px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>MEMBER SPOTLIGHT</span>
</div>
<div style='display:flex;flex-wrap:wrap'>
<div style='flex:1 1 300px;padding:clamp(20px,4vw,36px);box-sizing:border-box'>
<p style='margin:0 0 8px;font-size:12px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#c45c00'>MEMBER SUCCESS · CHICKEN ROAD 3</p>
<h1 style='margin:0 0 12px;font-size:clamp(28px,5vw,42px);line-height:1.1;color:#141414'>Chicken Road 3 on JAIHO777 Hits a ₹1.74 Lakh Member Spotlight — Steal Timing, Not the Fantasy</h1>
<p style='margin:0 0 16px;color:#3a3a3a'>UID 364***462 made the sunny street reel. Clap for the shot. Keep your own stake plan boring and written.</p>
<p style='margin:0'>{cta('PLAY ON LEGACY APK','#f5d547','#141414','#8a7400','999px')}</p>
</div>
<figure style='flex:1 1 300px;margin:0;padding:0;background:#eceae4'>
<img src='{IMG[3]}' alt='JAIHO777 Chicken Road 3 mega win showcase Rs 174500 with multipliers and member UID' title='Chicken Road 3 mega win' style='width:100%;height:auto;display:block;margin:0'>
<figcaption style='margin:0;padding:10px 14px;font-size:12px;color:#5a5a5a;background:#eceae4'>Spotlight: Chicken Road 3 · ₹174,500 · UID 364***462 — highlight reel, not a syllabus.</figcaption>
</figure>
</div>
<nav style='display:flex;flex-wrap:wrap;gap:12px;justify-content:center;padding:12px;background:#eceae4;border-top:1px solid #ddd9d0;border-bottom:1px solid #ddd9d0'>
<a href='#reel' style='color:#c45c00;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>THE REEL</a>
<a href='#lessons' style='color:#c45c00;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>LESSONS</a>
<a href='#faq-cr' style='color:#c45c00;text-decoration:none;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase'>FAQ</a>
</nav>
<div style='padding:clamp(18px,3vw,32px) 16px 36px'>
<section id='reel'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#141414'>What this street-sunny showcase is selling</h2>
<p style='margin:0 0 14px;color:#333'>Chicken Road 3 banners lean into playful chaos: cartoon chicken, coffee-street backdrop, multiplier badges, ₹174,500 flex. As member coverage for legacy JAIHO777 audiences, it is social proof with sparkle. As personal strategy, multipliers like 12.6x or 50.0x cut both ways — they are not a homework target for your next UPI top-up in Delhi or Bangalore.</p>
<p style='margin:0 0 14px;color:#333'>Hinglish: “Reel dekh ke plan mat uda dena.” Progressive loyal players celebrate a UID without treating it like a syllabus. Showcase culture should teach timing and exit discipline, not peer pressure.</p>
</section>
<section id='lessons'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#141414'>Lessons worth stealing from the reel</h2>
<ul style='margin:0 0 16px;padding:0;list-style:none'>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:16px;border:1px solid #e5e1d8'><strong>Official street only</strong> — legacy APK from this page, never random mirrors.</li>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:16px;border:1px solid #e5e1d8'><strong>Pre-write stakes</strong> — decide bet size before the chicken chaos starts.</li>
<li style='margin:0 0 10px;padding:14px;background:#ffffff;border-radius:16px;border:1px solid #e5e1d8'><strong>Hard stop time</strong> — end even if the next multiplier badge looks loud.</li>
<li style='margin:0 0 0;padding:14px;background:#ffffff;border-radius:16px;border:1px solid #e5e1d8'><strong>Surplus only</strong> — Paytm / PhonePe / Google Pay from entertainment money.</li>
</ul>
<p style='margin:0 0 14px;color:#333'>Confirm Chicken Road 3 is live in your lobby after install. Sample on the smallest comfortable stake. If friends demand you match ₹174,500, mute the noise. KYC still gates withdrawals after a loud night. 24/7 support helps with account issues; it cannot reverse a late decision you regret.</p>
<p style='margin:0 0 14px;color:#333'>Street-editorial truth: sunny creatives travel fast on WhatsApp. Reply with a stake plan, not only applause. That tiny social push keeps member spotlights inspiring instead of contagious in the worst way for hostel and flat group chats across India.</p>
<p style='margin:0 0 14px;color:#333'>If the session still feels restless after a short sample, switch titles or close the app. Changing games is a valid cool-down. Raising stakes after a loss is not. That distinction keeps Chicken Road 3 energy playful instead of punishing.</p>
<p style='margin:0 0 14px;color:#333'>Final frame: JAIHO777 can keep publishing sunny mega-win posters. You keep publishing your own stop time. That is the only credit roll that matters after the chicken leaves the screen.</p>
<p style='margin:0 0 14px;color:#333'>Hardware note for mature players: charged phone, muted banking notifications you do not need mid-round, stable data. Split attention is how late exits happen. Let the street cafe art stay visual; keep thumb rules boring. Boring rules are how spotlight nights stay affordable.</p>
<p style='margin:0 0 14px;color:#333'>Trend note for loyal Indian earning-game fans: playful chicken reels travel faster than caution notes. When a friend in Ahmedabad or Kochi forwards the ₹174,500 frame, reply with a stake plan. That tiny social push keeps showcase culture from becoming peer pressure dressed as entertainment.</p>
<p style='margin:0 0 14px;color:#333'>Close like a street editor: publish the win story once, then publish your stop. JAIHO777 can host Chicken Road 3. You host the boundaries that keep real cash nights adult and returnable.</p>
<p style='margin:0 0 18px'>{cta('OPEN CHICKEN ROAD PATH','#141414','#f5d547','#f5d547','999px')}</p>
</section>
<section id='faq-cr'>
<h2 style='margin:0 0 10px;font-size:clamp(22px,3vw,28px);color:#141414'>FAQ</h2>
<div style='display:flex;flex-direction:column;gap:10px'>
<div style='padding:12px 14px;background:#ffffff;border-radius:12px;border:1px solid #e5e1d8'><strong style='display:block;margin:0 0 4px'>Can I aim for the same ₹174,500?</strong><span style='color:#555'>No. This is a showcase, not a target sheet.</span></div>
<div style='padding:12px 14px;background:#ffffff;border-radius:12px;border:1px solid #e5e1d8'><strong style='display:block;margin:0 0 4px'>Is Chicken Road 3 always live?</strong><span style='color:#555'>Check the lobby after installing the legacy APK.</span></div>
<div style='padding:12px 14px;background:#ffffff;border-radius:12px;border:1px solid #e5e1d8'><strong style='display:block;margin:0 0 4px'>Safe download?</strong><span style='color:#555'>Only the JAIHO777 legacy APK button here.</span></div>
</div>
</section>
</div>
</article>"""


META = [
    {
        'file': '01-telegram-secret-codes.html',
        'title': 'Don’t Miss Today’s Secret Code on JAIHO777 — Fresh Promo Codes Daily on Telegram, Without Getting Played',
        'keywords': 'Telegram promo codes India, daily secret code JAIHO777, follow unlock rewards, legacy player verify checklist',
        'description': 'How JAIHO777 legacy players handle today’s secret code—fresh Telegram promos, verify-first habits, surplus-only play.',
        'fn': art1,
    },
    {
        'file': '02-weekly-bonus-tomorrow.html',
        'title': 'Your Weekly Bonus Arrives Tomorrow on JAIHO777 — Exclusive Rewards Are Coming, So Get Ready Without Going Reckless',
        'keywords': 'weekly bonus countdown, exclusive rewards tomorrow, get ready to claim, loyal cash game prep India',
        'description': 'Editorial prep for JAIHO777’s weekly bonus arriving tomorrow—exclusive rewards energy with a mature stake plan.',
        'fn': art2,
    },
    {
        'file': '03-weekly-bonus-here.html',
        'title': 'Your Weekly Bonus Is Here on JAIHO777 — Exclusive Rewards Available Today, If You Claim Like a Captain Not a Looter',
        'keywords': 'weekly bonus is here, exclusive rewards today, log in and claim, weekly vs midweek chaos',
        'description': 'Live claim-window brief for JAIHO777 weekly bonus—compare calm captain claims vs midweek FOMO top-ups.',
        'fn': art3,
    },
    {
        'file': '04-chicken-road-spotlight.html',
        'title': 'Chicken Road 3 on JAIHO777 Hits a ₹1.74 Lakh Member Spotlight — Steal Timing, Not the Fantasy',
        'keywords': 'Chicken Road 3 mega win, member spotlight India, ₹174500 showcase, multiplier discipline',
        'description': 'Chicken Road 3 ₹174,500 member spotlight on JAIHO777 decoded—celebrate the reel, write stakes, hard-stop on time.',
        'fn': art4,
    },
]


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    PUB.mkdir(parents=True, exist_ok=True)
    (PUB / 'per-artikel').mkdir(parents=True, exist_ok=True)
    all_parts = [
        'JAIHO777 BATCH 10 — PROSAFEBET (SITUS LAMA / LEGACY)',
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
        '# Batch 10 Legacy — Prosafebet inline articles\n\n'
        'Copy-paste: `../../publish/batch-10-legacy/`\n\n'
        '4 artikel. Full inline CSS. APK situs lama.\n',
        encoding='utf-8',
    )
    (PUB / 'README.md').write_text(
        '# Batch 10 Legacy Copy Pack\n\n'
        '- `COPY-PASTE-SEMUA-ARTIKEL.txt`\n'
        '- `per-artikel/artikel-01.txt` ... `artikel-04.txt`\n',
        encoding='utf-8',
    )
    print('DONE')


if __name__ == '__main__':
    main()
