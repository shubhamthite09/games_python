import turtle as t
import random
t.colormode(255)
tmmey = t.Turtle()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
for _ in range(50):
    tmmey.color(random_color())
    tmmey.pensize(3)
    tmmey.circle(150)
    current = tmmey.heading()
    tmmey.setheading(current + 30)
    tmmey.circle(100)
    tmmey.speed("fastest")





