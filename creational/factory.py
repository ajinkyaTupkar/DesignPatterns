'''
# Factory Pattern Example
The Factory Pattern is a creational design pattern that provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.
It is used to encapsulate the instantiation logic and promote loose coupling between classes.
This pattern is particularly useful when the exact type of the object to be created is not known until runtime,
or when the creation process is complex and should be encapsulated in a separate class.

Cons
- Can lead to a proliferation of factory classes, making the codebase more complex.
- May introduce additional layers of abstraction, which can make the code harder to understand.
- Can make it difficult to trace the instantiation of objects, as the creation logic is separated from the client code.
Pros
- Simplifies object creation by centralizing the instantiation logic in a factory class.
- Promotes loose coupling by separating the creation of objects from their usage.
- Encapsulates the instantiation logic, making it easier to manage and modify.
- Allows for easy extension of the codebase by adding new product types without modifying existing code.
- Facilitates testing by allowing the use of mock objects or stubs in place of real objects.
Uses
- Where a variety of related objects need to be created without specifying their concrete classes.
- GUI frameworks where different types of UI components need to be created.
- Database access layers where different types of database connections or queries need to be created.
- Logging frameworks where different types of loggers (e.g., file logger, console logger) need to be instantiated.
- Game development where different types of game objects (e.g., characters, items) need to be instantiated.
- Network protocols where different types of message handlers or clients need to be created.



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

# Factory
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Unknown shape type")

# Client code
if __name__ == "__main__":
    factory = ShapeFactory()

    shape1 = factory.get_shape("circle")
    print(shape1.draw())

    shape2 = factory.get_shape("square")
    print(shape2.draw())