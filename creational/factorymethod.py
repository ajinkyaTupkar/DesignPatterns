'''
# Factory Method Pattern

In this case, rather than defining a factory method in the base class, we define a factory class for each type of shape. This has an abstract method
which needs to be implemented by each subclass. Hence, the creation of objects is delegated to the concrete factory classes.

Cons
- Can lead to a proliferation of factory classes, making the codebase more complex.
- May introduce additional layers of abstraction, which can make the code harder to understand.
Pros
- Simplifies object creation by centralizing the instantiation logic in a factory class.
- Promotes loose coupling by separating the creation of objects from their usage.
- Follows Open Closed Principle, allowing for easy extension of the codebase.
- Encapsulates the instantiation logic, making it easier to manage and modify.
Use
- GUI frameworks where different types of UI components need to be created.
- Game development where different types of game objects (e.g., characters, items) need to be instantiated.
- Database Connections for different type of databases



'''


from abc import ABC, abstractmethod

# Abstract Product
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Products
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"
    
class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

class ShapeFactory:
    @abstractmethod
    def get_shape(self):
        pass

class EdgeShapeFactory(ShapeFactory):
    """
    Factory class to create shapes.
    This class is responsible for creating instances of shapes based on the type provided.
    """
    
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "square":
            return Square()
        elif shape_type == "rectangle":
            return Rectangle())
        else:
            raise ValueError("Unknown shape type")

class RoundShapeFactory(ShapeFactory):
    """
    Factory class to create round shapes.
    This class is responsible for creating instances of round shapes based on the type provided.
    """
    
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        else:
            raise ValueError("Unknown shape type")

# Client code
if __name__ == "__main__":
    edge_factory = EdgeShapeFactory()
    round_factory = RoundShapeFactory()
    shape1 = round_factory.get_shape("circle")
    print(shape1.draw())

    shape2 = edge_factory.get_shape("square")
    print(shape2.draw())