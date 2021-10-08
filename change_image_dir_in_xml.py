import os
from xml.etree import ElementTree as ET


def make_change(files, directory):
    os.chdir(directory)
    for file in files:
        try:
            file.index(".xml")
            xml = ET.parse(file)
            root = xml.getroot()
            for obj in root.iter():
                if obj.tag == "filename":
                    filename = obj.text
                if obj.tag == "path":
                    obj.text = os.path.join(directory, filename)
            xml.write(file)
        except ValueError:
            pass


def change_xml(directory):
    print("This part changes xml files in the appropriate test and train folders")
    ans = input("Please type 'yes' or 'Yes' if you understand")
    if ans == 'yes' or ans == 'Yes':
        main_directory = directory
        test_dir = os.path.join(main_directory, 'Tensorflow', 'workspace', 'images', 'test')
        train_dir = os.path.join(main_directory, 'Tensorflow', 'workspace', 'images', 'train')

        files_in_dir = os.listdir(test_dir)
        make_change(files_in_dir, test_dir)

        files_in_dir = os.listdir(train_dir)
        make_change(files_in_dir, train_dir)
    else:
        pass
