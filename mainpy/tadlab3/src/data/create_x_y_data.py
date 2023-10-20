import sys
import os
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
from sklearn.svm import SVC
import click

from utils import pickle_puck


@click.command()
@click.argument("path_from_data", type=click.Path(exists=True))
@click.argument("path_to_data", type=click.Path())
def create_x_y_data(path_from_data, path_to_data: str) -> None:
    """
    Сохраняет модели для тренировки модели
    :param: path_from_data: место до interim данных
            path_to_data: место до куда сохранять x_y данные
    :return: None
    """
    data = pd.read_pickle(path_from_data)
    data = data.sample(frac=1)
    data["img"]: pd.DataFrame = data["img"].values / 255
    train = data.loc[(data["data set"] == "train") | (data["data set"] == "valid")]
    test = data.loc[data["data set"] == "test"]
    x_train = train["img"].values
    y_train = train["class id"].values
<<<<<<< HEAD
    x_test = test["img"].values
    y_test = test["class id"].values
=======
    x_test = train["img"].values
    y_test = train["class id"].values
>>>>>>> dfa0adf2da6471ebfd023187c9a4ec366cb95a0c
    res_list = [(x_train, y_train), (x_test, y_test)]
    pickle_puck(res_list, path_to_data)


if __name__ == "__main__":
    create_x_y_data()
