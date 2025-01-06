

from app.models.buttons import FloorButton
from app.models.buttons import EmergencyButton

from app.models import Door
from app.models import Display

from app.models.sensors import WeightSensor
from app.models.sensors import FloorSensor



class Elevator:
    def __init__(self, elevator_id, maxWeight, maxPersons, totalFloors):
        self.elevator_id = elevator_id
        self.maxFloors = totalFloors
        self.maxCapacity = maxPersons
        self.isMoving = False
        self.currentFloor = 0
        
        self.buttons = [FloorButton(f"Floor {i}", self.move) for i in range(1, totalFloors + 1)]
        emergencyButton = EmergencyButton("Emergency Button", self.stop)
        self.buttons.append(emergencyButton)
        
        self.door = Door()
        doorOpen = DoorButton("Open", self.door.open)
        doorClose = DoorButton("Close", self.door.close)
        self.buttons.append(doorOpen)
        self.buttons.append(doorClose)
        
        self.display = Display("Elevator")
        self.weightSensor = WeightSensor("Weight Sensor", maxWeight)
        self.floorSensor = FloorSensor("Floor Sensor", totalFloors)
        
        
        
    def addTargetFloor(self, floor):
        if floor not in self.targetFloors:
            self.targetFloors.append(floor)
            self.targetFloors.sort()