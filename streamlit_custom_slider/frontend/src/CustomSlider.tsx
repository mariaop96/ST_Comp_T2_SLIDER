import React, { useEffect, useState } from "react";
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib"
import { Slider } from "baseui/slider";

const CustomSlider = (props: ComponentProps) => {
  /**
   * Destructuring JSON objects is a good habit.
   * This will look for label, minValue and maxValue keys
   * to store them in separate variables.
   */
  const { label, minValue, maxValue } = props.args;
  // Define an internal state for your component, called "value" with an initial value of [10]
  // setValue is used to modify the state with a new Array of numbers
  const [value, setValue] = useState([10]);

  useEffect(() => Streamlit.setFrameHeight());

  // Render this React component as a stateless baseui Slider
  return (
    <>
      <h3>{label}</h3>
      <Slider
        value={value}
        onChange={({ value }) => value && setValue(value)}
        onFinalChange={({ value }) => console.log(value)}
        min={minValue}
        max={maxValue}
      />
    </>
  );
};

export default withStreamlitConnection(CustomSlider);

