# Create LightSwitch class
class LightSwitch:
    def __init__(self, name, state: bool = False) -> None:
        self.state = state
        self.name = name
    
    def __repr__(self) -> str:
        return f'LightSwitch({self.name!r}): state={self.state}'
    
    def __str__(self) -> str:
        return f'{self.name} light is {"on" if self.state else "off"}'
    
    def turn_on(self) -> None:
        """turn the switch on"""
        self.state = True

    def turn_off(self) -> None:
        """turn the switch off"""
        self.state = False


light = LightSwitch("Kitchen")
print(light)
print(repr(light))