from PIL import Image

im = Image.open("python_logo.png")
im.rotate(45).show()
