import glob, os
from PIL import Image
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'pages')
for f in sorted(glob.glob(D + '/*.jpg')):
    if f.endswith(('_top.jpg', '_bot.jpg')) or os.path.exists(f[:-4] + '_top.jpg'): continue
    im = Image.open(f); w, h = im.size
    im.crop((0, 0, w, h // 2)).save(f[:-4] + '_top.jpg', quality=85); im.crop((0, h // 2, w, h)).save(f[:-4] + '_bot.jpg', quality=85)
    print('cropped', os.path.basename(f))
