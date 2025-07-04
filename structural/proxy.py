'''
Proxy Pattern Example

The Proxy Pattern is a structural design pattern that provides an object representing another object. It acts as an intermediary, controlling access to the real object and adding additional functionality such as lazy loading, access control, or logging.
This pattern is particularly useful when the real object is resource-intensive to create or access, or when you want to add additional behavior without modifying the real object.

Cons
- Can introduce additional complexity by adding an extra layer of abstraction.
- May lead to performance overhead due to the additional processing required for delegation.
- Can make the code harder to understand if not implemented carefully, as it may obscure the original object's behavior.
- Can lead to tight coupling between the proxy and the real object, making it harder to change either independently.
Pros
- Provides a way to control access to the real object, allowing for lazy loading or access control. 
- Allows for additional behavior to be added without modifying the real object, such as logging or caching.
- Follows the Open/Closed Principle, allowing for easy extension of the codebase by adding new proxies without modifying existing code.
- Simplifies the client code by providing a consistent interface to interact with the real object.
Uses
- When you want to control access to a resource-intensive object, such as a large image or a database connection.
- When you want to add additional behavior to an object without modifying its code, such as logging or caching.
- When you want to implement lazy loading, where the real object is created only when it is needed.
- When you want to implement access control, where certain operations on the real object are restricted based on user permissions.
'''


from abc import ABC, abstractmethod

# Subject Interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Real Subject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._load_from_disk()

    def _load_from_disk(self):
        print(f"Loading image from disk: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")

# Proxy
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        print("Proxy: Delegating display to RealImage.")
        self._real_image.display()

# Client code
if __name__ == "__main__":
    print("Creating proxy_image1...")
    proxy_image1 = ProxyImage("photo1.jpg")
    print("First display call:")
    proxy_image1.display()  # Loads and displays
    print("\nSecond display call:")
    proxy_image1.display()  # Only displays

    print("\nCreating proxy_image2...")
    proxy_image2 = ProxyImage("photo2.png")
    proxy_image2.display()