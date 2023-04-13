import math
import turtle
bob=turtle.Turtle()
def polygon(t,n,length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
#polygon(bob,15,70)
#Below are keyword Arguments
#polygon(bob,n=7,length=70)

#Interface Design
def circle(t,r):
    circumference=2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t,n,length)
#circle(bob,100)
#The Interface of a function is a summary of how it is used:what are the Parameters ?what does the function do?
#and what is the return value? An interface is "clean" if it allows the caller to do what they want without dealing with unnecessary details
def circle(t,r):
    circumference=2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t,n,length)
circle(bob,100)
