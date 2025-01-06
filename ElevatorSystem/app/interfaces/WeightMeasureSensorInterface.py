from abc import ABC, abstractmethod 

class WeightMeasureSensorInterface(ABC):
    
    def __init__(self, maxWeight: float):
        super().__init__()
        self.maxWeight = maxWeight
        
    @abstractmethod
    def measureWeight(self):
        pass
    
    @abstractmethod
    def isOverWeight(self):
        pass