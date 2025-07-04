from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver
class Editor:
    def __init__(self):
        self.text = ""
        self.history = []

    def write(self, text):
        self.history.append(self.text)
        self.text += text

    def erase(self, length):
        self.history.append(self.text)
        self.text = self.text[:-length]

    def undo(self):
        if self.history:
            self.text = self.history.pop()

# Concrete Commands
class WriteCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.write(self.text)

    def undo(self):
        self.editor.undo()

class EraseCommand(Command):
    def __init__(self, editor, length):
        self.editor = editor
        self.length = length

    def execute(self):
        self.editor.erase(self.length)

    def undo(self):
        self.editor.undo()

# Invoker
class EditorInvoker:
    def __init__(self):
        self.commands = []

    def execute_command(self, command):
        command.execute()
        self.commands.append(command)

    def undo_last(self):
        if self.commands:
            command = self.commands.pop()
            command.undo()

# Usage Example
if __name__ == "__main__":
    editor = Editor()
    invoker = EditorInvoker()

    write_cmd = WriteCommand(editor, "Hello, ")
    invoker.execute_command(write_cmd)
    write_cmd2 = WriteCommand(editor, "world!")
    invoker.execute_command(write_cmd2)
    print(editor.text)  # Output: Hello, world!

    erase_cmd = EraseCommand(editor, 6)
    invoker.execute_command(erase_cmd)
    print(editor.text)  # Output: Hello,

    invoker.undo_last()
    print(editor.text)  # Output: Hello, world!