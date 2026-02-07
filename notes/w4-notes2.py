"""
MAPPING PROTOCOL
----------------
objects that support:
- key-based lookup (dict)
- iteration, membership testing (in), len()

to be used as:
- dict keys
- set members
- object MUST be hashable
"""

# ==============================================
# COMPARISON OPERATORS
# ==============================================
"""
operator overloading lets classes define:
- equality (==)
- ordering (<, >, <=, >=)

Methods:
==  __eq__
!=  __ne__
<   __lt__
>   __gt__
<=  __le__
>=  __ge__
"""

# ==============================================
# EQUALITY vs IDENTITY
# ==============================================
"""
== equaltiy -> same value? -> calls __eq__
is identity -> same object in memory? -> compares id()

default (user-defined classes):
- == behaves like is
- identity comparison until __eq__ is overridden
"""


# ==============================================
# DEFINING EQUALITY: __eq__
# ==============================================
class LightSwitch:
    def _init__(self, name: str):
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LightSwitch):
            return NotImplemented
        return self.name == other.name


"""
__eq__ rules:
- return True / False / NotImplemented
- NotImplemented for unsupported types
"""
