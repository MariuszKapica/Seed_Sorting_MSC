import os


def train_selected_model(directory, model_name, type, form):
    model_path = os.path.join(directory, "Tensorflow", "workspace", "models", model_name)
    config_path = os.path.join(model_path, "pipeline.config")
    model_main_tf2 = os.path.join(directory, "Tensorflow", "workspace", "model_main_tf2.py")
    model_files = os.listdir(model_path)
    last_checkpint = ''
    number_steps_training = 200000

    for file in model_files:
        try:
            file.index('ckpt')
            if type == 'beg':
                os.remove(os.path.join(model_path, file))
            elif type == 'cont':
                last_checkpint = file
            else:
                print("Wrong input string of beginning  or continuation of training")
                return 0
        except ValueError:
            pass
    if type == 'cont':
        checkpoint_nr = int(last_checkpint[5:-6])
        number_steps_training *= checkpoint_nr * 2000

    training_string = f'python {model_main_tf2} --model_dir={model_path} --pipeline_config_path={config_path} --num_train_steps={number_steps_training}'
    if form == "loc":
        os.system(training_string)
    if form == "sbatch":
        env = input("What is your name of virtual env")
        os.system(f"sbatch --gres gpu:1 anaconda3-launch -env {env} " + training_string)

