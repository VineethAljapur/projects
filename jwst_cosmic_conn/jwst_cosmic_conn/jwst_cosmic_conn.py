"""Main module."""

import cv2
from PIL import Image


def create_cb(image_path, output: str = "output.pngs") -> None:
    """Creates cosmic con image"""
    image = cv2.imread(image_path, 0)
    
    return

if __name__ == "__main__":
    pass
