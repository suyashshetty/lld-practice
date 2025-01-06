from abc import ABC, abstractmethod

class DoorInterface(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def close(self):
        pass
    
    @abstractmethod
    def lock(self):
        pass
    
    @abstractmethod
    def unlock(self):
        pass