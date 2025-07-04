from abc import ABC, abstractmethod

# State interface
class LiftState(ABC):
    @abstractmethod
    def press_button(self, lift, floor):
        pass

    @abstractmethod
    def arrive(self, lift, floor):
        pass

# Concrete States
class IdleState(LiftState):
    def press_button(self, lift, floor):
        print(f"Button for floor {floor} pressed. Lift starting to move.")
        lift.target_floor = floor
        lift.set_state(MovingState())
    
    def arrive(self, lift, floor):
        print("Lift is idle. Already at the floor.")

class MovingState(LiftState):
    def press_button(self, lift, floor):
        print(f"Already moving. Added floor {floor} to queue.")
        lift.queue.append(floor)
    
    def arrive(self, lift, floor):
        print(f"Lift arrived at floor {floor}. Doors opening.")
        lift.current_floor = floor
        if lift.queue:
            next_floor = lift.queue.pop(0)
            print(f"Next target: floor {next_floor}")
            lift.target_floor = next_floor
        else:
            lift.set_state(IdleState())

# Context
class Lift:
    def __init__(self):
        self.state = IdleState()
        self.current_floor = 0
        self.target_floor = None
        self.queue = []

    def set_state(self, state):
        self.state = state

    def press_button(self, floor):
        self.state.press_button(self, floor)

    def arrive(self, floor):
        self.state.arrive(self, floor)

# Example usage
if __name__ == "__main__":
    lift = Lift()
    lift.press_button(3)   # Button for floor 3 pressed. Lift starting to move.
    lift.arrive(3)         # Lift arrived at floor 3. Doors opening.
    lift.press_button(5)   # Button for floor 5 pressed. Lift starting to move.
    lift.press_button(2)   # Already moving. Added floor 2 to queue.
    lift.arrive(5)         # Lift arrived at floor 5. Doors opening.
    lift.arrive(2)         # Lift arrived at floor 2. Doors opening.