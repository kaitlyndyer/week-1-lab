# Create LightSwitch class
class LightSwitch:
    def __init__(self, name: str, state: bool = False) -> None:
        self.name = name
        self.state = state

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name}, state={self.state})'
    
    def __str__(self) -> str:
        return f'{self.name} light is {"on" if self.state else "off"}'
    
    def turn_on(self) -> None:
        """turn on switch"""
        self.state = True
        print(f"{self.name} light turned on")

    def turn_off(self) -> None:
        """turn off switch"""    
        self.state = False
        print(f"{self.name} light turned off")

light = LightSwitch("Kitchen")
print(light)        # Light is off
print(repr(light))  # LightSwitch(state=False)
