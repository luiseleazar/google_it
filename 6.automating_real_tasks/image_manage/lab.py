from PIL import Image
import glob
import shutil
import os

def change_images(file):
    im = Image.open(file)
    new_name = file + ".jpg"
    new_im = im.rotate(90).resize((128,128)).save(new_name)

for file in glob.glob("*48dp"):
    change_images(file)

for file in glob.glob("*jpg"):
    dest = "/opt/icons/"
    shutil.move(file, dest)


