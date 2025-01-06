from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, elevatorId: int, currentFloor: int, targetFloors: list[int], direction: int):
        """
        Updates the observer with the current state of the elevator.
        :param elevatorId: The elevator's unique identifier.
        :param currentFloor: The elevator's current floor.
        :param targetFloors: List of requested target floors.
        :param direction: Current direction ("up" or "down").
        """
        pass