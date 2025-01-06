from interfaces.observer import Observer

class Display(Observer):
    def __init__(self, displayType: str):
        self.displayType = displayType
        self.currentFloor = None
        self.direction = None
        self.message = None  # For error, emergency, maintenance messages

    def __str__(self):
        if self.message:
            return f"{self.displayType} display: {self.message}"  # For special messages
        return f"{self.displayType} display: Floor {self.currentFloor}, Direction {self.direction}"

    def update(self, currentFloor: int, direction: str, totalFloors: int, message: str = None):
        """
        Updates the display with the current floor, direction, and optional message.
        :param currentFloor: Current floor of the elevator.
        :param direction: Current direction ("up" or "down").
        :param totalFloors: Total floors in the building (for potential validations or enhancements).
        :param message: Optional message for emergencies or maintenance.
        """
        self.currentFloor = currentFloor
        self.direction = direction
        self.message = message
        print(self)  # Print the updated state

    def reset(self):
        """Resets the display to its default state."""
        self.currentFloor = None
        self.direction = None
        self.message = None
        print("Display reset")
