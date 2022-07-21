from PIL import Image

im = Image.open("python_logo.png")
im.rotate(180).resize((640,480)).save("flipped_and_resized.png")