from PIL import Image

def image_tool():   # ✅ THIS NAME MUST MATCH
    path = input("Enter image path: ")
    key = int(input("Enter key: "))

    img = Image.open(path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save("encrypted.png")
    print("Image encrypted and saved!")
