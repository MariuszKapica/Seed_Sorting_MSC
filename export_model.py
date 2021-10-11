import os


def export(directory, model_name):
    model_directory = os.path.join(directory, "Tensorflow", "workspace", "models", model_name)
    pipeline_config_path = os.path.join(model_directory, "pipeline.config")
    export_directory = os.path.join(directory, "Tensorflow", "workspace", "exported_models", model_name)
    try:
        os.system(f'python exporter_main_v2.py --input_type image_tensor --pipeline_config_path {pipeline_config_path} --trained_checkpoint_dir {model_directory} --output_directory {export_directory}')
    except Exception:
        os.mkdir(export_directory)
        os.system(
            f'python exporter_main_v2.py --input_type image_tensor --pipeline_config_path {pipeline_config_path} --trained_checkpoint_dir {model_directory} --output_directory {export_directory}')