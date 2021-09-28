import os
from PIL import Image
from xml.etree import ElementTree as ET
from uuid import uuid4


def crop_files_move_boxes():
    for one in all_files:
        try:
            one.index(".jpg")
            img = Image.open(one)
            height = img.height
            width = img.width
            region = img.crop((int(width - width / 1.04), int(height - height / 1.53), int(width - width / 14), height))
            xml = ET.parse(str(one[:-3] + "xml"))
            root = xml.getroot()
            for obj in root.iter('annotation'):
                file_name = str(uuid4())
                new_root = ET.Element("annotaion")

                elem1 = ET.Element("folder")
                elem1.text = "train"
                new_root.append(elem1)

                elem2 = ET.Element("filename")
                elem2.text = file_name + '.jpg'
                new_root.append(elem2)

                elem3 = ET.Element("path")
                elem3.text = str(directory + '\\' + file_name + '.jpg')
                print(elem3.text)
                new_root.append(elem3)

                elem4 = ET.Element("source")
                elem4_sub1 = ET.SubElement(elem4, "database")
                elem4_sub1.text = "Unknown"
                new_root.append(elem4)

                elem5 = ET.Element("size")
                elem5_sub1 = ET.SubElement(elem5, "width")
                elem5_sub2 = ET.SubElement(elem5, "height")
                elem5_sub3 = ET.SubElement(elem5, "depth")
                elem5_sub1.text = str(int((width - width / 14 - width - width / 1.04) * -1))
                elem5_sub2.text = str(int(height / 1.53))
                elem5_sub3.text = "3"
                new_root.append(elem5)

                elem6 = ET.Element("segnmentated")
                elem6.text = "0"
                new_root.append(elem6)

                for each in obj.iter("object"):
                    for another in each.iter():
                        if another.tag == "name":
                            seed_class = another.text
                        if another.tag == "xmin":
                            xmin = int(another.text)
                        if another.tag == "ymin":
                            ymin = int(another.text)
                        if another.tag == "xmax":
                            xmax = int(another.text)
                        if another.tag == "ymax":
                            ymax = int(another.text)
                        try:
                            elem7 = ET.Element("object")
                            elem7_sub1 = ET.SubElement(elem7, "name")
                            elem7_sub2 = ET.SubElement(elem7, "pose")
                            elem7_sub3 = ET.SubElement(elem7, "truncated")
                            elem7_sub4 = ET.SubElement(elem7, "difficult")
                            elem7_sub5 = ET.SubElement(elem7, "bndbox")
                            elem7_sub5_sub1 = ET.SubElement(elem7_sub5, "xmin")
                            elem7_sub5_sub2 = ET.SubElement(elem7_sub5, "ymin")
                            elem7_sub5_sub3 = ET.SubElement(elem7_sub5, "xmax")
                            elem7_sub5_sub4 = ET.SubElement(elem7_sub5, "ymax")
                            elem7_sub1.text = seed_class
                            elem7_sub2.text = "Unspecified"
                            elem7_sub3.text = "0"
                            elem7_sub4.text = "0"
                            elem7_sub5_sub1.text = str(int(xmin - width / 1.03 + width -width/14))
                            elem7_sub5_sub2.text = str(int(ymin + height / 1.53 -height))
                            elem7_sub5_sub3.text = str(int(xmax - width / 1.04 + width-width/14))
                            elem7_sub5_sub4.text = str(int(ymax + height / 1.53 -height))

                        except NameError:
                            pass
                    new_root.append(elem7)

                tree = ET.ElementTree(new_root)

                with open(str(file_name + ".xml"), "wb") as files:
                    tree.write(files)

                region = region.save(str(file_name + ".jpg"))

        except ValueError:
            pass


def create_one_seed_files_and_xml():
    for one in all_files:
        try:
            one.index(".xml")
            xml = ET.parse(one)
            root = xml.getroot()
            for obj in root.iter('object'):
                img = Image.open(str(one[:-3] + "jpg"))
                for each in obj.iter():
                    if each.tag == "name":
                        seed_class = each.text
                    if each.tag == "xmin":
                        xmin = int(each.text)
                    if each.tag == "ymin":
                        ymin = int(each.text)
                    if each.tag == "xmax":
                        xmax = int(each.text)
                    if each.tag == "ymax":
                        ymax = int(each.text)

                file_name = str(uuid4())

                new_root = ET.Element("annotaion")

                elem1 = ET.Element("folder")
                elem1.text = "train"
                new_root.append(elem1)

                elem2 = ET.Element("filename")
                elem2.text = file_name + '.jpg'
                new_root.append(elem2)

                elem3 = ET.Element("path")
                elem3.text = str(directory + '\\' + file_name + '.jpg')
                new_root.append(elem3)

                elem4 = ET.Element("source")
                elem4_sub1 = ET.SubElement(elem4, "database")
                elem4_sub1.text = "Unknown"
                new_root.append(elem4)

                elem5 = ET.Element("size")
                elem5_sub1 = ET.SubElement(elem5, "width")
                elem5_sub2 = ET.SubElement(elem5, "height")
                elem5_sub3 = ET.SubElement(elem5, "depth")
                elem5_sub1.text = str(xmax - xmin)
                elem5_sub2.text = str(ymax - ymin)
                elem5_sub3.text = "3"
                new_root.append(elem5)

                elem6 = ET.Element("segnmentated")
                elem6.text = "0"
                new_root.append(elem6)

                elem7 = ET.Element("object")
                elem7_sub1 = ET.SubElement(elem7, "name")
                elem7_sub2 = ET.SubElement(elem7, "pose")
                elem7_sub3 = ET.SubElement(elem7, "truncated")
                elem7_sub4 = ET.SubElement(elem7, "difficult")
                elem7_sub5 = ET.SubElement(elem7, "bndbox")
                elem7_sub5_sub1 = ET.SubElement(elem7_sub5, "xmin")
                elem7_sub5_sub2 = ET.SubElement(elem7_sub5, "ymin")
                elem7_sub5_sub3 = ET.SubElement(elem7_sub5, "xmax")
                elem7_sub5_sub4 = ET.SubElement(elem7_sub5, "ymax")
                elem7_sub1.text = seed_class
                elem7_sub2.text = "Unspecified"
                elem7_sub3.text = "0"
                elem7_sub4.text = "0"
                elem7_sub5_sub1.text = "0"
                elem7_sub5_sub2.text = "0"
                elem7_sub5_sub3.text = str(xmax - xmin)
                elem7_sub5_sub4.text = str(ymax - ymin)
                new_root.append(elem7)

                tree = ET.ElementTree(new_root)

                with open(str(file_name + ".xml"), "wb") as files:
                    tree.write(files)

                region = img.crop((xmin, ymin, xmax, ymax))
                region.save(str(file_name + ".jpg"))
        except ValueError:
            pass




directory_main = os.getcwd()
directory_string = str(directory_main + "\\Tensorflow\\workspace\\images\\test")
os.chdir(directory_string)
directory = os.getcwd()
all_files = os.listdir()
crop_files_move_boxes()
create_one_seed_files_and_xml()

directory_string = str(directory_main + "\\Tensorflow\\workspace\\images\\train")
os.chdir(directory_string)
directory = os.getcwd()
all_files = os.listdir()
crop_files_move_boxes()
create_one_seed_files_and_xml()


