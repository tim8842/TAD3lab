import sys
import os
<<<<<<< HEAD
import numpy as np
=======
import pandas as pd
>>>>>>> dfa0adf2da6471ebfd023187c9a4ec366cb95a0c
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
from sklearn.svm import SVC
import click
<<<<<<< HEAD
from typing import Any, Dict, List, Tuple
=======
>>>>>>> dfa0adf2da6471ebfd023187c9a4ec366cb95a0c

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
<<<<<<< HEAD
            path_to_data: путь для конечных значений
    :return: None
    """
    models: Dict[str, Any] = {
=======
    :return: None
    """
    models = {
>>>>>>> dfa0adf2da6471ebfd023187c9a4ec366cb95a0c
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
<<<<<<< HEAD
    data: List[Tuple[np.ndarray]] = pickle_unpuck(path_to_data)
    x_train, y_train = data[0]
    print(len(x_train))
    model: Any = models[type_of_model]
=======
    data = pickle_unpuck(path_to_data)
    x_train, y_train = data[0]
    print(len(x_train))
    x_test, y_test = data[1]
    model = models[type_of_model]
>>>>>>> dfa0adf2da6471ebfd023187c9a4ec366cb95a0c
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
<<<<<<< HEAD
    path_to_model: str = os.path.join("models", name_of_model)
    if not os.path.exists(path_to_model):
        os.mkdir(path_to_model)
    pickle_puck(model, os.path.join(path_to_model, "model.pkl"))
=======
    path_to_model = os.path.join("models", name_of_model)
    os.mkdir(path_to_model)
    pickle_puck(model, os.path.join(path_to_model, "cross_val.pkl"))
>>>>>>> dfa0adf2da6471ebfd023187c9a4ec366cb95a0c


if __name__ == "__main__":
    train_model()
