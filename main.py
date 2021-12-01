import turtle as trtl
import random as rand
import time as time

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
    global level
    level = 1
    start.write("Level: " + str(level), font=font_setup)
    round()
def round():
    time.sleep(1)
    color = rand.randint(0, len(colors)-1)
    print(color)
    if color == 0:
        red.hideturtle()
        time.sleep(.25)
        red.showturtle()
    if color == 1:
        blue.hideturtle()
        time.sleep(.25)
        blue.showturtle()
    if color == 2:
        yellow.hideturtle()
        time.sleep(.25)
        yellow.showturtle()
    if color == 3:
        green.hideturtle()
        time.sleep(.25)
        green.showturtle()
    pattern.append(color)
    print(pattern)
    human_round()
def add_red(x, y):
    red.hideturtle()
    time.sleep(.25)
    red.showturtle()
    human_pattern.append(0)
    print(human_pattern)
def add_blue(x, y):
    blue.hideturtle()
    time.sleep(.25)
    blue.showturtle()
    human_pattern.append(1)
    print(human_pattern)
def add_yellow(x, y):
    yellow.hideturtle()
    time.sleep(.25)
    yellow.showturtle()
    human_pattern.append(2)
    print(human_pattern)
def add_green(x, y):
    green.hideturtle()
    time.sleep(.25)
    green.showturtle()
    human_pattern.append(3)
    print(human_pattern)
def human_round():
    red.onclick(add_red)
    blue.onclick(add_blue)
    yellow.onclick(add_yellow)
    green.onclick(add_green)
    remaining_taps = len(pattern) - len(human_pattern)
    if remaining_taps == 0:
        if human_pattern == pattern:
            start.clear()
            start.write("Nice")
            level = 1
            level += 1
            start.showturtle()
            start.clear()
            start.write("Level: " + str(level))
        else:
            print("Game over")

start.onclick(start_game)

wn = trtl.Screen()
wn.mainloop()