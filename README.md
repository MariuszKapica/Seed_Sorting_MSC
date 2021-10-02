# Seed Sorting
## How to get all the dependencied to work with the project
Install requirements:
- Anaconda
- Tensorflow Objecte Detecion API
- Protocol Buffer
- CUDA
- cuDNN
- Labelimg - annotation program
- Pre-trained models
## Anaconda
- Follow the link and install anaconda https://www.anaconda.com/products/individual

Anaconda is needed for creating the virtual env of the project. If you are working on remote server and you can not install anaconda, contact your server administartor. There might be an anaconda module able to be loaded. 
 
- To create virtual env with pip and python: "conda create -n <env_name> pip python"
- To activate the virtual env: "conda activate <env_name>"

## Tensorflow Object Detecion API / Protocol Buffer
Protocol Buffer is a dependency needed for installing the TFOB API. TFOB API is the part of the project responsible for training the selected models

- Upadate pip with: "python -m pip install --upgrade pip"
- Install Tensorflow with "pip install --upgrade Tensorflow"
- Check the versions of pip and tensorflow with "pip list"
- To install the TFOB API and Protoc please follow this tutorial: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html
- Clone the https://github.com/tensorflow/models git repository to the <project_directory>/Tensorflow/models
- Add the protoc to the path and install TFOB API

## CUDA / cuDNN

- Find the versions you will need to use at https://www.tensorflow.org/install/source
- Find the right CUDA version at https://anaconda.org/search?q=cuda+toolkit
- Find the right cuDNN at https://anaconda.org/search?q=cuDnn
- To install to conda env use "conda install ..."

## LabelImg

- To install the program clone the git repository https://github.com/tzutalin/labelImg
- Clone the repository to <project_directory>/Tensorflow/labelimg
- Complete the installation process availabe in the readme file of the repository

## Pre-trained models

Download the pre-trained models for the project. Download and extract the model archive to <project_directory>/Tensorflow/workspace/pre_trained_models. Models to download can be found here: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md. Models to download are of your choice but the following were used in the original project:

- http://download.tensorflow.org/models/object_detection/tf2/20200713/centernet_hg104_1024x1024_coco17_tpu-32.tar.gz
- http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d4_coco17_tpu-32.tar.gz
- http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d7_coco17_tpu-32.tar.gz
- http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet50_v1_1024x1024_coco17_tpu-8.tar.gz
- http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8.tar.gz
- http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet101_v1_fpn_1024x1024_coco17_tpu-8.tar.gz

/note if you are using different models you will need to add a new directory with your model name under <project_directory>/Tensorflow/workspace/models/<model_name>

## Workign with the project
To work with the porject run the main.py. The software gives you few menu options:

- Convert tiff images to jpg images - Converts the tiff images to jpg images from the <project_directory>/Tensorflow/workspace/images/collectedimages. This is also a directory where unlabelled images are stored.
- Open annotation program - If installed opens the LabelImg image annotation program.
- Crop labelled images to table size - Crops the whole sized images to the seed table size images. Images and xmls used for cropping got to be placed under <project_directory>/Tensorflow/workspace/images/images_to_crop.
- Crop seeds from labelled images - Crops the seeds from given images to single seed images. Images and xmls used for cropping got to be placed under <project_directory>/Tensorflow/workspace/images/images_to_crop. Give it a few minutes to finish even when the program will say it has finished.
- Change XML files to your project directory - Changes the xml files in <project_directory>/Tensorflow/workspace/images/test and <project_directory>/Tensorflow/workspace/images/train to your project directory
- Generate train.recod and test.record - generates records used for model training
- Train selected model - trains selected model - Before the training be sure to modify the config file to your specification. It can be found under <project_directory>/Tensorflow/workspace/models/<model_name>/pipeline.config
- Train all models - trains all models - Before the training be sure to modify the config file to your specification. It can be found under <project_directory>/Tensorflow/workspace/models/<model_name>/pipeline.config
- Test selected model -test selected model - You can choose the model to be tested. Images used for testing should be placed in <project_directory>/images_to_test. The results of test can be found under <project_directory>/tests
-  Test all models- test all models - Images used for testing should be placed in <project_directory>/images_to_test. The results of test can be found under <project_directory>/tests
-  Export selected model - You can choose the model to be exported. Exports selected model to the <project_directory>/Tensorflow/workspace/exported-models/<model_name>.
-  Export all models - Export models to the <project_directory>/Tensorflow/workspace/exported-models.
-  Exit
