import os
import streamlit.components.v1 as components


# Create a function _component_func which will call the frontend component when run
_component_func = components.declare_component(
    "custom_slider",
    url="http://localhost:3001",  # Fetch frontend component from local webserver
)


# Define a public function for the package, 
# which wraps the caller to the frontend code
# Add label, min and max as input arguments of the wrapped function
# Pass them to _component_func which will deliver them to the frontend part

# Lift key parameter up to the wrapper function
def st_custom_slider(label: str, min_value: int, max_value: int, key=None):
	# Pass min and max from Python to the frontend component
	#Nombres de las variables en frontend: minValue (React), min_value (Streamlit)
    component_value = _component_func(label=label, minValue=min_value, maxValue=max_value, key=key)
    return component_value