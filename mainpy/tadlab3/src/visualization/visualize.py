import os
import json
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List
import click


@click.command()
@click.argument("path_to_models", type=click.Path(exists=True))
def compare_results(path_to_models: str) -> None:
    """
    Тренировка моделей
    :param: path_to_data: путь до папки моделей
    :return: None
    """
    models_name: List = []
    metr_to_plot: Dict[str, List[float]] = {}
    for file in os.listdir(path_to_models):
        path_to_folder: str = os.path.join(path_to_models, file)
        if os.path.isdir(path_to_folder):
            path_to_metrics: str = os.path.join(path_to_folder, "metrics.json")
            with open(path_to_metrics, "r") as file:
                models_name.append(os.path.basename(os.path.dirname(path_to_metrics)))
                metrics: Dict[str, float] = json.load(file)
                if not metr_to_plot:
                    metr_to_plot: Dict[str, List[float]] = {
                        key: [round(metrics[key], 2)] for key in metrics.keys()
                    }
                else:
                    metr_to_plot: Dict[str, List[float]] = {
                        key: metr_to_plot[key] + [round(metrics[key], 2)]
                        for key in metrics.keys()
                    }
    X_axis: np.ndarray = np.arange(len(models_name))
    for key in metr_to_plot:
        plt.figure(figsize=(10, 5))
        for index, _ in enumerate(models_name):
            plt.bar(
                [models_name[index]],
                [metr_to_plot[key][index]],
                label=models_name[index],
            )
            plt.text(
                index,
                metr_to_plot[key][index] + 0.005,
                metr_to_plot[key][index],
                ha="center",
            )
        plt.title(f"Model's {key}")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    compare_results()
