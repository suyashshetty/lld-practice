from app.models.sensors import Sensor
from interfaces import ObstructionDectectionSensorInterface

class DoorSensor(Sensor, ObstructionDectectionSensorInterface):
    def __init__(self, name):
        super().__init__(name)
        
    def read(self, value):
        self.state = value
        print(f"{self.name} sensor read value {value}")
        
    def detectObstruction(self):
        return self.state == True
    