from PIL import Image
from os import listdir
from os.path import splitext

dir = "."
png_ext = '.png'

for file in listdir(dir):
    name, ext = splitext(file)
    try:
        if ext not in ['.py', png_ext]:
            im = Image.open(name + ext)
            im.save(name + "_converted" + png_ext)
    except OSError:
        print('Cannot convert %s' % file)