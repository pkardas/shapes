from typing import List, Union

from pydantic import BaseModel
from pydantic.color import Color

from src.errors import ShapeNotFoundError


class Shape(BaseModel):
    name: str
    color: Color

    @property
    def class_name(self):
        raise NotImplementedError


class Point(BaseModel):
    x: int
    y: int


class Circle(Shape):
    point: Point
    radius: int

    @property
    def class_name(self):
        return "circle"


class Rectangle(Shape):
    point: Point
    width: int
    height: int

    @property
    def class_name(self):
        return "rectangle"


class Drawing(BaseModel):
    width: int
    height: int
    background_color: Color
    circles: List[Circle]
    rectangles: List[Rectangle]
    order: List[str]

    def get_shape(self, name: str) -> Union[Circle, Rectangle]:
        shape = next((shape for shape in [*self.circles, *self.rectangles] if shape.name == name), None)

        if not shape:
            raise ShapeNotFoundError(f"'{name}' was not found")

        return shape
