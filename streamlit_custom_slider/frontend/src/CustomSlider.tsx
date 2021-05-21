import React, { useEffect, useState } from "react";
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib"
import { Slider } from "baseui/slider";


/**
 * We can use a Typescript interface to destructure the arguments from Python
 * and validate the types of the input
 */
//NO ES NECESARIO 
interface PythonArgs {
  label: string
  minValue?: number
  maxValue?: number
  initialValue: number
}

const CustomSlider = (props: ComponentProps) => {
  /**
   * Destructuring JSON objects is a good habit.
   * This will look for label, minValue and maxValue keys
   * to store them in separate variables.
   */
  //const { label, minValue, maxValue, initialValue } = props.args;
  const {label, minValue, maxValue, initialValue}: PythonArgs = props.args;
  // setValue is used to modify the state with a new Array of numbers
  // Set initial value of state using the initialValue prop
  // This sets state each time the component is mounted
  // so don't forget the key argument on the Python side to not remount every time !
  const [value, setValue] = useState([initialValue]);
  

  useEffect(() => Streamlit.setFrameHeight());

  // Render this React component as a stateless baseui Slider
  // Send data back to Streamlit in onFinalChange event
  return (
    <>
      <h3>{label}</h3>
      <Slider
        value={value}
        onChange={({ value }) => value && setValue(value)}
        onFinalChange={({ value }) => Streamlit.setComponentValue(value)}
        min={minValue}
        max={maxValue}
      />
    </>
  );
};

export default withStreamlitConnection(CustomSlider);

