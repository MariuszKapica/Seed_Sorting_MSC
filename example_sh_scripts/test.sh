#!/bin/bash --login
###
#SBATCH --job-name=testmodel
#SBATCH -p compute
#SBATCH -e bench.err.%J
#SBATCH -t 0-00:20
#SBATCH -n 1
#SBATCH --mem-per-cpu=4000
###
#now run normal batch commands
module load anaconda/3
source activate tfod
srun python $HOME/load_model_check_on_image.py
