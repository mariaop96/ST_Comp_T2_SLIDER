import streamlit as st
from streamlit_custom_slider import st_custom_slider

st.title("Testing Streamlit custom components")

# Add Streamlit widgets to define the parameters for the CustomSlider
#label = st.sidebar.text_input('Label', 'Hello world')
#min_value, max_value = st.sidebar.slider("Range slider", 0, 100, (0, 50))


# Store and display the return value of your custom component
# Pass the parameters inside the wrapper function

# Lift key parameter up to the wrapper function
#v1 = st_custom_slider(label=label, min_value=min_value, max_value=max_value, key="slider1")
#st.write(v1)
#v2 = st_custom_slider(label=label, min_value=min_value, max_value=max_value, key="slider2")
#st.write(v2)



# Streamlit native slider
v = st.slider("Hello world", 0, 100, 50)
st.write(v)

# Streamlit custom slider
v_custom = st_custom_slider('Hello world', 0, 100, 50, key="slider1")
#EN v_custom ahora recibes el valor que se ha seleccionado en el slider!!!
if v_custom==25:
	st.write("VALOR 25")