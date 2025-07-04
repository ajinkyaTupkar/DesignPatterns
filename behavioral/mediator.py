from abc import ABC, abstractmethod

# Mediator Interface
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

# Concrete Mediator
class DialogMediator(Mediator):
    def __init__(self):
        self.button = None
        self.textbox = None

    def notify(self, sender, event):
        if event == "button_clicked":
            print("Mediator reacts on button click and clears the textbox.")
            self.textbox.clear()
        elif event == "text_entered":
            print("Mediator reacts on text entry and enables the button.")
            self.button.enable()

# Base Component
class Component:
    def __init__(self, mediator: Mediator = None):
        self.mediator = mediator

# Concrete Components
class Button(Component):
    def click(self):
        print("Button clicked.")
        self.mediator.notify(self, "button_clicked")

    def enable(self):
        print("Button enabled.")

class TextBox(Component):
    def enter_text(self, text):
        print(f"Text entered: {text}")
        self.mediator.notify(self, "text_entered")

    def clear(self):
        print("TextBox cleared.")

# Client code
if __name__ == "__main__":
    mediator = DialogMediator()
    button = Button(mediator)
    textbox = TextBox(mediator)
    mediator.button = button
    mediator.textbox = textbox

    textbox.enter_text("Hello World")
    button.click()