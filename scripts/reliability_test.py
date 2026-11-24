"""Time loc.gov search + page-metadata + IIIF image calls for a sample of 1927 dates. Writes ../data/reliability.json"""
import json, time, urllib.request, datetime as D, random, os
UA = {'User-Agent': 'OmegaGames-100YearsAgoToday/0.1'}
def timed(url, raw=False):
    t = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
            b = r.read(); ok = r.status == 200
            if not raw: json.loads(b)
        return {'ok': ok, 'secs': round(time.time() - t, 1)}
    except Exception as e:
        return {'ok': False, 'secs': round(time.time() - t, 1), 'err': str(e)[:120]}
random.seed(7)
dates = sorted(D.date(1927, 1, 1) + D.timedelta(random.randrange(365)) for _ in range(10))
out = []
for d in dates:
    s = timed(f'https://www.loc.gov/collections/chronicling-america/?dates={d}/{d}&fa=online-format:image&fo=json&c=160&at=results,pagination')
    p = timed(f'https://www.loc.gov/resource/sn83045462/{d}/ed-1/?sp=1&fo=json')
    out.append({'date': str(d), 'search': s, 'page_meta': p}); print(out[-1], flush=True)
json.dump({'run_at': time.strftime('%Y-%m-%d %H:%M %Z'), 'results': out}, open(os.path.join(os.path.dirname(__file__), '..', 'data', 'reliability.json'), 'w'), indent=1)
