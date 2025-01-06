from app.models.sensors import Sensor
from interfaces import WeightSensorInterface

class WeightSensor(Sensor, WeightSensorInterface):
    def __init__(self, name, maxWeight):
        super().__init__(name)
        self.maxWeight = maxWeight
        
    def read(self, value):
        self.state = value
        print(f"{self.name} sensor read value {value}")
        
    def detectWeight(self):
        return self.state > 0
    
    def measureWeight(self):
        return self.state
    
    def isOverWeight(self):
        return self.state > self.maxWeight