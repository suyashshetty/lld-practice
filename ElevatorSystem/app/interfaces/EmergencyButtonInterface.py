from abc import ABC, abstractmethod

class EmergencyButtonInterface(ABC):
    @abstractmethod
    def callEmergencyOperator(self):
        pass
    
    @abstractmethod
    def triggerAlarm(self):
        pass