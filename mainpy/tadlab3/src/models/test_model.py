import sys
import os
from sklearn.metrics import accuracy_score, recall_score, precision_score
import click
import json
from typing import List, Tuple, Any, Dict
import numpy as np

sys.path.append(os.path.join(sys.path[0], "../data"))
from utils import pickle_unpuck, pickle_puck


@click.command()
@click.argument("path_to_model", type=click.Path(exists=True))
@click.argument("path_to_data", type=click.Path(exists=True))
def train_model(path_to_model: str, path_to_data: str) -> None:
    """
    Тренировка моделей
    :param: name_of_model: название модели (можете указать версию или что-либо еще)
    :param: path_to_data: путь до данных
    :return: None
    """
    data: List[Tuple[np.ndarray]] = pickle_unpuck(path_to_data)
    print(len(data[0][0]))
    x_test, y_test = data[1]
    model: Any = pickle_unpuck(path_to_model)
    predict = model.predict(list(x_test))
    acc: float = accuracy_score(predict, list(y_test))
    recall: float = recall_score(predict, list(y_test), average="macro")
    precision: float = precision_score(predict, list(y_test), average="macro")

    out_dict: Dict[str, Any] = {
        "model": path_to_model.split(os.path.sep)[-2],
        "metrics": {"accuracy": acc, "recall": recall, "precision": precision},
    }
    print(out_dict)
    print(os.path.join(os.path.split(path_to_model)[-2], "metrics.json"))
    with open(
        os.path.join(os.path.split(path_to_model)[-2], "metrics.json"), "w"
    ) as file:
        json.dump(out_dict["metrics"], file)


if __name__ == "__main__":
    train_model()
