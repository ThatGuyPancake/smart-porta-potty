from machine import Pin
import time
import platform
print(platform.python_version())

pin = Pin('P13', mode=Pin.IN)
print("Hello World")

# while True:         
#     pin_int = pin()
#     pin_int_size = sys.getsizeof(pin_int)

#     print(pin_int)
#     print(pin_int_size)

#     time.sleep(1)