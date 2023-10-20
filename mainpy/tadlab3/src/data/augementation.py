import numpy as np
import pandas as pd
import os.path as path
from typing import Union
from PIL import Image
import albumentations as A
from os import mkdir
import click

height: int = 224
width: int = 224

transform = A.Compose(
    [
        A.RandomBrightnessContrast(brightness_limit=0.8, contrast_limit=0.8, p=0.1),
        A.RandomResizedCrop(height=height, width=width, p=0.1),
        A.RandomRotate90(p=0.1),
        A.RandomToneCurve(scale=0.3, p=0.1),
        A.ElasticTransform(alpha=2.28, p=0.1),
        A.GaussNoise(mean=6, p=0.1),
        A.AdvancedBlur(p=0.1),
        A.RandomRain(brightness_coefficient=0.8, blur_value=5, p=0.1),
    ],
    p=1,
)


@click.command()
@click.argument("csv_path", type=click.Path(exists=True))
@click.argument("input_dir", type=click.Path(exists=True))
@click.argument("output_dir", type=click.Path())
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
@click.option(
    "--data_set_type",
    default="train",
    help="Тип данных (train/test/valid)",
)
@click.option(
    "--do_aug",
    default=True,
    help="Делать ли аугументацию (True/False)",
)
@click.option(
    "--limit_of_class_images",
    default=200,
    help="Какой лимит картинок в одном классе? (200/10/20)",
)
def create_augument_dataset(
    csv_path: str,
    input_dir: str,
    output_dir: str,
    class_id_name: str = "class id",
    data_set_name: str = "data set",
    data_set_type: str = "train",
    do_aug: Union[bool, int] = True,
    limit_of_class_images: int = 200,
) -> None:
    """Функция создает аугументированные данные и сохраняет старые, создает увеличенный датасет
    param: data: данные у которых хотим создать аугументацию
           input dir: место где хранятня папки train/valid/test
           output dir: место куда хотите сохранить новые данные
           data_set_name: название колонки, в которых хранится тип данных (по сути не нужны, можно было руками прописать)
           class_id_name: название колонки, в которой находятся классы (по сути не нужны, можно было руками прописать)
           do_aug: делать ли аугументацию
           limit_of_class_images: Лимит картинок в одном классе (если ставите меньше, чем есть в датасете, то не будут добавляться)
    return: None
    """
    data: pd.DataFrame = pd.read_csv(csv_path)
    tmp_data: pd.DataFrame = data[data[data_set_name] == data_set_type]
    for class_id in range(len(tmp_data[class_id_name].unique())):
        counter: int = 0
        class_data: pd.DataFrame = tmp_data[tmp_data[class_id_name] == class_id]
        rows: int = len(class_data)
        # need rows для балансировки классов
        need_rows: int = limit_of_class_images - rows
        path_data_set_type = path.join(output_dir, data_set_type)
        if path.exists(path_data_set_type):
            # raise Exception(f"Уже существует папка {data_set_type}")
            pass
        else:
            mkdir(path_data_set_type)
        for row in class_data.values:
            if path.exists(path.join(path_data_set_type, row[2])):
                # raise Exception(f"существует уже такая папка {path.join(data_set_type, row[2])}")
                pass
            else:
                mkdir(path.join(path_data_set_type, row[2]))
            img_path: str = path.join(
                input_dir, data_set_type, path.normpath(row[1]).split("\\", 1)[1]
            )
            img_o: Image = Image.open(img_path)
            if counter < need_rows and do_aug:
                img: np.ndarray = np.array(img_o)
                transformed: A.Compose = transform(image=img)["image"]
                Image.fromarray(transformed).save(
                    path.join(output_dir, data_set_type, row[2], f"aug{counter}.jpg")
                )
            img_o.save(path.join(output_dir, data_set_type, row[2], f"{counter}.jpg"))
            counter += 1
            img_o.close()


if __name__ == "__main__":
    create_augument_dataset()
