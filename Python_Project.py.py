
from turtle import * # imports the module turtule,
                    #* stands for all, which makes things easier
speed(0) # sets the speed of drawing to 0, which is the fastest
pencolor('white') # sets the color of the pen/lines to white
bgcolor('black') # sets the color of the background/canvas to black

x = 0 # creates a variable x with value 0
up() # lifts up the pen, so no line are drawn

#note fd() means forward, bk() means move back
# rt() or It() means tilt right by a certain angle

rt(45)
fd(90)
rt(135)

down() # stes down the pen, so that turtle can draw
while x < 120; # while the value of x is lesser than 120,
                #continuously do this:
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    
    rt(11.1111)
    x = x+1 # add 1 to the value of x,
            # so that it is closer to 120 after every loop

exitonclick() # When you click, turtle exits.

#Thst's all Try customizing the script! 8)