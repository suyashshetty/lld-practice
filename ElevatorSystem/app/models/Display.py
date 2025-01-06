class Display:
    def __init__(self, displayType: str):
        self.displayType = displayType
        self.currentFloor = None
        self.direction = None
        self.message = None # for error, emergency, maintenance messages
        
    def __str__(self):
        return f"{self.displayType} display: Floor {self.currentFloor}, Direction {self.direction}"
        
    def updateFloor(self, floor):
        self.currentFloor = floor
        print(f"Current floor : {floor}")
        
    def updateDirection(self, direction):
        self.direction = direction
        print(f"Current Direction : {direction}")
        
    def updateMessage(self, message):
        self.message = message
        print(f"Message: {message}")
        
    def reset(self):
        self.currentFloor = None
        self.direction = None
        self.message = None
        print("Display reset")
        
    def __str__(self):  
        if self.message:
            return f"{self.displayType} display: {self.message}" # for error, emergency, maintenance messages
        else:    
            return f"Floor {self.currentFloor}, Direction {self.direction}" 
        