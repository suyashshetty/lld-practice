from strategies.SchedulerStrategy import SchedulerStrategy
from enums.Direction import Direction

class SimpleSequentialStrategy(SchedulerStrategy):
    def getNextFloor(self, currentFloor: int, targetFloors: list[int], direction: int) -> int:
        """
        Determines the next floor based on the scheduling strategy.
        :param currentFloor: The elevator's current floor.
        :param targetFloors: List of requested target floors.
        :param direction: Current direction ("up" or "down").
        :return: The next floor to move to.
        """
        if direction == Direction.UP:
            candidates = [floor for floor in targetFloors if floor > currentFloor]
            return min(candidates) if candidates else max(targetFloors)
        else:
            candidates = [floor for floor in targetFloors if floor < currentFloor]
            return max(candidates) if candidates else min(targetFloors)
            