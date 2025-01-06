from models.buttons.Button import Button
from models.buttons.EmergencyButton import EmergencyButton

class EmergencyButton(Button, EmergencyButton):
    def __init__(self, name: str):
        super().__init__(name)
        
    def press(self):
        super().press()
        self.triggerAlarm()
        self.callEmergency()    
        
    def triggerAlarm(self):
        print(f"{self.name} button triggered alarm")
        
    def callEmergency(self):
        print(f"{self.name} button called emergency")
        
    def __str__(self):
        return f"Emergency button {self.name} is {self.isPressed}"