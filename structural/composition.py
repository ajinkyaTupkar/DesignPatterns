'''
Composite Pattern Example
This design pattern allows you to compose objects into a tree structure. The root will be an interface, which will be implemented by both leaf and composite objects.
The composite object will contain a collection of leaf objects and other composite objects, allowing you to treat individual objects and compositions uniformly.

Cons
- Can lead to a complex structure if not managed properly, making it difficult to understand the hierarchy.
- May introduce performance overhead due to the recursive nature of the structure.
- Can make it harder to enforce specific behaviors on leaf objects, as they are treated uniformly with composite objects.
Pros
- Simplifies client code by allowing it to treat individual objects and compositions uniformly.
- Promotes code reusability by allowing you to create complex structures from simple objects.
- Follows the Open/Closed Principle, allowing for easy extension of the codebase by adding new leaf or composite types without modifying existing code.
Uses
- GUI frameworks where UI components can be composed of other components (e.g., panels containing buttons and text fields).
- File systems where directories can contain files and other directories.
- Game development where game objects can be composed of other game objects (e.g., a character composed of body parts).
- Document structures where documents can contain sections, paragraphs, and other documents.
'''

from abc import ABC, abstractmethod

# Component
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

# Leaf
class Circle(Graphic):
    def draw(self):
        print("Drawing a Circle")

class Square(Graphic):
    def draw(self):
        print("Drawing a Square")

# Composite
class CompositeGraphic(Graphic):
    def __init__(self):
        self._children = []

    def add(self, graphic: Graphic):
        self._children.append(graphic)

    def remove(self, graphic: Graphic):
        self._children.remove(graphic)

    def draw(self):
        for child in self._children:
            child.draw()

# Usage
if __name__ == "__main__":
    circle1 = Circle()
    circle2 = Circle()
    square1 = Square()

    composite1 = CompositeGraphic()
    composite1.add(circle1)
    composite1.add(square1)

    composite2 = CompositeGraphic()
    composite2.add(circle2)
    composite2.add(composite1)

    print("Drawing composite2:")
    composite2.draw()