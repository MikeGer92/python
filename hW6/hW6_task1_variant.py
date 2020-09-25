from turtle import *
import time
t = Turtle()
t.screen.setup(400, 400)
def circle(x,y,r,color):
    t.up()
    t.goto(x,y-r)
    t.down()
    t.fillcolor("black")
    if (color==1):
     t.fillcolor("red")
    if (color==2):
     t.fillcolor("yellow")
    if (color==3):
     t.fillcolor("green")
    t.begin_fill()
    t.circle(r,360)
    t.end_fill()
circle(50,150,25,1)
circle(50,100,25,0)
circle(50,50,25,0)
time.sleep(7)
circle(50,150,25,1)
circle(50,100,25,2)
circle(50,50,25,0)
time.sleep(3)
circle(50,150,25,0)
circle(50,100,25,0)
circle(50,50,25,3)
time.sleep(10)
circle(50,150,25,0)
circle(50,100,25,2)
circle(50,50,25,0)
time.sleep(3)
circle(50,150,25,1)
circle(50,100,25,0)
circle(50,50,25,0)
time.sleep(7)



# t.screen.exitonclick()
# t.screen.mainloop()


