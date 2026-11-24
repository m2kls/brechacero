// srcset WebP para fotos y portadas propias (las variantes las crea tools/variantes.py en el build).
const RE = /^\/img\/(fotos|covers)\/([^/]+)\.jpg$/;
export function webpSrcset(src: string): string | undefined {
  const m = src.match(RE);
  if (!m) return undefined;
  const base = `/img/${m[1]}/${m[2]}`;
  return `${base}-480.webp 480w, ${base}-800.webp 800w, ${base}-1200.webp 1200w`;
}
