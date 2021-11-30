import turtle as trtl
import random as rand

# create turtles
red = trtl.Turtle()
red.pencolor("red")
red.fillcolor("red")
red.shape("square")
red.turtlesize(10)
red.penup()
red.goto(-100,100)
blue = trtl.Turtle()
blue.pencolor("blue")
blue.fillcolor("blue")
blue.shape("square")
blue.turtlesize(10)
blue.penup()
blue.goto(100,100)
yellow = trtl.Turtle()
yellow.pencolor("yellow")
yellow.fillcolor("yellow")
yellow.shape("square")
yellow.turtlesize(10)
yellow.penup()
yellow.goto(-100,-100)
green = trtl.Turtle()
green.pencolor("green")
green.fillcolor("green")
green.shape("square")
green.turtlesize(10)
green.penup()
green.goto(100,-100)
font_setup = ("Arial", 20, "normal")
start = trtl.Turtle()
start.penup()
start.turtlesize(3)
start.goto(-50,200)
start.write("Start (click the turtle to start)", font=font_setup)

# lists
colors = ["red", "blue", "yellow", "green"]
pattern = []
human_pattern = []

# functions
def start_game(x, y):
    start.clear()
    start.hideturtle()
    level = 1
    start.write("Level: " + str(level), font=font_setup)
    round()
def round():
    color = rand.randint(0, len(colors)-1)
    print(color)
    if color == 0:
        i = 0
        if i
        red.hideturtle()
        red.showturtle()
    if color == 1:
        blue.hideturtle()
        blue.showturtle()
    if color == 2:
        yellow.hideturtle()
        yellow.showturtle()
    if color == 3:
        green.hideturtle()
        green.showturtle()

start.onclick(start_game)

wn = trtl.Screen()
wn.mainloop()