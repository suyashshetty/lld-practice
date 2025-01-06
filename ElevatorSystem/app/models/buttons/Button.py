from interfaces import ButtonInterface
from abc import ABC, abstractmethod

class Button(ABC, ButtonInterface):
    def __init__(self, name: str):
        self.name = name
        self.isPressed = False
        
    def press(self):
        self.isPressed = True
        print(f"{self.name} button pressed")
        self.action()
        
    def release(self):
        self.isPressed = False
        print(f"{self.name} button released")
        
    def __str__(self):
        return f"Button {self.name} is {self.isPressed}"
        
        