from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
all_turtle = []
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="user_bet", prompt="whitch turtel will win the race,chose color: ")
color = ["red","green", "blue", "orange", "yellow","purple"]
y_cordinate = [-150, -100, -50, 0, 50, 100]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=y_cordinate[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("you win")
            else:
                print("you lose")
        random_distance = random.randint(5, 15)
        turtle.forward(random_distance)

screen.exitonclick()