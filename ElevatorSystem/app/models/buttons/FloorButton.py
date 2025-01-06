from app.models.buttons.Button import Button

class FloorButton(Button):
    def __init__(self, name: str, floorNum: int):
        super().__init__(name)
        super.floorNum = floorNum
        
    def press(self):
        super().press()
        self.goToFloor()
    
    def goToFloor(self):
        print(f"Going to floor {self.floorNum}")
        return self.floorNum