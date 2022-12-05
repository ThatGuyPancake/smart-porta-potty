from machine import PWM
import time
from machine import I2C
import vl6180xb

#INIT

#SERVO
pwm = PWM(0, frequency=50)   #50???
servo_position = pwm.channel(0, pin='P7', duty_cycle=0.5)
#LONG RANGE DISTANCE SENSOR
adc = machine.ADC()             # create an ADC object
lr_sensor = adc.channel(pin='P16')   # create an analog pin on P16
#SHORT RANGE DISTANCE SENSOR
i2c = I2C(0, I2C.MASTER, baudrate=100000, pins=('P9', 'P10'))
sr_sensor = vl6180xb.VL6180X(i2c)

#SERVO
# pos_top = 0.1
# pos_side = 0.05

# while(True):
#     servo_position.duty_cycle(pos_top)
#     time.sleep(0.5)
#     servo_position.duty_cycle(pos_side)
#     time.sleep(0.5)

while(True):
    lr = lr_sensor()
    sr = sr_sensor.read_range()
    print('\nLong Distance:  '+ str(lr))
    print('Short Distance: '+ str(sr))
    if(50 < sr < 150):
        servo_position.duty_cycle(0.05 + (sr-50)*0.0005)
    time.sleep(1)
