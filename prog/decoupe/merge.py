from PIL import Image

BLOC_SIZE = 33
ROW_SIZE = 24

merge = Image.new("RGB", (BLOC_SIZE * ROW_SIZE, BLOC_SIZE * ROW_SIZE), "white")

for y in range(ROW_SIZE):
    for x in range(ROW_SIZE):
        idx = (x + 1) + (y * ROW_SIZE)
        img = Image.open(f"./src/{idx}.png")
        merge.paste(img, (x * BLOC_SIZE, y * BLOC_SIZE))
        img.close()

merge.save("merged.png")
