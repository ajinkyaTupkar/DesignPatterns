from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, request):
        pass

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request < 10:
            print(f"HandlerA handled request: {request}")
        elif self._successor:
            self._successor.handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if 10 <= request < 20:
            print(f"HandlerB handled request: {request}")
        elif self._successor:
            self._successor.handle(request)

class ConcreteHandlerC(Handler):
    def handle(self, request):
        if request >= 20:
            print(f"HandlerC handled request: {request}")
        elif self._successor:
            self._successor.handle(request)

if __name__ == "__main__":
    # Set up the chain: A -> B -> C
    handler_chain = ConcreteHandlerA(ConcreteHandlerB(ConcreteHandlerC()))

    requests = [5, 14, 22, 3, 18, 27]
    for req in requests:
        handler_chain.handle(req)