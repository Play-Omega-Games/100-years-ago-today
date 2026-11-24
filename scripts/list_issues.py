"""List digitized newspaper issues in Chronicling America (loc.gov) for a date.
Usage: python3 list_issues.py 1926-11-24 [1926-11-25 ...]  -> writes ../data/issues/<date>.json"""
import json, sys, time, urllib.request, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'issues')
os.makedirs(OUT, exist_ok=True)
def get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'OmegaGames-100YearsAgoToday/0.1'})
            t = time.time()
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r), time.time() - t
        except Exception as e:
            print('  retry', i + 1, e, file=sys.stderr); time.sleep(3 * (i + 1))
    raise SystemExit('failed: ' + url)
for date in sys.argv[1:]:
    url = (f'https://www.loc.gov/collections/chronicling-america/?dates={date}/{date}'
           '&fa=online-format:image&fo=json&c=160&at=results,pagination')
    d, secs = get(url)
    rows = [{'date': x.get('date'), 'title': x.get('title'), 'item': x.get('id'),
             'state': x.get('location_state'), 'language': x.get('language')} for x in d['results']]
    json.dump(rows, open(os.path.join(OUT, f'{date}.json'), 'w'), indent=1)
    print(date, len(rows), f'{secs:.1f}s')
