"""Genera versiones WebP ligeras (480, 800 y 1200 px) de las fotos y portadas ya copiadas a dist/.
Se ejecuta en cada build, justo después de `astro build`. Las plantillas las piden con srcset."""
import sys
from pathlib import Path
from PIL import Image

ANCHOS = (480, 800, 1200)
total = 0
for carpeta in ('dist/img/fotos', 'dist/img/covers'):
    for jpg in sorted(Path(carpeta).glob('*.jpg')):
        with Image.open(jpg) as im:
            im = im.convert('RGB')
            for w in ANCHOS:
                out = jpg.with_name(f'{jpg.stem}-{w}.webp')
                h = round(im.height * w / im.width)
                im.resize((w, h), Image.LANCZOS).save(out, 'WEBP', quality=74, method=5)
                total += 1
print(f'variantes WebP: {total}', file=sys.stderr)
