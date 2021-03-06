from typing import Tuple

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from src.models import Drawing, Circle, Rectangle

# 'matplotlib' does not work with pixels directly, but uses physical sizes and DPI:
DPI = 100


def draw(drawing: Drawing) -> Figure:
    fig, ax = _setup_plt(drawing)

    for shape_name in drawing.order:
        shape = drawing.get_shape(shape_name)

        drawers[shape.class_name](ax, shape)

    return fig


def draw_circle(ax: Axes, circle: Circle) -> None:
    ax.add_patch(
        plt.Circle((circle.point.x, circle.point.y), circle.radius, color=circle.color.as_hex(), clip_on=True)
    )


def draw_rectangle(ax: Axes, rectangle: Rectangle) -> None:
    ax.add_patch(
        plt.Rectangle(
            (rectangle.point.x, rectangle.point.y),
            rectangle.width, rectangle.height,
            color=rectangle.color.as_hex(), clip_on=True
        )
    )


drawers = {
    "circle": draw_circle,
    "rectangle": draw_rectangle,
}


def _setup_plt(drawing: Drawing) -> Tuple[Figure, Axes]:
    # Set size:
    size = plt.rcParams["figure.figsize"]
    size[1] = drawing.height / DPI
    size[0] = drawing.width / DPI

    # Set background:
    plt.rcParams["figure.facecolor"] = drawing.background_color.as_hex()

    # Init image
    fig, ax = plt.subplots(dpi=DPI)

    plt.axis([0, drawing.width, 0, drawing.height])
    plt.axis("off")

    # Turn off borders around image
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    return fig, ax
