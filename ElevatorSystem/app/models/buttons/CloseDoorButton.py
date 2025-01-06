from app.models import Door
from models.buttons import Button

class CloseDoorButton(Button):
    def __init__(self, name: str, door: Door):
        super().__init__(name)
        self.door = door
        self.isEnabled = True
        
    def press(self):
        super().press()
        if self.isEnabled and self.door.isOpen:
            self.door.close()
        self.door.lock()

    def __str__(self):
        return f"{self.name} is {self.isPressed}"