#!/bin/bash --login
###
#SBATCH --job-name=testmodel
#SBATCH -o bench.out.%J
#SBATCH -e bench.err.%J
#SBATCH -t 0-24:00
#SBATCH --gres=gpu:2
#SBATCH -p gpu
#SBATCH --exclusive

###
#now run normal batch commands 
module load anaconda/3
source activate tfod
srun python $HOME/2.load_model_check_on_image.py