from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):

    def edit(self):
        print("Vscode edits")

    def debug(self):
        print("Vscode debugs")

    def execute(self):
        print("Vscode executes")

obj=Vscode()
obj.debug()