import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict, List
import numpy as np
import click


@click.command()
@click.argument("csv_path", type=click.Path(exists=True))
@click.option(
    "--class_id_name",
    default="class id",
    help="Название колонки с индексами классов (1/2/3)",
)
@click.option(
    "--data_set_name",
    default="data set",
    help="Название колонки с типом данных (train/valid/test)",
)
def show_class_data_diff(
    csv_path: str, class_id_name: str = "class id", data_set_name: str = "data set"
) -> None:
    """Функция показывает балансировку данных по классам
    param: data: датафрейм где нужно посмотреть балансировку
           class_id_name колонка в которой находятся классы (по сути не нужны, можно было руками прописать)
           data_set_name колонка в которой хранится тип данных (train, test, validate) (по сути не нужны, можно было руками прописать)
    return: None
    """
    data: pd.DataFrame = pd.read_csv(csv_path)
    data_gu: pd.DataFrame = data.groupby([class_id_name, data_set_name]).nunique()
    unique_data_set: np.ndarray = data[data_set_name].unique()
    class_balanse: Dict[str, List[int]] = {}
    for name in unique_data_set:
        class_balanse[name]: List = []
    for ind, vals in enumerate(data_gu.values):
        # data_gu.iloc[[ind]].index[0] получает смердженный индекс например "(0, 'test')"
        # vals[0] это количество уникальных картинок
        class_balanse[data_gu.iloc[[ind]].index[0][1]].append(vals[0])
    for ind, name in enumerate(unique_data_set):
        plt.figure(figsize=(6, 6))
        plt.subplot(3, 1, ind + 1)
        plt.plot(class_balanse[name])
        plt.title(f"Балансировка класса у {name}")
    plt.show()


if __name__ == "__main__":
    show_class_data_diff()
