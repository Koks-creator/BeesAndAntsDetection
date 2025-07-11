from pathlib import Path
from typing import Union
import logging
import os


class Config:
    ROOT_PATH: str = Path(__file__).resolve().parent
    CLI_LOG_LEVEL: int = logging.INFO
    FILE_LOG_LEVEL: int = logging.INFO

    # Folders
    RAW_DATA_PATH: Union[str, os.PathLike, Path] = fr"{ROOT_PATH}/RawData"
    CLEANED_DATA_PATH: Union[str, os.PathLike, Path] = fr"{ROOT_PATH}/DataCleaned"
    TRAIN_IMAGES_FOLDER: Union[str, os.PathLike, Path] = fr"{ROOT_PATH}/train_data/images/train"
    VAL_IMAGES_FOLDER: Union[str, os.PathLike, Path] = fr"{ROOT_PATH}/train_data/images/val"
    TRAIN_LABELS_FOLDER: Union[str, os.PathLike, Path] = fr"{ROOT_PATH}/train_data/labels/train"
    VAL_LABELS_FOLDER: Union[str, os.PathLike, Path] = fr"{ROOT_PATH}/train_data/labels/val"
    TEST_DATA_FOLDER: Union[str, os.PathLike, Path] = fr"{ROOT_PATH}/TestData"
    VIDEOS_FOLDER: Union[str, os.PathLike, Path] =  fr"{ROOT_PATH}/Videos"
    MODELS_PATH: Union[str, os.PathLike, Path] = fr"{ROOT_PATH}/models"
    # Model
    CLASSES_PATH: Union[str, os.PathLike, Path] = fr"{MODELS_PATH}/classes.txt"
    MODEL_PATH: Union[str, Path] = f"{MODELS_PATH}/model5_fine_tuned/best (15) fined tuned.pt"
    DEVICE: str = "cpu"

    # Regular model params
    IOU: float = .35
    CONF_THRESH: float = .2
    AUGMENT: bool = True
    AGNOSTIC_NMS: bool = True

    # Sahi model params
    USE_SAHI: bool = True
    SAHI_CONF_THRESH: float = .2
    SAHI_SLICE_HEIGHT: int = 400
    SAHI_SLICE_WIDTH: int = 400
    SAHI_OVERLAP_HEIGHT_RATIO: float = 0.3
    SAHI_OVERLAP_WIDTH_RATIO: float = 0.3

    # Main system
    TRACK: bool = True
    DRAW_TRACK: bool = True
    MIN_DET_FRAMES: int = 2
    SORT_MAX_AGE: int = 50
    SORT_MIN_HITS: int = 1
    SORT_IOU_THRESHOLD: float = .1
    FONT_SIZE: float = 1.4
    FONT_THICK: int = 2
    BBOX_THICK: int = 2

    # Dataset filtering
    MIN_HEIGHT: int = 120
    MIN_WIDTH: int = 120
    MAX_HEIGHT: int = 4000
    MAX_WIDTH: int = 4000
    ALLOWED_EXTENSIONS: tuple = (".jpg", ".png", ".jpeg")
