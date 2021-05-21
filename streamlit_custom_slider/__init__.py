import os
import streamlit.components.v1 as components
from typing import Tuple


# Create a function _component_func which will call the frontend component when run
_component_func = components.declare_component(
    "custom_slider",
    url="http://localhost:3001",  # Fetch frontend component from local webserver
)


# Define a public function for the package, 
# which wraps the caller to the frontend code
# Add label, min and max as input arguments of the wrapped function
# Pass them to _component_func which will deliver them to the frontend part


# Define a value argument in the wrapper function, pass it into `initialValue`
# Pass min and max from Python to the frontend component
#Nombres de las variables en frontend: minValue (React), min_value (Streamlit)
def st_custom_slider(label: str, min_value: int, max_value: int, value: int = 0, key=None) -> int:
    component_value = _component_func(label=label, minValue=min_value, maxValue=max_value, initialValue=[value], key=key, default=[value])
    return component_value[0]

# Define a new public method which takes as input a tuple of numbers to define a range slider, and returns back a tuple.
#def st_range_slider(label: str, min_value: int, max_value: int, value: Tuple[int, int], key=None) -> Tuple[int, int]:
#    component_value = _component_func(label=label, minValue=min_value, maxValue=max_value, initialValue=value, key=key, default=value)
#    return tuple(component_value)