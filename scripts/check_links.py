"""GET every URL in the plan (LOC pages, images, fact sources, standards sources, Next shelf links) and the rights page. Writes data/link-report.json"""
import json, os, time, urllib.request, concurrent.futures
# Try a browser User-Agent first. Some government and university CDNs block browser UAs that come
# from a script (TLS fingerprint mismatch) but accept others, so fall back through a short list.
UAS = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
       'Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0',
       'Mozilla/5.0 (compatible; OmegaGamesLinkCheck/1.0; +https://github.com/Play-Omega-Games/100-years-ago-today)']
BASE = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.9', 'Range': 'bytes=0-2047'}
# Live pages that refuse every scripted request (checked by hand in a browser). Reported, not counted as broken.
KNOWN_BOT_BLOCKED = {'www.usmint.gov'}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plan = json.load(open(f'{ROOT}/plans/front-pages.json'))
urls = {plan['rights']['source']} | {p['url'] for p in plan['next_shelf']['picks']} | {c['source'] for c in plan['standards']['codes'].values()}
for d in plan['days'] + plan['alternates']:
    for k in ('item_url', 'page_url', 'image_url', 'thumb_url'):
        if d.get(k): urls.add(d[k])
    t = d.get('then_vs_now') or {}
    for k in ('url', 'url2'):
        if t.get(k): urls.add(t[k])
def check(u):
    code, err, used = None, None, None
    for i in range(2):
        for ua in UAS:
            try:
                req = urllib.request.Request(u, headers={'User-Agent': ua, **BASE})
                with urllib.request.urlopen(req, timeout=60) as r: code, used = r.status, ua.split(' ')[-1][:30]
                return u, {'status': code, 'err': None, 'ua': used}
            except urllib.error.HTTPError as e: code, err = e.code, str(e)
            except Exception as e: code, err = None, str(e)[:100]
        time.sleep(3)
    return u, {'status': code, 'err': err, 'ua': None}
res = {}
with concurrent.futures.ThreadPoolExecutor(6) as ex:
    for u, r in ex.map(check, sorted(urls)):
        res[u] = r; print(r['status'], r['ua'] or '-', u, flush=True)
bad = {u: r for u, r in res.items() if r['status'] not in (200, 206) and u.split('/')[2] not in KNOWN_BOT_BLOCKED}
blocked = {u: r for u, r in res.items() if r['status'] not in (200, 206) and u.split('/')[2] in KNOWN_BOT_BLOCKED}
json.dump({'checked': time.strftime('%Y-%m-%d %H:%M %Z'), 'total': len(res), 'bad': bad, 'known_bot_blocked': blocked, 'all': res}, open((os.makedirs(f'{ROOT}/data', exist_ok=True), f'{ROOT}/data/link-report.json')[1], 'w'), indent=1)
print(f'\n{len(res)} urls, {len(res) - len(bad) - len(blocked)} OK, {len(bad)} not OK, {len(blocked)} known bot-blocked: {sorted(blocked)}')
raise SystemExit(1 if bad else 0)
