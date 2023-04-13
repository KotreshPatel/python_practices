#The Turtle Module
import turtle
import math
bob = turtle.Turtle()
print(bob)
#bob.fd(100)
#bob.lt(90)
#bob.fd(100)
#turtle.mainloop()
#fd - forward,bd- backward,lt - left turn, rt- right turn , pu - penup , pd - pen down

#encapsulation (Wrapping a Piece of code in a function is called Encapsulation)
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
#square(bob)
alice = Turtle()
#square(alice)

#Generalization ( adding a parameter to a function is called Generalization bz it makes the function more general)
def square2(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square2(alice,100)
