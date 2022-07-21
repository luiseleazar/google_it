from PIL import Image
im = Image.open("python_logo.png")
new_im = im.resize((640,480))
new_im.save("python_logo_resized.png")