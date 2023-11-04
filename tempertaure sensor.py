import time
import RPi.GPIO as GPIO
from smbus2 import SMBus
from RPLCD import CharLCD
lm235_pin = 17  # GPIO pin for LM235 analog output
adc_max = 1023  # ADC maximum value
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2)
def read_temperature():
    raw_value = 0
    for _ in range(10):
        raw_value += ADC.read(lm235_pin)
    raw_value /= 10
    voltage = (raw_value / adc_max) * 3.3
    temperature = (voltage - 0.5) * 100
    return temperature
try:
    ADC = SMBus(1)
    while True:
        temperature = read_temperature()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(f'Temperature: {temperature:.2f}C')
        time.sleep(2)
        lcd.clear()
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    ADC.close()
    GPIO.cleanup()
    lcd.close(clear=True)
