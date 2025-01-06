from enums.LightsState import LightsState

class Lights:
    def __init__(self, name, state):
        self.name = name
        self.state = state
        
    def turnOn(self):
        self.state = LightsState.LIGHTS_ON
        print(f"{self.name} lights turned on")
        
    def turnOff(self):
        self.state = LightsState.LIGHTS_OFF
        print(f"{self.name} lights turned off")
        
    def __str__(self):
        return f"{self.name} lights are {self.state}"