from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} received message: {message}")

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, message: str):
        pass

# Concrete Subject
class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

# Example usage
if __name__ == "__main__":
    subject = ConcreteSubject()
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    subject.attach(observer1)
    subject.attach(observer2)

    subject.notify("Hello Observers!")

    subject.detach(observer1)
    subject.notify("Second message")