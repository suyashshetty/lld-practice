from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, name):
        self.name = name 
        self.state = None
        
    @abstractmethod
    def read(self, value):
        pass
    
    @abstractmethod
    def getState(self):
        return self.state
    
    def __str__(self):
        return f"{self.name} is {self.state}"