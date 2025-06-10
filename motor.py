from time import sleep
import RPi.GPIO as gpio

dir_pin = 20
pulse_pin = 21
ena_pin = 16
cw_dir = 1
ccw_dir = 0

gpio.setmode(gpio.BCM)
gpio.setup(dir_pin, gpio.OUT)
gpio.setup(pulse_pin, gpio.OUT)
gpio.setup(ena_pin, gpio.OUT)
gpio.output(dir_pin, cw_dir)

# LOW means on -- HIGH means off
# gpio.output(ena_pin, gpio.LOW)

steps_taken = 0
max_steps = 600
reset_steps = 0

saved_ratios = {
    "The Bear": 70,
    "Netflix": 150,
    "Widescreen": 330,
}


def reset(steps_currently: int) -> int:
    if steps_currently <= reset_steps:
        return steps_currently  # already at reset

    gpio.output(ena_pin, gpio.LOW)  # enable motor
    gpio.output(dir_pin, ccw_dir)  # set direction

    while steps_currently > reset_steps - 6:
        gpio.output(pulse_pin, gpio.HIGH)
        sleep(0.01)
        gpio.output(pulse_pin, gpio.LOW)
        sleep(0.001)

        steps_currently -= 1

    gpio.output(ena_pin, gpio.HIGH)  # disable motor

    steps_currently = 0
    return steps_currently


def position(aspect_ratio: int, steps_currently: int) -> int:

    if steps_currently == aspect_ratio:
        return steps_currently  # already at position

    gpio.output(ena_pin, gpio.LOW)

    if steps_currently < aspect_ratio:
        gpio.output(dir_pin, cw_dir)
        increment = True  # going up
    else:
        gpio.output(dir_pin, ccw_dir)
        increment = False  # going down
        steps_currently += 10
    

    while steps_currently != aspect_ratio:
        gpio.output(pulse_pin, gpio.HIGH)
        sleep(0.01)
        gpio.output(pulse_pin, gpio.LOW)
        sleep(0.001)

        if increment:
            steps_currently += 1
        else:
            steps_currently -= 1

    gpio.output(ena_pin, gpio.HIGH)

    return steps_currently


def manual(direction: str, steps_to_take: int, steps_currently: int) -> int:
    gpio.output(ena_pin, gpio.LOW)

    if direction == "down":
        gpio.output(dir_pin, ccw_dir)
        #steps_to_take += 6
    else:
        gpio.output(dir_pin, cw_dir)


    while steps_to_take > 0:
        if direction == "down" and steps_currently > reset_steps:
            gpio.output(pulse_pin, gpio.HIGH)
            sleep(0.01)
            gpio.output(pulse_pin, gpio.LOW)
            sleep(0.001)

            steps_currently -= 1
            steps_to_take -= 1

        elif direction == "up" and steps_currently < max_steps:
            gpio.output(pulse_pin, gpio.HIGH)
            sleep(0.01)
            gpio.output(pulse_pin, gpio.LOW)
            sleep(0.001)

            steps_currently += 1
            steps_to_take -= 1

        else:
            break

    gpio.output(ena_pin, gpio.HIGH)

    return steps_currently
