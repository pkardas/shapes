from typing import List, Union, Optional

from pydantic import BaseModel
from pydantic.color import Color


class Shape(BaseModel):
    name: Optional[str]
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


class Square(Shape):
    point: Point
    length: int

    @property
    def class_name(self):
        return "square"


class Polygon(Shape):
    points: List[Point]

    @property
    def class_name(self):
        return "polygon"


class Drawing(BaseModel):
    width: int
    height: int
    background_color: Color
    shapes: List[Union[Circle, Rectangle, Square, Polygon]]
