import os
from tiffTojpg import tiff_to_jpg
from annotation_program import open_annotation_program
from makeMoreImages import crop_images
from change_image_dir_in_xml import change_xml
from create_test_train_record import create_records
from train_models import train_selected_model
from test_all_models import test_selected_model
from export_model import export

project_directory = os.getcwd()
models_list = os.listdir(os.path.join(project_directory, "Tensorflow", "workspace", "models"))

menu_dict = {
    '1': 'Convert tiff images to jpg images',
    '2': 'Open annotation program',
    '3': 'Crop labelled images to table size',
    '4': 'Crop seeds from labelled images',
    '5': 'Change XML files to your project directory',
    '6': 'Generate train.recod and test.record',
    '7': 'Train selected model',
    '8': 'Train all models',
    '9': 'Test selected model',
    '10': 'Test all models',
    '11': 'Export selected model',
    '12': 'Export all models',
    '13': 'Exit'
}


def menu():
    print("Menu: ")
    for each in range(0, len(menu_dict)):
        keys = list(menu_dict.keys())
        values = list(menu_dict.values())
        print(keys[each], values[each])
    answer = int(input("What you want to do?"))
    if answer == 1:
        tiff_to_jpg(project_directory)
    elif answer == 2:
        open_annotation_program(project_directory)
    elif answer == 3:
        crop_images(project_directory, "table")
    elif answer == 4:
        crop_images(project_directory, "single_seed")
    elif answer == 5:
        change_xml(project_directory)
    elif answer == 6:
        create_records(project_directory)
    elif answer == 7:
        print("Models List:")
        for nr in range(0, len(models_list)):
            print(nr+1, models_list[nr])
        ans = int(input("Which model would you like to train?"))
        print("Would you train it from beginning or would you like to continue training?")
        type = input("beg or cont //case sensitive")
        print("Would you like to train it locally or by using sbatch script?")
        form = input("loc or sbatch //case sensitive")
        train_selected_model(project_directory, models_list[ans-1], type, form)
    elif answer == 8:
        print("Would you train them from beginning or would you like to continue training?")
        type = input("beg or cont //case sensitive")
        print("Would you like to train them locally or by using sbatch script?")
        form = input("loc or sbatch //case sensitive")
        for each in models_list:
            train_selected_model(project_directory, each, type, form)
    elif answer == 9:
        print("Models List:")
        for nr in range(0, len(models_list)):
            print(nr + 1, models_list[nr])
        ans = int(input("Which model would you like to test?"))
        print("The model is tested on images from images_to_test directory and predictions are saved into tests directory")
        q = input("Please type yes or Yes if you have moved images there")
        if q == 'yes' or q == "yes":
            test_selected_model(project_directory, models_list[ans-1])
        else:
            print("wrong input")
    elif answer == 10:
        print(
            "The model is tested on images from images_to_test directory and predictions are saved into tests directory")
        q = input("Please type yes or Yes if you have moved images there")
        if q == 'yes' or q == "yes":
            for each in models_list:
                test_selected_model(project_directory, each)
        else:
            print("wrong input")
    elif answer == 11:
        print("Models List:")
        for nr in range(0, len(models_list)):
            print(nr + 1, models_list[nr])
        ans = int(input("Which model would you like to export?"))
        export(project_directory, models_list[ans-1])
    elif answer == 12:
        for each in models_list:
            export(project_directory, each)
    elif answer == 13:
        quit()
    else:
        print("Wrong Input. Try once again")


def main():
    while 1:
        os.chdir(project_directory)
        menu()


if __name__ == "__main__":
    main()
