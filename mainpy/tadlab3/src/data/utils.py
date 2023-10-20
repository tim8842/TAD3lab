import pickle
from typing import Optional, Any
import os.path as path


def pickle_puck(data: Any, path_to_data: str) -> None:
    """
    Запаковывает данные
    :param: data: данные, которые нужно сохранить
            path: путь куда сохранить
    :return: None
    """
    if path.exists(path_to_data):
        menu: str = "..."
        while menu not in ["yes", "no", "да", "нет"]:
            menu: str = input(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                f"Файл {path_to_data} существует введите да/yes, чтобы перезаписать, нет/no, чтобы не записывать\n"
=======
                f"Файл {path_to_data} существует введите да/yes, чтобы перезаписать, нет/no, чтобы не записывать"
>>>>>>> dfa0adf2da6471ebfd023187c9a4ec366cb95a0c
=======
                f"Файл {path_to_data} существует введите да/yes, чтобы перезаписать, нет/no, чтобы не записывать"
>>>>>>> dfa0adf2da6471ebfd023187c9a4ec366cb95a0c
=======
                f"Файл {path_to_data} существует введите да/yes, чтобы перезаписать, нет/no, чтобы не записывать"
>>>>>>> dfa0adf2da6471ebfd023187c9a4ec366cb95a0c
            )
        if menu in ["yes", "да"]:
            with open(path_to_data, "wb") as handle:
                pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        with open(path_to_data, "wb") as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def pickle_unpuck(path_to_data: str) -> Optional[Any]:
    """
    Распаковка данных
    :param: path: путь до файла, который нужно распокавать
    :return: Данные, которые были запакованы
    """
    if path.exists(path_to_data):
        with open(path_to_data, "rb") as handle:
            return pickle.load(handle)
    else:
        return None


if __name__ == "__main__":
    pass
