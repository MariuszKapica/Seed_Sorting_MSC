import os

#Create conda enviroment and install packages
os.system('conda create --name conda_env --file conda_env.txt')

#Conda activate envirometn
try:
    os.system("conda activate conda_env")
except Exception:
    os.system("source activate conda_env")

#Install pip packages
os.system("pip install -r pip_env.txt")


