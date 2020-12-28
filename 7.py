from PIL import Image
img = Image.open("oxygen.png")

row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
ords = [r for r, g, b, a in row[::7] if r == g == b]

"".join(map(chr, ords))

"".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
