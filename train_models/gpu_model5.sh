#!/bin/bash --login
###
#SBATCH --job-name=testmodel
#SBATCH -e bench.err.%J
#SBATCH -t 0-24:00
#SBATCH --gres=gpu:2
#SBATCH -p gpu
#SBATCH --exclusive

###
#now run normal batch commands 
module load anaconda/3
source activate tfod
srun python $HOME/Tensorflow/workspace/model_main_tf2.py --model_dir=$HOME/Tensorflow/workspace/models/ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8 --pipeline_config_path=$HOME/Tensorflow/workspace/models/ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8/pipeline.config --num_train_steps=200000