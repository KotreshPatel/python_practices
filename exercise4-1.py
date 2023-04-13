"""This Module contains a code example related to Think Python,2nd edition
by allen downey"""

from _future_import print_function,division
import Turtle
from polygon import arc

def polyline(t,n,length,angle):
    for in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,n,length):
    angle=360.0/n
    polyline(t,n,length,angle)

def arc(t,r,angle):
    arc_length=2*math.pi*r*angle /360
    n = int(arc_length/3)+1
    step_length = arc_length/n
    step_angle=float(angle)/n
    polyline(t,n,step_length,step_angle)

def petal(t,r,angle):
    """Draws a petal using two arcs.
    t:Turtle r: radius of the arcs
    angle:angle(degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t,r,angle)
        t.lt(180-angle)

def flower(t,b,r,angle):
    """Draws a flower with a Petals.
    t:turtle
    n:number of Petals
    r:radius of the arcs
    angle:angle(degrees) that subtends the arcs """

    for i in range(n):
        petals(t,r,angle)
        t.lt(360.0/n)

def move(t,length):
    """Move Turtle(t) forward(length) units without leaving a trail.
    Leaves the pen down"""
    t.pu()
    t.fd(length)
    t.pd()

bob=turtle.turtle()

#draw a sequence of three flowers,as shown in the book.
move(bob,-100)
flower(bob,10,60.0,60.0)

move(bob,100)
flower(bob,20,40.0,80.0)

move(bob,100)
flower(bob,20,140.0,20.0)

#bob.hideturtle()
turtle.mainloop()
