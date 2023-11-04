# temperature-sensor
In this project me and my team members used a raspberry pi with lm35 sensor and lcd to display the current temperature.

ABSTRACT:
This project involves connecting an LM235 temperature sensor and a 2x16 LCD display to a Raspberry Pi. The LM235 sensor will measure the ambient temperature and provide an analog voltage output, which will be read by the Raspberry Pi's analog-to-digital converter (ADC). The Raspberry Pi will then process this data and display the temperature on the LCD screen. This setup can be used for various applications, including environmental monitoring and home automation.

ALGORITHM:
1.Initialize the necessary GPIO pins and I2C for the Raspberry Pi.
2.Set up the LM235 temperature sensor to provide an analog output.
3.Create a loop to continuously read the analog value from the LM235 sensor using the Raspberry Pi's ADC.
4.Convert the analog reading to temperature in degrees Celsius using the LM235's characteristics.
5.Update the LCD display with the current temperature reading.
6.Repeat the above steps to provide real-time temperature monitoring.
7.Handle any exceptions or interruptions gracefully to ensure proper program termination.
