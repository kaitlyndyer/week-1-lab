# Create the light switch
class LightSwitch:
    def __init__(self, state: bool = False) -> None:
        self.state = state # attribute to track switch state
    
    def turn_on(self) -> None:
        """Turn the switch on"""
        self.state = True

    def turn_off(self) -> None:
        """Turn the switch off"""
        self.state = False
    
    def __repr__(self, state: bool = False) -> None:
        self.state = state

    def __str__(self) -> str:
        return f'Light is {"on" if self.state else "off"}'