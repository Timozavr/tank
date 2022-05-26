from random import randint, choice
import turtle

window = turtle.Screen()
window.title("TANK")
window.setup(width=1.0,height=1.0)
window.bgcolor("yellow")
window.tracer(1.5)

desk = turtle.Turtle()
desk.speed(0)
desk.color('white')
desk.begin_fill()
desk.goto(400,400)
desk.goto(400,-400)
desk.goto(-400,-400)
desk.goto(-400,400)
desk.goto(400,400)
desk.end_fill()
desk.hideturtle()

FONT = ("Arial", 44)
score_a = 0
s1 = turtle.Turtle(visible=False)
s1.color('blue')
s1.up()
s1.setpos(-500,0)
s1.write(score_a, font=FONT)

score_b = 0
s2 = turtle.Turtle(visible=False)
s2.color('red')
s2.up()
s2.setpos(500,0)
s2.write(score_b, font=FONT)

tank = turtle.Turtle()
tank.color('blue')
tank.shape('square')
tank.shapesize(stretch_len=4,stretch_wid=4)
tank.up()
tank.goto(0,-350)
goon = turtle.Turtle()
goon.color('blue')
goon.shape('square')
goon.shapesize(stretch_len=1,stretch_wid=4)
goon.up()
goon.goto(0,-310)

enemy = turtle.Turtle()
enemy.color('green')
enemy.shape('square')
enemy.shapesize(stretch_len=4,stretch_wid=1)
enemy.up()
enemy.goto(0,350)
enemy.dx = choice([-3,-2,-1,1,2,3])


projectile = turtle.Turtle()
projectile.shape('circle')
projectile.up()
projectile.speed(0)
projectile.color('red')
projectile.hideturtle()
projectile.dy = -5

def move_left():
    x = tank.xcor() - 25
    x1 = goon.xcor() - 25
    if x < -360:
        x = -360
    if x1 < -360:
        x1 = -360
    tank.setx(x)
    goon.setx(x)

def move_right():
    x = tank.xcor() + 25
    x1 = goon.xcor() + 25
    if x > 360:
        x = 360
    if x1 > 360:
        x1 = 360
    tank.setx(x)
    goon.setx(x)

def move_goon():
    x = goon.xcor()
    y = goon.ycor() + 40
    projectile.goto(x, y)
    projectile.showturtle()
    projectile.dy = 5

window.listen()
window.onkeypress(move_left,"a")
window.onkeypress(move_right,"d")
window.onkeypress(move_goon,"w")

while True:
    window.update()
    
    projectile.sety(projectile.ycor() + projectile.dy)
    enemy.setx(enemy.xcor() + enemy.dx)

    if projectile.ycor()>= 390:
        projectile.dy = - projectile.dy
        score_b += 1
        s2.clear()
        s2.write(score_b,font=FONT)

    if projectile.ycor()<= -390:
        projectile.dy = 0

    if enemy.xcor()>= 360:
        enemy.dx = - enemy.dx
        enemy.showturtle()

    if enemy.xcor()<= -360:
        enemy.dx = - enemy.dx 
        enemy.showturtle()

    if projectile.ycor() >= enemy.ycor()-10\
        and projectile.ycor()<= enemy.ycor()+10\
        and projectile.xcor()>= enemy.xcor()-40\
        and projectile.xcor()<= enemy.xcor()+40:
        projectile.dy = - projectile.dy
        enemy.dx = choice([-3,-2,-1,1,2,3])
        enemy.hideturtle()
        projectile.hideturtle()
        score_a += 1
        s1.clear()
        s1.write(score_a,font=FONT)

window.mainloop()
