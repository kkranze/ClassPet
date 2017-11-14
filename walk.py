from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def walkingdog():
    g = green
    y = yellow
    b = blue
    p = pink
    w = white
    r = red
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    p, p, O, O, p, O, p, O,
    O, p, g, g, p, y, y, O,
    O, g, g, g, y, w, y, g,
    O, g, g, g, g, y, y, O,
    O, g, O, g, O, g, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def walkingdog2():
    g = green
    y = yellow
    b = blue
    p = pink
    w = white
    r = red
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    p, p, O, O, p, O, p, O,
    O, p, g, g, p, y, y, O,
    O, g, g, g, y, w, y, g,
    O, g, g, g, g, y, y, O,
    O, O, g, O, g, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo



images = [walkingdog,walkingdog2,]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
