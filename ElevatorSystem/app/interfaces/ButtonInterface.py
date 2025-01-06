from abc import ABC, abstractmethod

class ButtonInterface(ABC):
    @abstractmethod
    def press(self):
        pass
    
    @abstractmethod
    def reset(self):
        pass