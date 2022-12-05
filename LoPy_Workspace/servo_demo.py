from machine import PWM
import time

pwm = PWM(0, frequency=50)   #50???
pwm_c = pwm.channel(0, pin='P7', duty_cycle=0.5)

pos = 0
while(True):
    pos += 0.01
    if(pos >= 0.1):
        pos = 0
    pwm_c.duty_cycle(pos) 
    print(pos)
    time.sleep(2)