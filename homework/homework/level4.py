from turtle import *

#drawing a castle

#step 1: draw a square

begin_fill()
width(5)
speed(10)
shape("turtle")
color("light blue")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
begin_fill()
forward(70)
color("blue")
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

color("light green")
begin_fill()
right(150) 
forward(200)
left(120)
forward(200)
end_fill()
#end of roof 

#drawing second building
begin_fill()
color("light pink")
pendown()
right(60)
forward(200)

pendown()
left(90)
forward(200)

left(90)
forward(200)
end_fill()


#end of second building

#drawing third building

begin_fill()

forward(400)
penup()

left(60)
pendown()
right(60)

color("light pink")
pendown()

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)
end_fill()


#end of drawing third building

#drawing roof of third building
goto(400, 200)
pendown()
right(90)

color("light yellow")
begin_fill()

right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of drawing third buildings roof

#drawing roof of second building
goto(400, 200)
pendown()
right(90)
left(90)
#end of drawing roof











































exitonclick()