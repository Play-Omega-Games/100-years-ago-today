"""Standards tags, following the Omega Home Library method: tag the activity, not the book;
wording is always "supports practice toward"; code text copied from the official documents
(C3 Framework PDF from NCSS; Common Core ELA from California's official CCSS PDF, because
corestandards.org blocks automated reads). Every code below was checked against those texts on 2026-11-24."""
C3 = 'https://www.socialstudies.org/standards/c3'
CCSS = 'https://www.cde.ca.gov/be/st/ss/documents/finalelaccssstandards.pdf'
CODES = {
 'D2.His.2.3-5': {'framework': 'C3', 'band': '3-5', 'text': 'Compare life in specific historical time periods to life today.', 'source': C3},
 'D2.His.2.6-8': {'framework': 'C3', 'band': '6-8', 'text': 'Classify series of historical events and developments as examples of change and/or continuity.', 'source': C3},
 'D2.His.10.3-5': {'framework': 'C3', 'band': '3-5', 'text': 'Compare information provided by different historical sources about the past.', 'source': C3},
 'D2.His.11.3-5': {'framework': 'C3', 'band': '3-5', 'text': 'Infer the intended audience and purpose of a historical source from information within the source itself.', 'source': C3},
 'RI.3.7': {'framework': 'CCSS-ELA', 'band': '3', 'text': 'Use information gained from illustrations (e.g., maps, photographs) and the words in a text to demonstrate understanding of the text (e.g., where, when, why, and how key events occur).', 'source': CCSS},
 'RH.6-8.7': {'framework': 'CCSS-ELA', 'band': '6-8', 'text': 'Integrate visual information (e.g., in charts, graphs, photographs, videos, or maps) with other information in print and digital texts.', 'source': CCSS},
}
ACTIVITY = {'then_vs_now': 'Then vs now fact', 'what_next': 'What happened next, from a later front page',
            'who_was_it_for': '"Who was this paper for?" prompt (price, ads, place names)', 'picture_spots': 'Spots that pair a photo, cartoon or ad with its words'}
VERIFIED = '2026-11-24'
def tag(code, activity):
    c = CODES[code]
    return {'framework': c['framework'], 'code': code, 'band': c['band'], 'activity': activity,
            'wording': 'supports practice toward', 'source': c['source'], 'verified': VERIFIED}
PICTURE_WORDS = ('photo', 'cartoon', 'ad for', 'ad ', 'drawing', 'banner')
def tags_for(entry):
    out = [tag('D2.His.11.3-5', 'who_was_it_for')]
    kind = (entry.get('then_vs_now') or {}).get('kind', 'change')
    if kind == 'what_next':
        out.append(tag('D2.His.10.3-5', 'what_next'))
    elif kind == 'change':
        out += [tag('D2.His.2.3-5', 'then_vs_now'), tag('D2.His.2.6-8', 'then_vs_now')]
    elif kind == 'continuity':
        out.append(tag('D2.His.2.6-8', 'then_vs_now'))
    if any(w in s['spot'].lower() for s in entry['spots'] for w in PICTURE_WORDS):
        out += [tag('RI.3.7', 'picture_spots'), tag('RH.6-8.7', 'picture_spots')]
    return out
