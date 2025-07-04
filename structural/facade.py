'''
Implementation of the Facade Design Pattern
The Facade Pattern provides a simplified interface to a complex subsystem. It is used to hide the complexities of the system and provide a simpler interface to the client code.
Here, we abstract out the details in a facade class, and leave out the details of the subsystem classes..
This facade class is then used for interaction with any client code, which does not need to know about the complexities of the subsystem.

Cons
- Can lead to a proliferation of facade classes, making the codebase more complex.
- May introduce additional layers of abstraction, which can make the code harder to understand.
- Can hide important details of the subsystem, making it difficult to debug or extend the system.
- Can make it difficult to trace the flow of execution, as the facade class may obscure the underlying logic.
Pros
- Simplifies the interface to a complex subsystem, making it easier to use.
- Reduces the dependencies between the client code and the subsystem, promoting loose coupling.
- Encapsulates the complexities of the subsystem, making it easier to maintain and modify.
- Provides a clear and consistent interface for the client code to interact with the subsystem.
Uses
- GUI frameworks where a complex set of components need to be simplified for easier interaction.
- Game development where a complex game engine needs to be simplified for easier interaction.
- Any client code that needs to interact with a complex subsystem, such as a database or a network service.
'''


class CPU:
    def freeze(self):
        print("CPU: Freezing processor.")

    def jump(self, position):
        print(f"CPU: Jumping to {position}.")

    def execute(self):
        print("CPU: Executing instructions.")

class Memory:
    def load(self, position, data):
        print(f"Memory: Loading data '{data}' into position {position}.")

class HardDrive:
    def read(self, lba, size):
        print(f"HardDrive: Reading {size} bytes from LBA {lba}.")
        return f"Data from {lba}"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        print("Facade: Starting computer...")
        self.cpu.freeze()
        data = self.hard_drive.read(100, 1024)
        self.memory.load(0, data)
        self.cpu.jump(0)
        self.cpu.execute()

if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start()