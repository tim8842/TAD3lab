import sys
import os
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
from sklearn.svm import SVC
import click
from typing import Any, Dict, List, Tuple

sys.path.append(os.path.join(sys.path[0], "../data"))
from utils import pickle_unpuck, pickle_puck


@click.command()
@click.argument("name_of_model", type=click.STRING)
@click.argument("type_of_model", type=click.STRING)
@click.argument("path_to_data", type=click.Path())
def train_model(name_of_model: str, type_of_model: str, path_to_data: str) -> None:
    """
    Тренировка моделей
    :param: name_of_model: название модели (можете указать версию или что-либо еще)
            type_of_model: типо модели (предназначено для выбора моделей из словаря)
            path_to_data: путь для конечных значений
    :return: None
    """
    models: Dict[str, Any] = {
        "kn": KNeighborsClassifier(),
        "svc": SVC(verbose=1),
        "hgrad": HistGradientBoostingClassifier(
            verbose=1,
            early_stopping=True,
            n_iter_no_change=2,
            max_iter=15,
            max_depth=6,
            max_leaf_nodes=6,
        ),
    }
    data: List[Tuple[np.ndarray]] = pickle_unpuck(path_to_data)
    x_train, y_train = data[0]
    print(len(x_train))
    model: Any = models[type_of_model]
    model.fit(list(x_train), list(y_train))
    # # cross_model = cross_validate(
    # #     model,
    # #     list(x_train),
    # #     list(y_train),
    # #     cv=5,
    # #     scoring=("accuracy", "f1_macro"),
    # #     return_estimator=True,
    # #     return_train_score=True,
    # #     verbose=1,
    # # )
    path_to_model: str = os.path.join("models", name_of_model)
    if not os.path.exists(path_to_model):
        os.mkdir(path_to_model)
    pickle_puck(model, os.path.join(path_to_model, "model.pkl"))


if __name__ == "__main__":
    train_model()
