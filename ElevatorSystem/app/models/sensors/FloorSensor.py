from app.models.sensors import Sensor

class FloorSensor(Sensor):
    def __init__(self, name, totalFloors):
        super().__init__(name)
        self.totalFloors = totalFloors
        self.floor = 0
        
    def read(self, value):
        self.floor = value
        print(f"{self.name} sensor read value {value}")
        
    def detectFloor(self):
        return self.floor > 0 and self.floor <= self.totalFloors
    
    def measureFloor(self):
        return self.floor