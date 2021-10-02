from PIL import Image
import os


def tiff_to_jpg(directory):
    print("Please move the tiff images to the Tensorflow/workspace/images/collectedimages")
    ans = input("Please type 'yes' or 'Yes' if you have moved the images")
    if ans == "yes" or ans == "Yes":
        directory_string = os.path.join(directory, "Tensorflow", "workspace", "images", "collectedimages")
        os.chdir(directory_string)
        all_files = os.listdir()
        for one in all_files:
            try:
                one.index(".tif")
                img = Image.open(one)
                img.save(str(one[:-4] + ".jpg"), quality=100)
            except ValueError:
                pass
    print("Images Converted")
