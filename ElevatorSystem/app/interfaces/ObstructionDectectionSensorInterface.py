from abc import ABC, abstractmethod

class ObstructionDetectionSensorInterface(ABC):
    @abstractmethod
    def detectObstruction(self):
        pass
    
    