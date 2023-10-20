class TQDMBytesReader(object):
    def __init__(self, fd, **kwargs):
        self.fd = fd
        from tqdm import tqdm

        self.tqdm = tqdm(**kwargs)

    def read(self, size=-1):
        bytes = self.fd.read(size)
        self.tqdm.update(len(bytes))
        return bytes

    def readline(self):
        bytes = self.fd.readline()
        self.tqdm.update(len(bytes))
        return bytes

    def __enter__(self):
        self.tqdm.__enter__()
        return self

    def __exit__(self, *args, **kwargs):
        return self.tqdm.__exit__(*args, **kwargs)


import os
import pickle


def test_tqdm_reader():
    from pickle import Unpickler

    with open("models\SVC_Aug.v1\model.pkl", "rb") as fd:
        total = os.path.getsize("models\SVC_Aug.v1\model.pkl")
        obj = 0
        with TQDMBytesReader(fd, total=total) as pbfd:
            up = Unpickler(pbfd)
            obj = up.load()
        with open("data\processed\\augument_x_y_data.pkl", "rb") as handle:
            data = pickle.load(handle)
        x_test, y_test = data[1]
        pred = obj.predict(list(x_test)[0:10])
        print(pred)
        print(f"Loaded {str(obj)}")


test_tqdm_reader()
