from sense_hat import SenseHat
from random import choice

sense = SenseHat()

red = (255, 0, 0)
white = (255,255,255)
answers = ["Not likely","Chances are slim","Maybe","Quite possibly","Certainly"]

try:
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1 or y > 1 or z > 1:
            sense.show_message(choice(answers), text_colour=red, back_colour=white, scroll_speed=0.05)
        else:
            sense.clear()
except KeyboardInterrupt:
    sense.clear()
