from turtle import *

#we want to paint a house

#step 1: draw a square
width(7)
speed(4)
color("pink")
shape("turtle")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("light green")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()


color("light blue")
begin_fill()
right(150) 
forward(200)
left(120)
forward(200)
end_fill()
#end of roof 

#drawing windows 
penup()
goto(10, 120)
pendown()

right(150)
color("yellow")
begin_fill()
forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)
end_fill()

goto(140, 120)
pendown()

begin_fill()
forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)
end_fill()


exitonclick()  