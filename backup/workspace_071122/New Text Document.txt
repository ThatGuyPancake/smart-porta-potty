from machine import I2C
import vl6180xb
import time

i2c = I2C(0, I2C.MASTER, baudrate=100000, pins=('P11', 'P10'))

vl61b = vl6180xb.VL6180X(i2c)

while(True):
    print("Getting sensor range...")
    print(vl61b.read_range())
    time.sleep(0.5)