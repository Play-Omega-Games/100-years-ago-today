"""Zoom into part of a page for visual checking. Usage: zoom.py <date>_<lccn> x y w h (percent) out.jpg"""
import json, sys, urllib.request, os
m = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'data', 'pages', sys.argv[1] + '.json')))
x, y, w, h = sys.argv[2:6]
url = f"{m['iiif_base']}/pct:{x},{y},{w},{h}/pct:50/0/default.jpg"
open(sys.argv[6], 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'OmegaGames'}), timeout=90).read())
print(url)
