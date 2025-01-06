from strategies.SchedulerStrategy import SchedulerStrategy

class ClosestFloorStrategy(SchedulerStrategy):
    def getNextFloor(self, currentFloor: int, targetFloors: list[int], direction: int) -> int:
        """
        Determines the next floor based on the scheduling strategy.
        :param currentFloor: The elevator's current floor.
        :param targetFloors: List of requested target floors.
        :param direction: Current direction ("up" or "down").
        :return: The next floor to move to.
        """
        if not targetFloors:
            return currentFloor
        
        return min(targetFloors, key=lambda floor: abs(floor - currentFloor))