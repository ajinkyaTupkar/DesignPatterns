'''
Abstract Factory Pattern Example

Basically a factory pattern with increased complexity. Instead of a single factory, you define multiple factories, which inherits a common abstract factory interface. This is basically 
to follow Open Closed Principle, where you can add new families of products without modifying existing code. If a new factory needs to be added, you don't need to modify
existing code. You can just create a new factory.

Cons
- Can lead to a proliferation of factory classes, making the codebase more complex.
- May introduce additional layers of abstraction, which can make the code harder to understand.
- Can make it difficult to trace the instantiation of objects, as the creation logic is separated from the client code.
- Can be overkill for simple object creation scenarios, where a simple factory or builder pattern would suffice.
Pros
- Follows Open Closed Principle, allowing for easy extension of the codebase.
- Simplifies object creation by centralizing the instantiation logic in a factory class.
- Promotes loose coupling by separating the creation of objects from their usage.
- Encapsulates the instantiation logic, making it easier to manage and modify.
- Allows for easy extension of the codebase by adding new product families without modifying existing code.
Uses
- GUI frameworks where different types of UI components need to be created.
- Game development where different types of game objects (e.g., characters, items) need to be instantiated.
- Complex real life applications with multiple families of related objects that need to be created together, such as furniture in a home design application.

'''




from abc import ABC, abstractmethod

# Abstract Product A
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

# Abstract Product B
class Table(ABC):
    @abstractmethod
    def use(self):
        pass

# Concrete Product A1
class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian Chair."

# Concrete Product A2
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a Modern Chair."

# Concrete Product B1
class VictorianTable(Table):
    def use(self):
        return "Using a Victorian Table."

# Concrete Product B2
class ModernTable(Table):
    def use(self):
        return "Using a Modern Table."

# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

# Concrete Factory 1
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

    def create_table(self):
        return VictorianTable()

# Concrete Factory 2
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()

# Client Code
def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    print(chair.sit_on())
    print(table.use())

if __name__ == "__main__":
    print("Victorian Furniture:")
    victorian_factory = VictorianFurnitureFactory()
    client_code(victorian_factory)

    print("\nModern Furniture:")
    modern_factory = ModernFurnitureFactory()
    client_code(modern_factory)