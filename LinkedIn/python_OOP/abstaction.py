from abc import ABC, abstractmethod


class GraphicShape(ABC):  # ABC = Abstract Base Class
    def __init__(self):
        super().__init__()

    @abstractmethod  # decorator to create an abstract method
    def calculate_area(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius**2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


circle = Circle(10)
print(circle.calculate_area())  # 314.0
