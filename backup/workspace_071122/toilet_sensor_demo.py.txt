import machine
import time

adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16

while(True):
    val = apin()                    # read an analog value
    print(val)
    time.sleep(1)