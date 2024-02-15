# Anastacia Aguirre and Abigail Lopez

import turtle
jack=turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side==2:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)

#Considering that range starts at 0, the conditional says that on the number 2
#side, become blu, but before moving. And since python is interpreted, the last
#color was blue, so it remains blue


for side in range(4):
    jack.forward(100)
    jack.right(90)
    if side==2:
        jack.color("blue")
        
#This code, while similar contents, has the if as the end, after the movement.
#So the turtle color changes after it completes the number 2 side.

#Changing the conditional to side==3 would do the same either  efore or after
#the number 3 side, depending on where the conditional is placed.
