from PIL import Image
import os
directory = os.getcwd()
directory_string = str(directory + "\\Tensorflow\\workspace\\images\\collectedimages")
os.chdir(directory_string)
all_files = os.listdir()
for one in all_files:
    try:
        one.index(".tif")
        print(one)
        img = Image.open(one)
        img.save(str(one[:-4] + ".jpg"), quality=100)
    except ValueError:
        pass