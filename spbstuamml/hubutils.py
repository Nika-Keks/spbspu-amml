import os
import dvc.api

from pathlib import Path

__all__ = ["URLDatasetHalper"]

class URLDatasetHalper:
    ROOT_DIR: Path = "/home/nika/Documents/projects/Imagerepository"
    #Path.home() / ".spbstu-amml"
    ROOT_CACHE: str = os.path.join(ROOT_DIR, "cache")
    ROOT_REPO: str = os.path.join(ROOT_DIR, "spbstu-datahub")
    MODEL_SUBDIR: str = "models"
    DATA_SUBDIR: str = "data"

    def __init__(self, dataset: str) -> None:

        self.dataset = dataset
        self.dataset_path: str = os.path.join(URLDatasetHalper.ROOT_CACHE, dataset)
        self.dvc_file_sys = dvc.api.DVCFileSystem(URLDatasetHalper.ROOT_REPO, rev=self.dataset)

        os.makedirs(self.dataset_path, exist_ok=True)

    def get_model_path(self, model: str):
        model_path = os.path.join(self.dataset_path, model)
        if not os.path.isfile(model_path):
            self.dvc_file_sys.get_file(rpath=URLDatasetHalper.MODEL_SUBDIR + "/" + model, lpath=model_path)

        return model_path

    def get_dataset_path(self):
        data_path = os.path.join(URLDatasetHalper.ROOT_DIR, self.dataset, URLDatasetHalper.DATA_SUBDIR)
        if not os.path.isdir(data_path):
            self.dvc_file_sys.get(rpath=URLDatasetHalper.DATA_SUBDIR, lpath=data_path, recursive=True)

        return data_path
