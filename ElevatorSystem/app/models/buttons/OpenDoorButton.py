from app.models import Door
from models.buttons import Button

class OpenDoorButton(Button):
    def __init__(self, name: str, action: callable, door: Door):
        super().__init__(name, action)
        self.door = door
        self.isenabled = True
        
    def press(self):
        super().press()
        if self.isenabled and self.door.isLocked:
            self.door.unlock()
        self.door.open()

    def __str__(self):
        return f"{self.name} is {self.isPressed}"