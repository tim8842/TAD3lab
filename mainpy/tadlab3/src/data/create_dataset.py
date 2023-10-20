import numpy as np
import pandas as pd
import os.path as path
from typing import Optional
from PIL import Image
from os import listdir
import click


@click.command()
@click.argument("csv_path", type=click.Path(exists=True))
@click.argument("input_dir", type=click.Path(exists=True))
@click.argument("output_dir", type=click.Path())
# @click.argument("output_dir", type=click.Path())
def create_csv_data(
    csv_path: str, input_dir: str, output_dir: Optional[str] = None
) -> (
    pd.DataFrame
):  # data_set_type: str = "train", data_set_name:str = "data set", class_id_name: str = "class id") -> List[Generator]:
    data: pd.DataFrame = pd.read_csv(csv_path)
    new_data: pd.DataFrame = data.iloc[:0].copy()
    new_data["img"] = 0
    """Функция создания датасета на основе данных
    param: data: датасет с которого копировать стилистику
           input_dir папка с данными
           output_dir куда сохранить данные
    return: путь по которому сохранил данные
    """
    for data_set_type in listdir(path.normpath(input_dir)):
        path_to_type: str = path.join(input_dir, data_set_type)
        if path.isdir(path_to_type):
            for class_id_type in listdir(path_to_type):
                path_to_class: str = path.join(path_to_type, class_id_type)
                if path.isdir(path_to_class):
                    for file in listdir(path_to_class):
                        path_to_file: str = path.join(path_to_class, file)
                        with Image.open(path_to_file) as file:
                            img: Image = file.resize((80, 80))
                            img: np.ndarray = np.array(img)
                            new_data.loc[len(new_data)] = [
                                data[data["labels"] == class_id_type].iloc[0].values[0],
                                path_to_file,
                                class_id_type,
                                data_set_type,
                                np.ravel(img),
                            ]
    # path_to_save: str = path.join(path.normpath(output_dir), "data.csv")
    # if path.exists(path_to_save):
    #     raise Exception("Файл уже существует")
    # else:
    #     new_data.to_csv(path_to_save, index=False)
    print(type(new_data))
    new_data.to_pickle(path.join(output_dir))
    return new_data


if __name__ == "__main__":
    create_csv_data()
