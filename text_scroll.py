from sense_hat import SenseHat
sense = SenseHat()

red = (255, 0, 0)
white = (255, 255, 255)
message = "Hello World"
try:
    while True:
      sense.show_message(message, text_colour=red, back_colour=white, scroll_speed=0.1)
except KeyboardInterrupt:
    sense.clear()
