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
    global score
    score = 0
    while score < 5:
        round()
def round():
    global level
    start.write("Level: " + str(level), font=font_setup)
    time.sleep(1)
    amount = 1
    color = rand.randint(range(str(0, len(colors)-1)), amount)
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
    while len(pattern) != len(human_pattern):
        human_round()
    if human_pattern == pattern:
        level += 1
        global score
        score += 1
        start.clear()
        start.write("Level: " + str(level), font=font_setup)
    else:
        start.clear()
        start.write("Game Over")
    amount += 1
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
start.onclick(start_game)
wn = trtl.Screen()
wn.mainloop()