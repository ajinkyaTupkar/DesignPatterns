import threading

'''
# Singleton Pattern Implementation in Python

Should have only one instance of a class and provide a global point of access to it.
This is a common design pattern used to restrict the instantiation of a class to one "single" instance.
This instance is often used to manage shared resources, such as a configuration object or a connection pool.

Cons
- Multiple threads might cause inconsistency --> Need to add thread safety.
- Can lead to issues in unit testing due to the global state.
- Can cause memory exhaustion if not managed properly.
- Makes it difficult to subclass, as the singleton pattern is typically implemented in a way that prevents multiple instances.
- Can introduce hidden dependencies, making the code harder to understand and maintain.
- Can lead to tight coupling between classes, as they may rely on the singleton instance.
Pros
- Promotes lazy initialization, as the instance is created only when it is needed.
- Ensures that a class has only one instance and provides a global point of access to it.
- Encapsulates the instantiation logic, making it easier to manage the lifecycle of the instance.
- Reduces memory usage by sharing a single instance across the application.
- Provides a clear and consistent way to access shared resources.

Uses
- Configuration management
- Logging
- Database connections
- Thread pools
- Event dispatching systems
- Resource management
- Locks and semaphores
- Caching mechanisms
- Global state management
- Service locators
- Dependency injection containers

'''

class Singleton:
    _instance = None

    ## Thread-safe singleton implementation
    _lock = threading.Lock()

    ## Check java file to understand the __new__ and __init__ methods
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.value = None

# Example usage
singleton1 = Singleton()
singleton1.value = "First Instance"

singleton2 = Singleton()
print(singleton2.value)  # Output: First Instance

print(singleton1 is singleton2)  # Output: True