from models.buttons.Button import Button
from models.buttons.EmergencyButton import EmergencyButton

class EmergencyButton(Button, EmergencyButton):
    def __init__(self, name: str, action: callable):
        super().__init__(name, action)
        
    def press(self):
        self.isPressed = True
        print(f"{self.name} button pressed")
        self.action()
        
    def release(self):
        self.isPressed = False
        print(f"{self.name} button released")
        
    def triggerAlarm(self):
        print(f"{self.name} button triggered alarm")
        
    def callEmergency(self):
        print(f"{self.name} button called emergency")
        
    def __str__(self):
        return f"Emergency button {self.name} is {self.isPressed}"