# Pong Game
# Shreyas Pani

import turtle
import winsound

# Setup of Screen
window = turtle.Screen()
window.title("Pong by Shreyas Pani")  # Name Window
window.bgcolor("#333333")  # Color of Window
window.setup(width=800, height=600)  # Dimensions of Window
window.tracer(0)  # No Frames Are Not Shown

#Scores
score1 = 0
score2 = 0

#  Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()  # No Lines
paddle1.goto(-350, 0)

#  Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()  # No Lines
paddle2.goto(350, 0)

#  Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

#Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


# Function
def paddle1up():
    paddle1.sety(paddle1.ycor()+20)


def paddle1down():
    paddle1.sety(paddle1.ycor()-20)


def paddle2up():
    paddle2.sety(paddle2.ycor()+20)


def paddle2down():
    paddle2.sety(paddle2.ycor()-20)


# Keyboard Binding
window.listen()
window.onkeypress(paddle1up, "w")
window.onkeypress(paddle1down, "s")
window.onkeypress(paddle2up, "Up")
window.onkeypress(paddle2down, "Down")


#  Main Loop
while True:
    window.update()
    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
    # Paddle and Ball Collision
    if (350 > ball.xcor() > 340) and (paddle2.ycor() + 40 > ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (-350 < ball.xcor() < -340) and (paddle1.ycor() + 40 > ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
