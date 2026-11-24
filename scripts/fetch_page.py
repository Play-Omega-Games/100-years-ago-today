"""Fetch front page (sp=1) metadata, a readable JPG and OCR text for one issue.
Usage: python3 fetch_page.py <lccn> <date> [<lccn> <date> ...]
Writes ../data/pages/<date>_<lccn>.json, .jpg (25%), .txt (OCR)."""
import json, sys, time, urllib.request, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'pages'); os.makedirs(OUT, exist_ok=True)
UA = {'User-Agent': 'OmegaGames-100YearsAgoToday/0.1'}
def get(url, tries=4, raw=False):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                b = r.read(); return b if raw else json.loads(b)
        except Exception as e:
            print('  retry', i + 1, url[:80], e, file=sys.stderr); time.sleep(3 * (i + 1))
    return None
args = sys.argv[1:]
for lccn, date in zip(args[::2], args[1::2]):
    t = time.time()
    res = f'https://www.loc.gov/resource/{lccn}/{date}/ed-1/'
    d = get(res + '?sp=1&fo=json')
    if not d: print(date, lccn, 'FAILED meta'); continue
    files = d['page']
    jp2 = next(f for f in files if f.get('mimetype') == 'image/jp2')
    iiif = jp2['info'].rsplit('/info.json', 1)[0]
    pdf = next((f['url'] for f in files if f.get('mimetype') == 'application/pdf'), None)
    txt_url = d['resource'].get('fulltext_file')
    it = d['item']
    meta = {'date': date, 'lccn': lccn, 'title': it.get('title'), 'newspaper': (it.get('newspaper_title') or [None])[0],
            'location': it.get('location'), 'item_url': f'https://www.loc.gov/item/{lccn}/{date}/ed-1/',
            'page_url': res + '?sp=1', 'iiif_base': iiif, 'width': jp2.get('width'), 'height': jp2.get('height'),
            'image_jpg': iiif + '/full/pct:25/0/default.jpg', 'pdf': pdf, 'ocr_text_url': txt_url,
            'rights': it.get('rights'), 'contributor': it.get('contributor_names')}
    json.dump(meta, open(f'{OUT}/{date}_{lccn}.json', 'w'), indent=1)
    img = get(meta['image_jpg'], raw=True)
    if img: open(f'{OUT}/{date}_{lccn}.jpg', 'wb').write(img)
    tx = get(txt_url, raw=True) if txt_url else None
    if tx:
        try: tx = json.loads(tx); tx = next(iter(tx.values())).get('full_text', '') if isinstance(tx, dict) else tx
        except Exception: tx = tx.decode('utf-8', 'replace')
        open(f'{OUT}/{date}_{lccn}.txt', 'w').write(tx if isinstance(tx, str) else str(tx))
    print(date, lccn, meta['newspaper'], 'img', bool(img), 'ocr', bool(tx), f'{time.time()-t:.1f}s')
