import os


def create_records(directory):
    print("Creating train.record and test.record")
    main_directory = directory
    label_map_dir = os.path.join(main_directory, "Tensorflow", "workspace", "annotations", "label_map.pbtxt")
    train_images_dir = os.path.join(main_directory, "Tensorflow", "workspace", "images", "train")
    test_images_dir = os.path.join(main_directory, "Tensorflow", "workspace", "images", "test")
    annotations_dir = os.path.join(main_directory, "Tensorflow", "workspace", "annotations")
    train_record = os.path.join(annotations_dir, "train.record")
    test_record = os.path.join(annotations_dir, "test.record")

    os.system(f"python generate_tfrecord.py -x {train_images_dir} -l {label_map_dir} -o {train_record}")
    os.system(f"python generate_tfrecord.py -x {test_images_dir} -l {label_map_dir} -o {test_record}")
