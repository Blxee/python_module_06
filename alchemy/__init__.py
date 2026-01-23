"""Controls package level access."""

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

# import two functions from the elements submodule relatively.
from .elements import create_fire, create_water

# expose only these two functions
__all__ = ["create_fire", "create_water"]
