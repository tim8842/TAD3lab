import os
import json
import matplotlib.pyplot as plt


def compare_results(path_to_models: str):
    models_name = []
    metr_to_plot = []
    for file in os.listdir(path_to_models):
        path_to_folder: str = os.path.join(path_to_models, file)
        if os.path.isdir(path_to_folder):
            print(path_to_folder)
            path_to_metrics = os.path.join(path_to_folder, "metrics.json")
            with open(path_to_metrics, "r") as file:
                models_name.append(os.path.basename(os.path.dirname(path_to_metrics)))
                metrics = json.load(file)
                if isinstance(metrics[list(metrics.keys())[0]], (float)):
                    metrics = {key: [metrics[key]] for key in metrics.keys()}
                else:
                    metrics
                print(metrics)
                print(models_name)


if __name__ == "__main__":
    compare_results("models")
