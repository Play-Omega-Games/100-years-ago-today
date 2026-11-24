# 📰 100 Years Ago Today

Part of the Omega Home Library, Scholar Shelf, by Omega Games. A Grok Bot template that brings a real American newspaper front page from exactly 100 years ago, every morning: the day's headlines, things to spot on the page, a then-vs-now fact with its source, a "who was this paper for?" prompt and a question to talk about. Family mode is for ages 8 and up; parents should preview each page first.

All front pages come from the Library of Congress, Chronicling America. The Library of Congress states: "Newspapers published in the United States more than 95 years ago are in the public domain in their entirety." (https://www.loc.gov/collections/chronicling-america/about-this-collection/rights-and-access/)

## What the bot loads
- `plans/front-pages.json`: the curated plan. Raw URL: https://raw.githubusercontent.com/Play-Omega-Games/100-years-ago-today/main/plans/front-pages.json
- `scripts/live_lookup.py`: the fallback for dates past the plan, "My state, when available" and "Another paper". Raw URL: https://raw.githubusercontent.com/Play-Omega-Games/100-years-ago-today/main/scripts/live_lookup.py

## The plan
- 45 consecutive days, Nov 24, 1926 to Jan 7, 1927, published in monthly batches.
- Each day: paper, city, state, Library of Congress page and image links, headlines (each flagged family-safe or not), 3 to 5 things to spot with where they sit, a then-vs-now fact (`kind`: change, continuity or what_next) with a source URL, a question, a family level (`ok` or `care`, with a parent note) and `standards` tags.
- `alternates`: pages checked but kept out of the daily rotation, mostly family level `no`.
- Every headline and spot was read off the page image, not the OCR text.
- `standards.json`: the 6 verified codes (C3 Framework and Common Core ELA). Wording is always "supports practice toward". Not a full curriculum and not accredited.

## Build and check
```
python3 scripts/build_plan.py     # curated_content.py + curated_batch2.py + data/pages/*.json -> plans/front-pages.json, standards.json
python3 tests/test_plan.py        # plan checks
python3 scripts/check_links.py    # GETs every URL in the plan
python3 scripts/live_lookup.py --date 1927-01-08 --state MT
```

## Curating a new batch
1. `python3 scripts/list_issues.py <date> ...` lists digitized issues for each date.
2. `python3 scripts/fetch_page.py <lccn> <date> ...` fetches front-page metadata, a 25% image and OCR; `python3 scripts/crops.py` makes top and bottom halves.
3. Look at the halves; zoom with `python3 scripts/zoom.py <date>_<lccn> x y w h out.jpg`.
4. Rate the family level: `no` for graphic violence, suicide, lynching, cannibalism, slurs or disaster photos with bodies; `care` for crime, death or disaster without gore, or a period term in small print; `ok` otherwise. Small weeklies are usually gentler than big dailies.
5. Find a then-vs-now fact on an official page (.gov, Library of Congress, a university, museum or the organization itself), open it and confirm the wording. No Wikipedia.
6. Add the entry to a `curated_batchN.py`, rebuild, test and check links.

Note: `data/pages/` holds only the metadata JSON in this repo; images and OCR are re-fetched with `fetch_page.py`.

## License
Plan content (`plans/`, `standards.json`, curated text in `scripts/curated_*.py`): CC0 1.0. Code: MIT. See LICENSE. The newspaper pages themselves are public domain, hosted by the Library of Congress.

Questions or ideas? Contact Omega Games at john@playomega.games.
