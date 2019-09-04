import turtle         #title('Racing Game Created By Janu Nayak')
wn= turtle.Screen()
wn.bgcolor('yellow')
from turtle import*
from random import*
speed(10)
penup()
goto(-240,240)  #Initial position of track
z=100
y=25

for x in range(15):  #Iterate to draw fifteen lines
    write(x)         #Mark distance at the top of lines
    right(90)        #Change direction facing downwards
    forward(10)      #Move 10 steps ahead
    pendown()        #Open pen to draw 
    forward(150)     #Move 150 steps ahead
    penup()          #Close pen
    backward(160)    #Move 160 steps backward
    left(90)         #Change the direction towards left
    forward(y)       #Move by y direction
    
t1= Turtle()         #Creating Turtle object t1
t1.penup()           #Pen up to place Turtle at x y position
t1.goto(-260,200)    #This is for x and y values
t1.color('red')      #Change the color of Turtle
t1.shape('circle')   #Give proper shape to it

t2= Turtle()         #Creating Turtle object t2
t2.penup()           #Pen up to place Turtle at x y position
t2.goto(-260,150)    #This is for x and y values
t2.color('Green')    #Change the color of Turtle
t2.shape('circle')    #Give proper shape to it

t3= Turtle()
t3.penup()
t3.goto(-260,180)
t3.color('white')
t3.shape('circle')

for m in range(50):        #from random import to perform the above turtle operation
    t1.forward(randint(1,15))
    t2.forward(randint(1,15))
    t3.forward(randint(1,15))

