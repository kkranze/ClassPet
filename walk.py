from sense_hat import SenseHat
import time


s = SenseHat()


def animate(sense,slides,timetosleep):
	for slide in slides:
		sense.set_pixels(slide)
		time.sleep(timetosleep)




green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
tan = (210,180,140)
brown = (210,105,30)
gold = (255,215,0)
orange = (255,165,0)

O = orange
G = gold
B = brown
t = tan
g = green
y = yellow
b = blue
p = pink
w = white
r = red
o = nothing

pet = [
    o, o, o, g, g, g, g, o,
    o, G, G, G, b, G, b, o,
    o, o, g, w, w, g, g, g,
    o, B, g, w, w, w, g, g,
    B, B, g, B, B, B, o, o,
    B, g, g, y, G, y, g, o,
    o, B, g, G, G, G, o, o,
    o, o, g, o, o, g, o, o,
    ]

eat = [
    [o, o, o, t, t, o, o, o,
    o, o, t, y, r, t, o, o,
    o, t, r, y, y, y, t, o,
    t, y, y, r, y, r, y, t,
    t, y, r, y, y, y, y, t,
    o, t, y, y, r, y, t, o,
    o, o, t, y, y, t, o, o,
    o, o, o, t, t, o, o, o,
    ],[
    o, o, o, t, t, o, o, o,
    o, o, o, y, r, t, o, o,
    o, o, o, y, y, y, t, o,
    o, o, o, r, y, r, y, t,
    t, y, r, y, y, y, y, t,
    o, t, y, y, r, y, t, o,
    o, o, t, y, y, t, o, o,
    o, o, o, t, t, o, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    t, y, r, y, y, y, y, t,
    o, t, y, y, r, y, t, o,
    o, o, t, y, y, t, o, o,
    o, o, o, t, t, o, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, y, y, y, t,
    o, o, o, o, r, y, t, o,
    o, o, o, o, y, t, o, o,
    o, o, o, o, t, o, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ],[
    o, o, o, g, g, g, g, o,
    o, G, G, G, b, G, b, o,
    o, o, g, w, w, g, g, g,
    o, B, g, w, w, w, g, g,
    B, B, g, B, B, B, B, B,
    B, g, g, y, G, y, y, y,
    o, B, g, G, G, G, G, o,
    o, o, g, o, o, g, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, w, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, w, o, o, o,
    o, o, o, w, r, w, o, o,
    o, o, o, o, w, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, r, w, r, o, o,
    o, o, o, w, r, w, o, o,
    o, o, o, r, w, r, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, r, w, w, w, r, o,
    o, o, w, r, w, r, w, o,
    o, o, w, r, w, r, w, o,
    o, o, w, r, w, r, w, o,
    o, o, r, w, w, w, r, o,
    o, o, o, o, o, o, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, w, o, o, o,
    o, o, r, w, w, w, r, o,
    o, o, w, r, w, r, w, o,
    o, w, w, r, w, r, w, w,
    o, o, w, r, w, r, w, o,
    o, o, r, w, w, w, r, o,
    o, o, o, o, w, o, o, o,
    ],[
    w, w, w, y, y, y, w, w,
    w, w, y, y, O, y, y, w,
    o, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    w, B, B, B, B, B, B, B,
    w, w, y, y, O, y, y, w,
    w, w, w, y, y, y, w, w,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, r, w, w, w, r, o,
    o, o, w, r, w, r, w, o,
    o, o, w, r, w, r, w, o,
    o, o, w, r, w, r, w, o,
    o, o, r, w, w, w, r, o,
    o, o, o, o, o, o, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, r, w, r, o, o,
    o, o, o, w, r, w, o, o,
    o, o, o, r, w, r, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, w, o, o, o,
    o, o, o, w, r, w, o, o,
    o, o, o, o, w, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ],[
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, w, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ]
]
while True: 
	s.set_pixels(pet)
	x, y, z = s.get_accelerometer_raw().values()
	if(x > 1 or y > 1 or z > 1):
		animate(s,eat,0.5)
	time.sleep(1)

