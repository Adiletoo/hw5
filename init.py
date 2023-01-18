from classs import Hero, Hero_super

hero1 = Hero_super('Naruto', 'cloning')
hero2 = Hero('Sasuke', 'Sharingan')
print(hero1.__get_name__())
print(hero1.power())

import turtle

tt = turtle.Turtle()
turtle.bgcolor("blue")
tt.pencolor("yellow")

tt.speed(0)
tt.penup()
tt.goto(0, 200)
tt.pendown()
forDis = 0
dR = 0

while (True):
    tt.forward(forDis)
    tt.right(dR)
    forDis += 3
    dR += 1
    if dR == 210:
        break
    tt.hideturtle()

turtle.done()
