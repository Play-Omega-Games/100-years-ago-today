"""Fallback: find a real front page from exactly 100 years ago on loc.gov when the curated plan
has no entry for a date (or the owner asked for a state the plan doesn't cover).

Usage: python3 live_lookup.py [--date 1926-12-08] [--state CA] [--out /workspace/100-years-ago-today/live]
Prints JSON: candidates (English issues, state matches first) and, for the first one that loads,
the front-page metadata plus a downloaded 25% JPG and its top/bottom halves for visual checking.
The bot must look at the images before writing anything; OCR is only a reading aid."""
import argparse, json, os, sys, time, urllib.request, datetime as D
UA = {'User-Agent': 'OmegaGames-100YearsAgoToday/1.0'}
STATES = {'AL':'alabama','AK':'alaska','AZ':'arizona','AR':'arkansas','CA':'california','CO':'colorado','CT':'connecticut','DE':'delaware','DC':'district of columbia','FL':'florida','GA':'georgia','HI':'hawaii','ID':'idaho','IL':'illinois','IN':'indiana','IA':'iowa','KS':'kansas','KY':'kentucky','LA':'louisiana','ME':'maine','MD':'maryland','MA':'massachusetts','MI':'michigan','MN':'minnesota','MS':'mississippi','MO':'missouri','MT':'montana','NE':'nebraska','NV':'nevada','NH':'new hampshire','NJ':'new jersey','NM':'new mexico','NY':'new york','NC':'north carolina','ND':'north dakota','OH':'ohio','OK':'oklahoma','OR':'oregon','PA':'pennsylvania','RI':'rhode island','SC':'south carolina','SD':'south dakota','TN':'tennessee','TX':'texas','UT':'utah','VT':'vermont','VA':'virginia','WA':'washington','WV':'west virginia','WI':'wisconsin','WY':'wyoming'}
# Dailies that run most days in the 1920s and read well; used to order candidates after the state match.
PREFERRED = ['sn83045462','sn84026749','sn82016181','sn82015313','sn85042243','sn84020657','sn87062169','sn82014519','sn92070146','sn82014248','sn86092280','sn87055779','sn86063730','sn84020064','sn84020645']
def get(url, raw=False, tries=4, timeout=60):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                b = r.read(); return b if raw else json.loads(b)
        except Exception as e:
            print(f'retry {i+1}: {e}', file=sys.stderr); time.sleep(4 * (i + 1))
    return None
ap = argparse.ArgumentParser(); ap.add_argument('--date'); ap.add_argument('--state'); ap.add_argument('--skip', action='append', default=[], help='LCCN to skip (repeatable)'); ap.add_argument('--out', default='/workspace/100-years-ago-today/live')
a = ap.parse_args()
today = D.date.today()
if a.date:
    date = a.date
elif (today.month, today.day) == (2, 29) and (today.year - 100) % 4:
    date = str(D.date(today.year - 100, 2, 28))
else:
    date = str(today.replace(year=today.year - 100))
d = get(f'https://www.loc.gov/collections/chronicling-america/?dates={date}/{date}&fa=online-format:image&fo=json&c=160&at=results')
if not d: print(json.dumps({'ok': False, 'date': date, 'error': 'loc.gov search failed after retries'})); sys.exit(2)
rows = [{'title': x.get('title'), 'lccn': x['id'].split('/item/')[1].split('/')[0], 'states': x.get('location_state') or [], 'language': x.get('language') or []} for x in d.get('results', [])]
rows = [r for r in rows if 'english' in r['language'] and r['lccn'] not in a.skip]
want = STATES.get((a.state or '').upper())
rows.sort(key=lambda r: (0 if want and want in r['states'] else 1, PREFERRED.index(r['lccn']) if r['lccn'] in PREFERRED else 99))
os.makedirs(a.out, exist_ok=True)
for r in rows[:6]:
    m = get(f"https://www.loc.gov/resource/{r['lccn']}/{date}/ed-1/?sp=1&fo=json")
    if not m: continue
    jp2 = next((f for f in m.get('page', []) if f.get('mimetype') == 'image/jp2'), None)
    if not jp2: continue
    base = jp2['info'].rsplit('/info.json', 1)[0]
    img = get(base + '/full/pct:25/0/default.jpg', raw=True, timeout=90)
    if not img: continue
    stem = f"{a.out}/{date}_{r['lccn']}"; open(stem + '.jpg', 'wb').write(img)
    try:
        from PIL import Image
        im = Image.open(stem + '.jpg'); w, h = im.size
        im.crop((0, 0, w, h // 2)).save(stem + '_top.jpg'); im.crop((0, h // 2, w, h)).save(stem + '_bot.jpg')
    except Exception as e:
        print('PIL crop skipped:', e, file=sys.stderr)
    rights = (m['item'].get('rights') or [''])[0]
    print(json.dumps({'ok': True, 'date': date, 'paper': r['title'], 'lccn': r['lccn'], 'state_match': bool(want and want in r['states']),
        'item_url': f"https://www.loc.gov/item/{r['lccn']}/{date}/ed-1/", 'page_url': f"https://www.loc.gov/resource/{r['lccn']}/{date}/ed-1/?sp=1",
        'image_url': base + '/full/pct:25/0/default.jpg', 'iiif_base': base, 'ocr_text_url': m['resource'].get('fulltext_file'),
        'rights_95_year_line': 'more than 95 years ago are in the public domain' in rights,
        'local_images': [stem + '.jpg', stem + '_top.jpg', stem + '_bot.jpg'], 'other_candidates': [x['title'] for x in rows[:12] if x is not r]}, indent=1))
    sys.exit(0)
print(json.dumps({'ok': False, 'date': date, 'error': 'no candidate page loaded', 'candidates': [x['title'] for x in rows[:12]]})); sys.exit(3)
