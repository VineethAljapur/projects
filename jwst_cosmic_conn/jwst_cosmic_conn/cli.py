"""Console script for jwst_cosmic_conn."""
import argparse
import sys
import logging

from jwst_cosmic_conn import create_cb

logging.basicConfig(level=logging.INFO)

def main():
    """Console script for jwst_cosmic_conn."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, help="Path of the image to analyze")
    args = parser.parse_args()

    logging.info(args)

    create_cb(args.image)
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
