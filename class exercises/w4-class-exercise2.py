# CLASS EXERCISES

# ==================================
# MAKING LIGHTSWITCHES WORK IN SETS
# ==================================
class LightSwitch:
    def __init__(self, name: str):
        self.name = name
        self.state = False

    def turn_on(self) -> None:
        self.state = True

    def __repr__(self) -> str:
        return f'LightSwitch({self.name!r})'
    
    def __eq__(self, other):
        if not isinstance(other, LightSwitch):
            return False
        return self.name == other.name
        
    def __hash__(self) -> int:
        return hash(self.name)
    
class Room:
    def __init__(self, name: str):
        self.name = name
        self.lights: set[LightSwitch] = set()

    def add_light(self, light: LightSwitch) -> None:
        self.lights.add(light) # Changed from append to add

    def activate_lights(self) -> None:
        for light in self.lights:
            light.turn_on()


# Test implementation:
kitchen = Room("Kitchen")
kitchen.add_light(LightSwitch("Main"))
kitchen.add_light(LightSwitch("Main"))
# Duplicate - should not be added
kitchen.add_light(LightSwitch("Counter"))

print(len(kitchen.lights))      # Should print 2 not 3

# ==================================
# ORDERING EVENTS BY TIME
# ==================================
from datetime import datetime

class Event:
    def __init__(self, name: str, scheduled_time: datetime):
        self.name = name
        self.scheduled_time = scheduled_time

    def __repr__(self) -> str:
        return f'Event({self.name!r}, {self.scheduled_time.strftime("%H:%M")})'
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Event):
            return False
        return self.name == other.name and self.scheduled_time == other.scheduled_time
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Event):
            return NotImplemented
        return self.scheduled_time < other.scheduled_time
    
    def __hash__(self) -> int:
        return hash((self.namem, self.scheduled_time))


# Test your implementation:
events = [
    Event('Lunch Break', datetime(2026, 1, 15, 12, 0)),
    Event('iPDI', datetime(2026, 1, 15, 9, 0)),
    Event('PDI1', datetime(2026, 1, 15, 14, 30)),
    Event('Meeting', datetime(2026, 1, 15, 10, 0)),
    Event('Planning', datetime(2026, 1, 15, 10, 0))
]

events.sort()
for event in events:
    print(event)
