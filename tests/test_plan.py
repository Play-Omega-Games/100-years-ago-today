import json, os, re, datetime as D, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
plan = json.load(open(f'{ROOT}/plans/front-pages.json'))
fails = []
def check(name, cond):
    print(('PASS ' if cond else 'FAIL ') + name); cond or fails.append(name)
days, alts = plan['days'], plan['alternates']
dates = [D.date.fromisoformat(d['date']) for d in days]
check('45 days, Nov 24, 1926 to Jan 7, 1927', len(days) == 45 and dates[0] == D.date(1926, 11, 24) and dates[-1] == D.date(1927, 1, 7))
check('consecutive dates, no gaps or repeats', all((b - a).days == 1 for a, b in zip(dates, dates[1:])))
check('covers block matches days', plan['covers']['first'] == days[0]['date'] and plan['covers']['last'] == days[-1]['date'])
check('show_on and weekday match date', all(d['show_on'] == d['date'][5:] and d['weekday'] == D.date.fromisoformat(d['date']).strftime('%A') for d in days))
check('every page is 95+ years old as of 2026', all(dt.year <= 1931 for dt in dates))
req = ['paper', 'city', 'state', 'lccn', 'item_url', 'page_url', 'image_url', 'thumb_url', 'family', 'headlines', 'spots', 'then_vs_now', 'question', 'standards']
check('required fields on every day', all(all(d.get(k) for k in req) for d in days))
check('no pdf fields', all('pdf' not in d and 'pdf_url' not in d for d in days + alts))
check('3 to 5 spots each, each with a where', all(3 <= len(d['spots']) <= 5 and all(s['spot'] and s['where'] for s in d['spots']) for d in days))
check('at least 3 family-safe headlines each (1 for full-page pictures)', all(sum(h['family'] for h in d['headlines']) >= (1 if d['page_type'] == 'picture' else 3) for d in days))
check('picture pages are rare (at most 1 in 10)', sum(d['page_type'] == 'picture' for d in days) * 10 <= len(days))
check('family level valid; care has a note', all(d['family'] in ('ok', 'care') and (d['family'] != 'care' or d['family_note']) for d in days))
check('family mode is 8 and up with a preview note', plan['family_mode']['ages'] == '8 and up' and 'preview' in plan['family_mode']['preview_note'])
t = [d['then_vs_now'] for d in days]
check('every then-vs-now has kind, text, source and https url', all(x['kind'] in ('change', 'continuity', 'what_next') and x['text'] and x['source'] and x['url'].startswith('https://') for x in t))
check('no Wikipedia sources anywhere', 'wikipedia.org' not in json.dumps(plan))
import standards as S
tags = [g for d in days for g in d['standards']]
check('every standards tag is a verified code with the right wording', all(g['code'] in S.CODES and g['wording'] == 'supports practice toward' and g['verified'] for g in tags))
check('plan standards list equals verified codes', set(plan['standards']['codes']) == set(S.CODES))
check('every day has the who-was-it-for tag', all(any(g['activity'] == 'who_was_it_for' for g in d['standards']) for d in days))
ns = plan['next_shelf']
check('next shelf has the two Scholar Shelf picks', [p['url'] for p in ns['picks']] == ['https://x.ai/bot/OiJ2yft0AxrfrCdRAgFYu', 'https://x.ai/bot/k232Uq3GOPgOdh63JWIWp'])
check('images and pages hosted at loc.gov', all(re.match(r'https://(www|tile)\.loc\.gov/', d[k]) for d in days + alts for k in ('item_url', 'page_url', 'image_url', 'thumb_url')))
check('LOC rights statement present on every item', all(d['rights_ok'] for d in days + alts))
check('every page verified against the image', all(d['verified']['checked_against_image'] for d in days + alts))
txt = json.dumps(plan, ensure_ascii=False)
check('no em or en dashes anywhere in the plan', '\u2014' not in txt and '\u2013' not in txt)
check('alternates have a level and a note, and no fact or spots when "no"', all(a['family'] in ('no', 'care') and a['family_note'] and (a['family'] != 'no' or (not a['spots'] and a['then_vs_now'] is None)) for a in alts))
check('alternate dates fall inside the plan', all(days[0]['date'] <= a['date'] <= days[-1]['date'] for a in alts))
skills = [os.path.join(ROOT, 'skills', s, 'SKILL.md') for s in ('100-years-ago-today-getting-started', '100-years-ago-today-daily')]
if all(os.path.exists(p) for p in skills):
    st = ''.join(open(p).read() for p in skills)
    check('skills have no em dashes', '\u2014' not in st)
    check('skills load from the Play-Omega-Games repo', 'raw.githubusercontent.com/Play-Omega-Games/100-years-ago-today/main/plans/front-pages.json' in st)
    check('skills say 8 and up, preview first and "when available"', '8 and up' in st and 'preview each page first' in st and 'when available' in st)
print(f'\n{len(fails)} failed' if fails else '\nall passed'); sys.exit(1 if fails else 0)
