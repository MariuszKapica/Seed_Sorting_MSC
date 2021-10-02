import os


def open_annotation_program(directory):
    label_img_path = os.path.join(directory, "Tensorflow", "labelImg")
    if os.path.isdir(label_img_path):
        os.chdir(label_img_path)
        os.system("python labelimg.py")
        print("Please remember to move labelled images with xml files to the appropriate train and test folders")
    else:
        print("Please install the annotation program and try again")
