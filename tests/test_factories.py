from random import randrange

from factory import Factory, Faker, SubFactory, List
from factory.fuzzy import FuzzyText, FuzzyInteger

from src.models import Shape, Point, Circle, Drawing


def generate_range(max_number: int) -> range:
    return range(randrange(max_number))


class ShapeFactory(Factory):
    class Meta:
        model = Shape

    name = FuzzyText()
    color = Faker("color")


class PointFactory(Factory):
    class Meta:
        model = Point

    x = FuzzyInteger(20, 50)
    y = FuzzyInteger(20, 50)


class CircleFactory(ShapeFactory):
    class Meta:
        model = Circle

    point = SubFactory(PointFactory)
    radius = FuzzyInteger(0, 5)


class DrawingFactory(Factory):
    class Meta:
        model = Drawing

    width = FuzzyInteger(0, 100)
    height = FuzzyInteger(0, 100)
    background_color = Faker("color")
    shapes = List([SubFactory(CircleFactory) for _ in generate_range(5)])
