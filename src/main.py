# from pyb import Timer
from machine import Pin

import pyb, micropython
micropython.alloc_emergency_exception_buf(100)

# using timer 2 at 4 Hz
tim = pyb.Timer(2, freq=4)

# get GPIOs via 'help(machine.Pin.board)' on python repl
# Nucleo144 F767ZI:
#   LED1: Pin.cpu.B0  (green) or 'B0'
#   LED2: Pin.cpu.B7  (blue)  or 'B7'
#   LED3: Pin.cpu.B14 (red)   or 'B14'
#   SW:   Pin.cpu.C13 (blue user button) or 'C13'
# Nucleo64 WB55:
#   LED1: Pin.cpu.B5  (blue)  or 'B5'
#   LED2: Pin.cpu.B0  (green) or 'B0'
#   LED3: Pin.cpu.B1  (red)   or 'B1'
#   SW:   Pin.cpu.C4  (user button SW1) or 'C4'
led = Pin('B7', mode=Pin.OUT) # enable B7 as output to drive the LED

def isr_timer(timer):           # we will receive the timer object when being called
    global led
    led.value(not led.value())  # toggle the LED

# tim.irq(handler=isr_timer, trigger=Timer.TIMEOUT) # create the interrupt

tim.callback(isr_timer)

