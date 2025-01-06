from interfaces import ButtonInterface
from abc import ABC, abstractmethod

class Button(ABC, ButtonInterface):
    def __init__(self, name: str, action: callable):
        self.name = name
        self.isPressed = False
        self.action = action
        
    def __str__(self):
        return f"Button {self.name} is {self.isPressed}"
        
        