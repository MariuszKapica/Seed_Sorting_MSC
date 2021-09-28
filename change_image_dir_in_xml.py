import os
from xml.etree import ElementTree as ET
from sys import platform

def change_xml_win(files, directory):
    for file in files:
        try:
            file.index(".xml")
            xml = ET.parse(file)
            root = xml.getroot()
            for obj in root.iter():
                if obj.tag == "filename":
                    filename = obj.text
                if obj.tag == "path":
                    obj.text = str(directory + '\\' + filename)
            xml.write(file)
        except ValueError:
            pass

def change_xml_linux(files, directory):
    for file in files:
        try:
            file.index(".xml")
            xml = ET.parse(file)
            root = xml.getroot()
            for obj in root.iter():
                if obj.tag == "filename":
                    filename = obj.text
                if obj.tag == "path":
                    obj.text = str(directory + '/' + filename)
            xml.write(file)
        except ValueError:
            pass


if platform == "win32":
    main_directory = os.getcwd()
    test_dir = str(main_directory + '\\Tensorflow\\workspace\\images\\test')
    train_dir = str(main_directory + '\\Tensorflow\\workspace\\images\\train')

    os.chdir(test_dir)
    files_in_dir = os.listdir()
    change_xml_win(files_in_dir, test_dir)

    os.chdir(train_dir)
    files_in_dir = os.listdir()
    change_xml_win(files_in_dir, train_dir)

if platform == "linux" or platform == "linux2":
    main_directory = os.getcwd()
    test_dir = str(main_directory + '/Tensorflow/workspace/images/test')
    train_dir = str(main_directory + '/Tensorflow/workspace/images/train')

    os.chdir(test_dir)
    files_in_dir = os.listdir()
    change_xml_linux(files_in_dir, test_dir)

    os.chdir(train_dir)
    files_in_dir = os.listdir()
    change_xml_linux(files_in_dir, train_dir)

