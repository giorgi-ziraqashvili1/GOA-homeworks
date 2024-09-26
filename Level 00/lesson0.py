from turtle import *

#we want to paint a house

#step 1 draw a square 
speed(30)
width(7)
color("green")
begin_fill()
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

forward(70)
color("pink")
begin_fill()
left(90)
forward (120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()  
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("green")
left(30)
forward(40)
left(90)

color("blue")
forward(55)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
left(180)
forward(30)
left(90)
forward(50)
right(90)
forward(30)
right(90)
forward(25)
right(90)
forward(60)

penup()  
goto(200, 200)
pendown()

color("green")
left(180)
forward(40)
color("blue")
right(90)
forward(55)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
left(180)
forward(30)
right(90)
forward(50)
right(90)
left(180)
forward(30)
left(90)
forward(25)
left(90)
forward(60)

color("green")
penup()  
goto(200, 200)
pendown()

exitonclick()