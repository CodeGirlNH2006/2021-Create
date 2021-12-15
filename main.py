import turtle as trtl
import random as rand
import time
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
pattern = []
human_pattern = []
colors = ["red", "blue", "yellow", "green"]

# functions
def start_game(x, y):
    start.clear()
    start.hideturtle()
    global level
    level = 1
    while level <= 10:
        round()
    if level == 11:
        start.clear()
    start.goto(-175, -20)
    start.write("You completed all the levels!", font=font_setup)
    time.sleep(1)
    end_game()
def round():
    global level
    start.write("Level: " + str(level), font=font_setup)
    time.sleep(1)
    for x in pattern:
        if x == ['red']:
            blink(red)
        elif x == ['blue']:
            blink(blue)
        elif x == ['yellow']:
            blink(yellow)
        else:
            blink(green)
    color = rand.sample(colors, 1)
    if color == ['red']:
        blink(red)
    elif color == ['blue']:
        blink(blue)
    elif color == ['yellow']:
        blink(yellow)
    else:
        blink(green)
    pattern.append(color)
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
def blink(button):
    button.hideturtle()
    time.sleep(.25)
    button.showturtle()
    time.sleep(.25)
def add_red(x, y):
    blink(red)
    human_pattern.append(['red'])
def add_blue(x, y):
    blink(blue)
    human_pattern.append(['blue'])
def add_yellow(x, y):
    blink(yellow)
    human_pattern.append(['yellow'])
def add_green(x, y):
    blink(green)
    human_pattern.append(['green'])
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