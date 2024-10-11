import machine
from time import sleep
from picozero import Pot
from pid import PID_Controller

set_potentiometer = Pot(1)
read_potentiometer = Pot(0)
pid = PID_Controller(1, 0, 0, 216)

try:
    while True:
        target_pos = set_potentiometer.value * 216
        current_pos = read_potentiometer.value * 216
        print(f"Target Pos: {target_pos:.2f}    Current Pos: {current_pos:.2f}")
        sleep(0.01)

except KeyboardInterrupt:
    print("Keyboard interrupt")
    machine.reset()




