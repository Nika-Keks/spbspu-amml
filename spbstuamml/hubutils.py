import os
import dvc.api


__all__ = ["DSHalper"]

class DSHalper:
    ROOT_CACHE: str = "datahub-cache"
    ROOT_REPO: str = "https://github.com/Nika-Keks/spbstu-datahub.git"
    MODEL_SUBDIR: str = "models"
    DATA_SUBDIR: str = "data"

    def __init__(self, dataset: str) -> None:

        self.dataset = dataset
        self.dataset_path: str = os.path.join(DSHalper.ROOT_CACHE, dataset)
        self.dvc_file_sys = dvc.api.DVCFileSystem(DSHalper.ROOT_REPO, rev=self.dataset, use_listings_cache=False)

        os.makedirs(self.dataset_path, exist_ok=True)

    def get_model_path(self, model: str):
        model_path = os.path.join(self.dataset_path, DSHalper.MODEL_SUBDIR, model)
        if not os.path.isfile(model_path):
            self.dvc_file_sys.get_file(rpath=DSHalper.MODEL_SUBDIR + "/" + model, lpath=model_path)

        return model_path

    def get_dataset_path(self):
        data_path = os.path.join(DSHalper.ROOT_DIR, self.dataset, DSHalper.DATA_SUBDIR)
        if not os.path.isdir(data_path):
            self.dvc_file_sys.get(rpath=DSHalper.DATA_SUBDIR, lpath=data_path, recursive=True)

        return data_path
