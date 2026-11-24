"""Merge curated content (batch 1 + batch 2) with fetched LOC page metadata into plans/front-pages.json.
Needs data/pages/<date>_<lccn>.json for every entry (made by fetch_page.py)."""
import json, os, datetime as D, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from curated_content import PAGES, ALTERNATES, LOC_RIGHTS_URL
from curated_batch2 import PAGES2, ALTERNATES2
import standards

NEXT_SHELF = {
 'title': 'Ready for a longer read? Next on the Scholar Shelf:',
 'picks': [{'name': "Founders' Reading Plan", 'url': 'https://x.ai/bot/OiJ2yft0AxrfrCdRAgFYu'},
           {'name': 'Great Books: Reading Paths', 'url': 'https://x.ai/bot/k232Uq3GOPgOdh63JWIWp'}],
 'family_line': 'Grown-ups who finish a path can read along with a younger shelf too.',
 'rule': 'Name and link only. Never add or install another bot.'}

def meta(p):
    m = json.load(open(f"{ROOT}/data/pages/{p['date']}_{p['lccn']}.json"))
    base = m['iiif_base']
    return {'item_url': m['item_url'], 'page_url': m['page_url'],
            'image_url': base + '/full/pct:25/0/default.jpg', 'thumb_url': base + '/full/pct:6.25/0/default.jpg',
            'ocr_text_url': m['ocr_text_url'], 'loc_title': m['title'],
            'rights_ok': bool(m['rights']) and 'more than 95 years ago are in the public domain' in m['rights'][0]}

def entry(p, main):
    d = D.date.fromisoformat(p['date'])
    e = {'show_on': d.strftime('%m-%d'), 'date': p['date'], 'weekday': d.strftime('%A'),
         'paper': p['paper'], 'city': p['city'], 'state': p['state'], 'lccn': p['lccn'], **meta(p),
         'page_type': p.get('page_type', 'news'), 'family': p['family'], 'family_note': p['family_note'], 'headlines': p['headlines'], 'spots': p['spots'],
         'then_vs_now': p['then_vs_now'], 'question': p['question'],
         'verified': {'checked_against_image': True, 'checked_on': '2026-11-24'}}
    if main:
        e['standards'] = standards.tags_for(p)
    return e

days = sorted(PAGES + PAGES2, key=lambda p: p['date'])
alts = sorted(ALTERNATES + ALTERNATES2, key=lambda p: (p['date'], p['lccn']))
plan = {'name': '100 Years Ago Today', 'version': 2, 'built': '2026-11-24',
        'repo': 'https://github.com/Play-Omega-Games/100-years-ago-today',
        'covers': {'first': days[0]['date'], 'last': days[-1]['date'],
                   'note': 'Curated in monthly batches. Days past the last date use scripts/live_lookup.py until the next batch is published.'},
        'rights': {'statement': 'The Library of Congress believes that the newspapers in Chronicling America are in the public domain or have no known copyright restrictions. Newspapers published in the United States more than 95 years ago are in the public domain in their entirety.',
                   'source': LOC_RIGHTS_URL},
        'family_mode': {'ages': '8 and up',
                        'preview_note': 'Old papers report crime and disasters like papers do today. Please preview each page first: open the full page link before you share it.'},
        'family_levels': {'ok': 'Nothing a parent needs to explain in the big headlines or photos.',
                          'care': 'A headline or item is about crime, death, disaster or scandal, told without gore, or the page uses a period term for a group of people in small print. Family mode stays on the spots and adds a parent note naming what to skip.',
                          'no': 'Graphic violence, suicide, lynching, cannibalism, slurs, or disaster photos with bodies. Never shown in family mode.'},
        'standards': {'wording': 'supports practice toward',
                      'note': 'Supports practice toward these standards. Not a full curriculum and not accredited.',
                      'codes': {k: {**v, 'verified': standards.VERIFIED} for k, v in standards.CODES.items()},
                      'activities': standards.ACTIVITY},
        'next_shelf': NEXT_SHELF,
        'days': [entry(p, True) for p in days], 'alternates': [entry(p, False) for p in alts]}
os.makedirs(f'{ROOT}/plans', exist_ok=True)
json.dump(plan, open(f'{ROOT}/plans/front-pages.json', 'w'), indent=1, ensure_ascii=False)
json.dump({'wording': 'supports practice toward', 'verified': standards.VERIFIED, 'codes': standards.CODES, 'activities': standards.ACTIVITY},
          open(f'{ROOT}/standards.json', 'w'), indent=1, ensure_ascii=False)
print('days', len(plan['days']), 'alternates', len(plan['alternates']), plan['covers']['first'], plan['covers']['last'])
