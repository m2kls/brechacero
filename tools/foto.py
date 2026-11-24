#!/usr/bin/env python3
"""Fotos reales con licencia libre desde Wikimedia Commons.

Buscar candidatas (y guardar una hoja de contacto para mirarlas):
    python3 -I tools/foto.py buscar "J. Edgar Hoover Building" --hoja /tmp/hoja.jpg
Descargar la elegida (n.º de la lista) como portada de un artículo:
    python3 -I tools/foto.py bajar "J. Edgar Hoover Building" 0 mi-slug
Imprime las líneas image / imageAlt / imageCredit para el frontmatter.
Solo acepta licencias que permiten uso comercial y modificación (CC0, PD, CC BY, CC BY-SA).
"""
import io, json, re, sys, time, html, urllib.parse, urllib.request
from pathlib import Path

UA = {"User-Agent": "BrechaCeroBot/1.0 (https://brechacero.pages.dev)"}
ROOT = Path(__file__).resolve().parent.parent

def get(url):
    for i in range(6):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(int(e.headers.get("retry-after", "30")) + 5); continue
            raise
    raise RuntimeError("Wikimedia sigue limitando peticiones; espera un minuto")

def thumb(url, w):
    url = url.split("?")[0]
    m = re.match(r"https://upload.wikimedia.org/wikipedia/commons/(\w)/(\w\w)/(.+)$", url)
    return f"https://upload.wikimedia.org/wikipedia/commons/thumb/{m[1]}/{m[2]}/{m[3]}/{w}px-{m[3]}"

def buscar(q, n=8):
    u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "format": "json", "generator": "search", "gsrnamespace": 6,
        "gsrsearch": q + " filetype:bitmap", "gsrlimit": 25, "prop": "imageinfo",
        "iiprop": "url|size|extmetadata"})
    data = json.loads(get(u))
    out = []
    for p in sorted(data.get("query", {}).get("pages", {}).values(), key=lambda p: p["index"]):
        ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
        lic = m.get("LicenseShortName", {}).get("value", "")
        if ii["width"] < 1300 or ii["width"] < ii["height"] * 1.2: continue
        if not re.search(r"^(CC0|CC BY(-SA)? [\d.]+|Public domain|PD)", lic, re.I): continue
        if re.search(r"NC|ND", lic): continue
        artist = re.sub(r"\s+", " ", re.sub("<[^>]+>", "", html.unescape(m.get("Artist", {}).get("value", "")))).strip() or "Autor desconocido"
        desc = re.sub("<[^>]+>", "", html.unescape(m.get("ImageDescription", {}).get("value", ""))).strip()
        out.append({"title": p["title"], "url": ii["url"].split("?")[0], "page": ii["descriptionurl"],
                    "w": ii["width"], "h": ii["height"], "license": lic, "artist": artist[:80], "desc": desc[:160]})
        if len(out) >= n: break
    return out

def hoja(cands, path):
    from PIL import Image, ImageDraw
    W, H = 360, 230
    sheet = Image.new("RGB", (W * 4, (H + 22) * 2), "white"); d = ImageDraw.Draw(sheet)
    for i, c in enumerate(cands[:8]):
        time.sleep(1.5)
        im = Image.open(io.BytesIO(get(thumb(c["url"], 500)))).convert("RGB"); im.thumbnail((W, H))
        x, y = (i % 4) * W, (i // 4) * (H + 22); sheet.paste(im, (x, y))
        d.text((x + 4, y + H + 5), f"{i} {c['license']} {c['title'][5:42]}", fill="black")
    sheet.save(path, quality=80)

def bajar(c, slug):
    from PIL import Image
    im = Image.open(io.BytesIO(get(thumb(c["url"], 1280)))).convert("RGB")
    w, h = im.size; tw, th = w, int(w * 2 / 3)
    if th > h: th = h; tw = int(h * 3 / 2)
    l, t = (w - tw) // 2, (h - th) // 2
    im = im.crop((l, t, l + tw, t + th)).resize((1500, 1000), Image.LANCZOS)
    dest = ROOT / "public" / "img" / "fotos" / f"{slug}.jpg"
    im.save(dest, quality=82, optimize=True, progressive=True)
    lic = c["license"].replace("Public domain", "dominio público")
    print(f'image: "/img/fotos/{slug}.jpg"')
    print(f'imageCredit: "Foto: {c["artist"]} / Wikimedia Commons ({lic})"')
    print(f'imageCreditUrl: "{c["page"]}"')

def info(file_title):
    """Datos de un archivo concreto de Commons ("File:Nombre.jpg")."""
    u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "format": "json", "titles": file_title, "prop": "imageinfo",
        "iiprop": "url|size|extmetadata"})
    p = next(iter(json.loads(get(u))["query"]["pages"].values()))
    ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
    lic = m.get("LicenseShortName", {}).get("value", "")
    if re.search(r"NC|ND|fair", lic, re.I) or not re.search(r"^(CC0|CC BY|Public domain|PD)", lic, re.I):
        raise ValueError(f"{file_title}: licencia no válida ({lic})")
    artist = re.sub(r"\s+", " ", re.sub("<[^>]+>", "", html.unescape(m.get("Artist", {}).get("value", "")))).strip() or "Autor desconocido"
    return {"title": p["title"], "url": ii["url"].split("?")[0], "page": ii["descriptionurl"], "license": lic, "artist": artist[:80].replace('"', "'")}

def ci():
    """Usado por GitHub Actions antes de compilar: para cada artículo con `photo: "File:..."`
    descarga la foto (si no está en caché) y añade image / imageCredit / imageCreditUrl."""
    cache = ROOT / "public" / "img" / "fotos"; cache.mkdir(parents=True, exist_ok=True)
    meta_path = cache / "creditos.json"
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    for md in sorted((ROOT / "src" / "content" / "articulos").glob("*.md")):
        txt = md.read_text(); fm = txt.split("---", 2)[1]
        m = re.search(r'^photo:\s*"?([^"\n]+)"?\s*$', fm, re.M)
        if not m or re.search(r"^image:", fm, re.M): continue
        slug, ft = md.stem, m[1].strip()
        try:
            if meta.get(slug, {}).get("file") != ft or not (cache / f"{slug}.jpg").exists():
                c = info(ft); bajar(c, slug)
                meta[slug] = {"file": ft, "credit": f'Foto: {c["artist"]} / Wikimedia Commons ({c["license"].replace("Public domain", "dominio público")})', "page": c["page"]}
                meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
                time.sleep(2)
        except Exception as e:
            print(f"AVISO {slug}: {e} (se usa la portada ilustrada)"); continue
        add = f'image: "/img/fotos/{slug}.jpg"\nimageCredit: "{meta[slug]["credit"]}"\nimageCreditUrl: "{meta[slug]["page"]}"\n'
        fm2 = re.sub(r"^imageCredit(Url)?:.*\n", "", fm, flags=re.M)
        md.write_text(txt.replace(fm, fm2.rstrip("\n") + "\n" + add, 1))
        print("foto ok", slug)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "ci":
        ci(); sys.exit(0)
    q = sys.argv[2]
    cands = buscar(q)
    if cmd == "buscar":
        for i, c in enumerate(cands):
            print(i, c["license"], f'{c["w"]}x{c["h"]}', c["title"], "|", c["artist"], "|", c["desc"][:90])
        if "--hoja" in sys.argv: hoja(cands, sys.argv[sys.argv.index("--hoja") + 1])
    elif cmd == "bajar":
        bajar(cands[int(sys.argv[3])], sys.argv[4])
