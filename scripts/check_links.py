"""GET every URL in the plan (LOC pages, images, fact sources, standards sources, Next shelf links) and the rights page. Writes data/link-report.json"""
import json, os, time, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plan = json.load(open(f'{ROOT}/plans/front-pages.json'))
urls = {plan['rights']['source']} | {p['url'] for p in plan['next_shelf']['picks']} | {c['source'] for c in plan['standards']['codes'].values()}
for d in plan['days'] + plan['alternates']:
    for k in ('item_url', 'page_url', 'image_url', 'thumb_url'):
        if d.get(k): urls.add(d[k])
    t = d.get('then_vs_now') or {}
    for k in ('url', 'url2'):
        if t.get(k): urls.add(t[k])
res = {}
for u in sorted(urls):
    code, err = None, None
    for i in range(3):
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (OmegaGames link check)', 'Range': 'bytes=0-2047'})
            with urllib.request.urlopen(req, timeout=60) as r: code = r.status
            break
        except urllib.error.HTTPError as e: code, err = e.code, str(e)
        except Exception as e: err = str(e)[:100]
        time.sleep(2)
    res[u] = {'status': code, 'err': None if code in (200, 206) else err}
    print(code, u)
bad = {u: r for u, r in res.items() if r['status'] not in (200, 206)}
json.dump({'checked': time.strftime('%Y-%m-%d %H:%M %Z'), 'total': len(res), 'bad': bad, 'all': res}, open((os.makedirs(f'{ROOT}/data', exist_ok=True), f'{ROOT}/data/link-report.json')[1], 'w'), indent=1)
print(f'\n{len(res)} urls, {len(bad)} not OK')
