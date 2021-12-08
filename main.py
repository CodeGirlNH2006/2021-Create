import turtle as trtl
import random as rand
import time as time
import sys
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
font_setup = ("Comic Sans MS", 20, "italic")
start = trtl.Turtle()
start.penup()
start.turtlesize(3)
start.goto(-50,200)
start.write("Start (click the turtle to start)", font=font_setup)

# lists
colors = ["red", "blue", "yellow", "green"]
pattern = []
human_pattern = []
pattern_add = []

# functions
def start_game(x, y):
    start.clear()
    start.hideturtle()
    global level
    level = 1
    while level <= 10:
        round()
    start.goto(-70, -20)
    start.write("Congrats! You completed all the levels!", font=font_setup)
    end_game()
def round():
    global level
    start.write("Level: " + str(level), font=font_setup)
    time.sleep(1)
    for x in pattern:
        if x == ['red']:
            red.hideturtle()
            time.sleep(.25)
            red.showturtle()
            time.sleep(.25)
        if x == ['blue']:
            blue.hideturtle()
            time.sleep(.25)
            blue.showturtle()
            time.sleep(.25)
        if x == ['yellow']:
            yellow.hideturtle()
            time.sleep(.25)
            yellow.showturtle()
            time.sleep(.25)
        if x == ['green']:
            green.hideturtle()
            time.sleep(.25)
            green.showturtle()
            time.sleep(.25)
    color = rand.sample(colors, 1)
    if color == ['red']:
        red.hideturtle()
        time.sleep(.25)
        red.showturtle()
    if color == ['blue']:
        blue.hideturtle()
        time.sleep(.25)
        blue.showturtle()
    if color == ['yellow']:
        yellow.hideturtle()
        time.sleep(.25)
        yellow.showturtle()
    if color == ['green']:
        green.hideturtle()
        time.sleep(.25)
        green.showturtle()
    pattern.append(color)
    print(pattern)
    while len(pattern) != len(human_pattern):
        human_round()
    if human_pattern == pattern:
        level += 1
        start.clear()
        start.write("Level: " + str(level), font=font_setup)
        human_pattern.clear()

    else:
        start.goto(-70,-20)
        start.write("Game Over", font=font_setup)
        end_game()
def add_red(x, y):
    red.hideturtle()
    time.sleep(.25)
    red.showturtle()
    human_pattern.append(['red'])
    print(human_pattern)
def add_blue(x, y):
    blue.hideturtle()
    time.sleep(.25)
    blue.showturtle()
    human_pattern.append(['blue'])
    print(human_pattern)
def add_yellow(x, y):
    yellow.hideturtle()
    time.sleep(.25)
    yellow.showturtle()
    human_pattern.append(['yellow'])
    print(human_pattern)
def add_green(x, y):
    green.hideturtle()
    time.sleep(.25)
    green.showturtle()
    human_pattern.append(['green'])
    print(human_pattern)
def human_round():
    red.onclick(add_red)
    blue.onclick(add_blue)
    yellow.onclick(add_yellow)
    green.onclick(add_green)
def end_game():
    time.sleep(.5)
    sys.exit()
start.onclick(start_game)
wn = trtl.Screen()
wn.mainloop()