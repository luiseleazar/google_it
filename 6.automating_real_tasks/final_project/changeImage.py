from PIL import Image
import os

def img_changer(img_file):
    """Convert image to RGB,
    resize image to 600x400,
    convert image from TIFF to jpeg"""
    img = Image.open(img_file)
    img = img.convert('RGB').resize((600, 400))
    img.save(img_file.replace("tiff", "jpeg"), quality = 95)

path = '~/supplier-data/images/'
images_list = os.listdir(path)

for image in images_list:
    img_changer(path + image)
