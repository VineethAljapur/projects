"""Main module."""

import cv2
from PIL import Image
from cosmic_conn import init_model


def create_cb(image_path, model="ground_imaging", output: str = "output.png") -> None:
    """Creates cosmic con image"""
    image = cv2.imread(image_path, 0)
    image = cv2.resize(image, (256, 256))

    cr_model = init_model(model)
    cr_prob = cr_model.detect_cr(image)
    cr_mask = cr_prob > 0.5

    img = Image.fromarray(cr_mask)
    img.save(output)

if __name__ == "__main__":
    pass
