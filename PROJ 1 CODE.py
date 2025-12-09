from machine import Pin, ADC, PWM
import time

led = PWM(Pin(15))
led2 = PWM(Pin(16))
led2 = PWM(Pin(18))
pent = ADC(27)
led.freq(1000)
led2.freq(1000)
led3.freq(1000)

button = Pin(14, Pin.IN, Pin.PULL_UP) # declaring button to be a pin
# attached to pin 14 an input and a pull up resistor. dont want a floating wire

while True:
    reading = pent.read_u16()
    print(reading)
    time.sleep(0.1)
    
    if button.value() == 0: # Notice that this is double = this means =? instead of assignment
        print("button pressed")
        led.duty_u16(reading)
        led2.duty_u16(reading)
        led3.duty_u16(reading)

        time.sleep(0.1)
    else:
        led.duty_u16(0)
        led2.duty_u16(0)
        led3.duty_u16(0)
