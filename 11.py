from PIL import Image
img = Image.open("cave.jpg")

res = [[img.getpixel((x, y)) for x in range(img.width)] for y in range(img.height)]
res = [x[(i%2)::2] for i,x in enumerate(res)]

img2 = Image.new(img.mode, (int(img.size[0]/2), int(img.size[1]/2)))
data = img2.load()

for x in range(img2.size[0]):
    for y in range(img2.size[1]):
        p = res[y][x]
        if all([x < 25 for x in p]):
            data[x,y] = (255, 255, 255)
        else:
            data[x,y] = p

img2.show()
