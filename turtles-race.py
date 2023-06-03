import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(500, 400)
user = screen.textinput("make a bet", "Enter a color: ")
colors = "red", "blue", "yellow", "green", "pink", "black"
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[index])
    all_turtles.append(new_turtle)
race_on = True
while race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.ycor() == 130:
             race_on = False
screen.bye()
