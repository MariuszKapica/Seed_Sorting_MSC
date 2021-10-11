import os
import cv2
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
import numpy as np
import datetime


def test_selected_model(directory, model_name):
    models_path = os.path.join(directory, "Tensorflow", "workspace", "models")

    images_path = os.path.join(directory, "images_to_test")
    images_names = os.listdir(images_path)
    images = []
    images_np = []
    for img_name in images_names:
        images.append(cv2.imread(os.path.join(images_path, img_name)))
    for image in images:
        images_np.append(np.array(image))

    try:
        files = os.listdir(os.path.join(models_path, model_name))
        for file in files:
            try:
                file.index("ckpt")
                ckpt_name = file.split(".")[0]
            except ValueError:
                pass
        config = config_util.get_configs_from_pipeline_file(os.path.join(models_path, model_name, 'pipeline.config'))
        detection_model = model_builder.build(model_config=config["model"], is_training=False)
        ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
        ckpt.restore(os.path.join(models_path, model_name, ckpt_name)).expect_partial()
        category_index = label_map_util.create_category_index_from_labelmap(os.path.join(directory, 'Tensorflow', 'workspace', 'annotations', 'label_map.pbtxt'))

        for nr in range(0, len(images_names)):
            input_tensor = tf.convert_to_tensor(np.expand_dims(images_np[nr], 0), dtype=tf.float32)
            images_detection, shapes = detection_model.preprocess(input_tensor)
            prediction_dict = detection_model.predict(images_detection, shapes)
            detections = detection_model.postprocess(prediction_dict, shapes)

            num_detections = int(detections.pop('num_detections'))
            detections = {key: value[0, :num_detections].numpy()
                          for key, value in detections.items()}
            detections['num_detections'] = num_detections

            detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

            label_id_offset = 1
            image_np_with_detections = images[nr].copy()

            viz_utils.visualize_boxes_and_labels_on_image_array(
                image_np_with_detections,
                detections['detection_boxes'],
                detections['detection_classes'] + label_id_offset,
                detections['detection_scores'],
                category_index,
                use_normalized_coordinates=True,
                max_boxes_to_draw=500,
                min_score_thresh=.01,
                agnostic_mode=False)
            image_name = model_name + images_names[nr][:-4] + '.' + str(datetime.datetime.now()) + '.jpg'
            cv2.imwrite(os.path.join(directory, "tests", image_name), image_np_with_detections)
    except Exception as e:
        print(e)

