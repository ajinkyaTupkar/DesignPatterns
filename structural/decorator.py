'''
Example of the Decorator Design Pattern
Decorator pattern is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class.
It is achieved by creating a set of decorator classes that are used to wrap concrete components.
This pattern is particularly useful when you want to add responsibilities to objects without modifying their code, allowing for flexible and reusable code.

Cons
- Can lead to a complex structure if many decorators are used, making it difficult to understand the final behavior of the object.
- May introduce performance overhead due to the additional layers of abstraction.
- Can make the code harder to read and maintain if not used judiciously, as it may obscure the original object's behavior.
Pros
- Provides a flexible alternative to subclassing for extending functionality.
- Allows for dynamic addition of responsibilities to objects, enabling behavior to be added or removed at runtime.
- Promotes code reusability by allowing you to create reusable decorators that can be applied to different components.
Uses
- When you want to add responsibilities to individual objects without affecting other objects of the same class.
- When you want to add behavior to objects dynamically at runtime.
- UI frameworks where you want to add features like borders, scrollbars, or shadows to UI components without modifying their code.
- Authentication and logging where you want to add these features to methods or classes without modifying their implementation.
'''

from abc import ABC, abstractmethod

# Component
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1

# Usage
if __name__ == "__main__":
    coffee = SimpleCoffee()
    print("Simple Coffee Cost:", coffee.cost())

    coffee_with_milk = MilkDecorator(coffee)
    print("Coffee with Milk Cost:", coffee_with_milk.cost())

    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print("Coffee with Milk and Sugar Cost:", coffee_with_milk_and_sugar.cost()) 