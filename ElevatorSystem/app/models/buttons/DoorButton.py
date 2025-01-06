from models import Button

class DoorButton(Button):
    def __init__(self, name: str, action: callable):
        super().__init__(name, action)
        
    def press(self):
        self.isPressed = True
        print(f"{self.name} button pressed")
        self.action()
        
    def release(self):
        self.isPressed = False
        print(f"{self.name} button released")
        
    def __str__(self):
        return f"Door button {self.name} is {self.isPressed}"