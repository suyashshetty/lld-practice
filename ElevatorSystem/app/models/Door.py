from app.interfaces import DoorInterface
from enums.DoorState import DoorState
from app.models.sensors import DoorSensor

class Door(DoorInterface):
    def __init__(self):
        self.state = DoorState.LOCKED
        self.sensor = DoorSensor("Door Sensor")
        
    def unlock(self):
        self.state = DoorState.UNLOCKED
        print("Door unlocked")
        
    def lock(self):
        self.state = DoorState.LOCKED
        print("Door locked")
        
    def open(self):
        self.state = DoorState.OPEN
        print("Door opened")
        
    def close(self):
        self.state = DoorState.CLOSED
        print("Door closed")
        
    def __str__(self):  
        return f"Door is {self.state}"