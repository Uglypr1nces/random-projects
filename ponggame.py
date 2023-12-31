#Mini hockey game for 2 players

import turtle as t
playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title("ping pong")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)

#create left paddie
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#create right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)


ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection = 0,2
ballydirection = 0,2

#creating pen for scoreboard update

pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=("Arial",24,"normal"))

def leftpaddleup(): 
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)


def rightpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)



while True:
    window.update()

    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1

    elif ball.ycor()>-290:
        ball.sety(-s290)
        ballydirection=ballydirection*-1

    elif ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection = ballxdirection
        playerAscore = playerAscore+1
        pen.clear()
        pen.write("player a: {} player B:{}".format(playerAscore,playerBscore),align="center",font=("Arial"))
        

