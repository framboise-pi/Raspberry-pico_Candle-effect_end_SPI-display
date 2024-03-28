import time
import board
import pwmio


led1_pwn = pwmio.PWMOut(board.GP0, frequency=5000, duty_cycle=0)
led2_pwn = pwmio.PWMOut(board.GP1, frequency=5000, duty_cycle=0)

while True:
    led1_pwn.duty_cycle = random.randint(0, 65535)
    led2_pwn.duty_cycle = random.randint(0, 65535)
    time.sleep(.1)
