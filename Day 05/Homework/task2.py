from turtle import *

speed(30)
width(5)
begin_fill()
color("green")
left(180)
forward(480)
left(90)
forward(400)
left(90)
forward(960)
left(90)
forward(400)
left(90)
forward(480)
end_fill()

color("black")
begin_fill()
forward(480)
right(90)
forward(400)
right(90)
forward(960)
right(90)
forward(400)
right(90)
forward(480)
end_fill()

penup()
goto(300, 200)
pendown()
width(2)
color("yellow")
forward(10)
right(180)
forward(5)
left(90)
forward(6)
left(180)
forward(12)

penup()
goto(100, 250)
pendown()

forward(10)
right(180)
forward(5)
left(90)
forward(6)
left(180)
forward(12)

penup()
goto(-100, 200)
pendown()
forward(10)
right(180)
forward(5)
left(90)
forward(6)
left(180)
forward(12)

penup()
goto(-300, 250)
pendown()
forward(10)
right(180)
forward(5)
left(90)
forward(6)
left(180)
forward(12)

penup()
goto(10, 320)
pendown()
forward(10)
right(180)
forward(5)
left(90)
forward(6)
left(180)
forward(12)

penup()
goto(220, 330)
pendown()
forward(10)
right(180)
forward(5)
left(90)
forward(6)
left(180)
forward(12)

penup()
goto(-5, 0)
pendown()

width(5)
color("red")
begin_fill()
forward(30)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
end_fill()

color("brown")
begin_fill()
forward(5)
left(90)
forward(30)
left(90)
forward(10)
left(90)
forward(30)
left(90)
forward(5)
end_fill()

penup()
goto(30, 60)
pendown()
color("blue")
begin_fill()
left(120)
forward(65)
left(115)
forward(70)
left(125)
forward(70)
end_fill()

penup()
goto(260, -5)

color("blue")
begin_fill()
forward(30)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
end_fill()

color("brown")
begin_fill()
forward(5)
left(90)
forward(30)
left(90)
forward(10)
left(90)
forward(30)
left(90)
forward(5)
end_fill()

penup()
goto(295, 60)
pendown()
color("purple")
begin_fill()
left(120)
forward(65)
left(115)
forward(70)
left(125)
forward(70)
end_fill()

penup()
goto(-200, -5)
pendown()

color("yellow")
begin_fill()
forward(30)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
end_fill()

color("brown")
begin_fill()
forward(5)
left(90)
forward(30)
left(90)
forward(10)
left(90)
forward(30)
left(90)
forward(5)
end_fill()

penup()
goto(-165, 60)
pendown()
color("red")
begin_fill()
left(120)
forward(65)
left(115)
forward(70)
left(125)
forward(70)
end_fill()


exitonclick()