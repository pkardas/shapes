#!/usr/bin/env python3

from pathlib import Path

import typer

from src.data import load_raw_drawing, save_figure
from src.drawing import draw


def main(input_file: Path) -> None:
    drawing = load_raw_drawing(input_file)

    figure = draw(drawing)

    save_figure(input_file, figure)


if __name__ == "__main__":
    typer.run(main)
