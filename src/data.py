import json
from pathlib import Path

from matplotlib.figure import Figure

from src.models import Drawing


def load_raw_drawing(path: Path) -> Drawing:
    with open(path, "r") as file:
        return Drawing(**json.loads(file.read()))


def save_figure(path: Path, fig: Figure) -> None:
    Path("./out").mkdir(exist_ok=True)

    input_file_name = str(path).split('/')[-1].replace(".json", '')
    fig.savefig(f"./out/{input_file_name}", facecolor=fig.get_facecolor())
