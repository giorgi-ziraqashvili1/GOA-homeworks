from turtle import * 
"""turtle-ში დახაზეთ სასახლე, კოშკზე უნდა იყოს GOA-ს დროშა, ჯგუფიდან საუკეთესო დავალების ავტორი გახდება მინი ლიდერი"""

#ვქმნით Tower's

#კედლები



speed(500)
width(7)


color("gray")
begin_fill()

penup()
goto(-450, -395)
pendown()


forward(900)

left(90)

forward(300)

left(90)

forward(300)

right(90)

forward(300)

left(90)

forward(300)

left(90)

forward(300)

right(90)

forward(300)

left(90)

forward(300)


end_fill()


#სახურავი main

penup()
goto(150, 205)
pendown()

color("black")

begin_fill()

right(90)
forward(300)

right(90)

right(45)

forward(215)

right(90)

forward(215)

end_fill()

#სახურავი rigth
penup()
goto(155, -95)
pendown()
color("black")
begin_fill()
left(45)

forward(295)

left(90)

left(45)

forward(215)

left(90)

forward(215)

left(135)

forward(295)

end_fill()

#სახურავი left

penup()
goto(-450, -95)
pendown()

color("black")
begin_fill()
left(45)

forward(215)

right(90)

forward(215)

right(135)

forward(300)
end_fill()

#კარების გაკეტება

#კარი Main


penup()
goto(-450, -395)
pendown()

color("gray")
left(180)
forward(400)

color("brown")
begin_fill()

left(90)

forward(150)

right(90)

forward(100)

right(90)

forward(150)

right(90)

forward(100)

end_fill()

penup()
color("black")
goto(-40, -345)
pendown()
right(180)

forward(15)

penup()
goto(-50, -240)
pendown()

begin_fill()

left(45)

forward(75)

right(90)

forward(75)

right(135)

forward(110)
end_fill()


#კარი right

penup()
goto(250, -395)
pendown()
color("brown")
begin_fill()
right(90)

forward(125)

right(90)

forward(75)

right(90)
forward(125)

right(90)
forward(75)

end_fill()

color("black")

penup()
goto(245, -270)
pendown()

begin_fill()
right(180)

left(45)

forward(60)

right(90)

forward(60)

right(135)

forward(80)

end_fill()

penup()
goto(255, -350)
pendown()

right(180)

forward(10)

# კარი left

penup()
goto(-350, -395)
pendown()
color("brown")

begin_fill()
left(90)

forward(125)

right(90)

forward(75)
right(90)
forward(125)

right(90)

forward(75)

end_fill()


penup()
goto(-355, -270)
pendown()

color("black")
begin_fill()
right(180)

left(45)

forward(60)

right(90)

forward(60)

right(135)

forward(80)

end_fill()


penup()
goto(-345, -345)
pendown()

right(180)

forward(10)

#ფანჯარა 1


penup()
goto(-345, -215)
pendown()

color("aqua")

begin_fill()
forward(65)

left(90)

forward(90)

left(90)

forward(65)

left(90)

forward(90)

end_fill()


penup()
goto(-345, -175)
pendown()

color("black")

left(90)

forward(65)


penup()
goto(-315, -215)
pendown()

left(90)

forward(90)

penup()
goto(-350, -220)
pendown()

color("black")


forward(95)

right(90)

forward(70)

right(90)
forward(95)
right(90)
forward(70)


#ფანჯარა 2

penup()
goto(-30, -170)
pendown()

color("aqua")
begin_fill()
right(180)

forward(65)

left(90)

forward(90)

left(90)

forward(65)

left(90)

forward(90)
end_fill()

penup()
goto(-30, -130)
pendown()

color("black")

left(90)

forward(65)

penup()
goto(3, -170)
pendown()

left(90)
forward(90)


penup()
goto(-33, -175)
pendown()

forward(95)

right(90)

forward(70)

right(90)

forward(95)

right(90)

forward(70)


#ფანჯარა 3

penup()
goto(255, -220)
pendown()

color("aqua")
begin_fill()
right(180)

forward(65)

left(90)

forward(90)

left(90)

forward(65)

left(90)

forward(90)
end_fill()

penup()
goto(250, -220)
pendown()

color("black")

right(180)

forward(95)

right(90)

forward(70)

right(90)

forward(95)

right(90)

forward(70)



penup()
goto(250, -175)
pendown()

right(180)

forward(65)


penup()
goto(285, -220)
pendown()

left(90)

forward(90)


#ფანჯარა 4


penup()
goto(-30, 25)
pendown()

color("aqua")
begin_fill()
right(90)
forward(65)
left(90)
forward(90)
left(90)
forward(65)
left(90)
forward(90)
end_fill()

color("black")
penup()
goto(-30, 65)
pendown()

left(90)

forward(65)



penup()
goto(1, 25)
pendown()

left(90)

forward(90)

penup()
goto(-35, 20)
pendown()

forward(95)

right(90)

forward(70)

right(90)

forward(95)

right(90)

forward(70)

#მორჩა კოშკის დიზაინი 2 საათის შემდეგ

#ახლა ვაკეთებთ დროშას რომელზეც გამოსახულია GOA

#დროშა
penup()
goto(210, -30)
pendown()
color("gray")

right(90)

forward(180)

right(90)

forward(5)
color("green")
right(90)
begin_fill()
forward(70)

left(90)

forward(100)

left(90)

forward(70)

left(90)

forward(100)
end_fill()

width(4)
penup()
goto(235, 125)
pendown()
#ასო G
color("black")

forward(20)


left(90)

forward(35)

left(90)

forward(20)

left(90)

forward(15)

left(90)

forward(10)

#ასო O
penup()
goto(245, 125)
pendown()

left(90)

forward(35)

left(90)

forward(25)

left(90)

forward(35)

left(90)

forward(25)

#ასო A
penup()
goto(280, 90)
pendown()

right(90)

right(20)

forward(35)

right(135)

forward(35)

right(180)


forward(15)

left(70)

forward(15)


penup()
goto(200, 200)
pendown()

exitonclick()
#დასასრული