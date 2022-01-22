"""Simple Pong game"""

import turtle
import winsound
import time

#creating window for game
wn = turtle.Screen()
#name of game
wn.title("Pong by Sam")
#colour of window
wn.bgcolor("black")
#size of window
wn.setup(width=800, height=600)
#stop the window from updating, speeds up game
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
#speed of animation -max speed
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
#stop the turtle from drawing lines as it moves
paddle_a.penup()
#define start position for paddle
paddle_a.goto(-350,0)
#change default shape 20px x20px to 100px x 20px
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

#Paddle B
paddle_b = turtle.Turtle()
#speed of animation -max speed
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
#stop the turtle from drawing lines as it moves
paddle_b.penup()
#define start position for paddle
paddle_b.goto(350,0)
#change default shape 20px x20px to 100px x 20px
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#Ball
ball = turtle.Turtle()
#speed of animation -max speed
ball.speed(0)
ball.shape('square')
ball.color('white')
#stop the turtle from drawing lines as it moves
ball.penup()
#define start position for paddle
ball.goto(0,0)
#defining the movement of the ball - 2 pixels in each dimension in this case
ball.dx = 0.2
ball.dy = -0.2

#pen - the scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
#hides the turtle
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align='center', font=('Courier', 24, 'normal'))



#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y+= -20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y+= -20
    paddle_b.sety(y)

#keyboard binding
#tells window to listen to keyboard inputs
wn.listen()
#calls function specified when key is pressed
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update()
    #every time the loop runs the window updates.

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    #y borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('446100__justinvoke__bounce.wav', winsound.SND_ASYNC)
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('446100__justinvoke__bounce.wav', winsound.SND_ASYNC)

    #x borders
    if ball.xcor() > 390:
        ball.goto(0, 0)
        time.sleep(1)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=('Courier', 24, 'normal'))
        winsound.PlaySound('142608__autistic-lucario__error.wav', winsound.SND_ASYNC)
    elif ball.xcor() < -390:
        ball.goto(0,0)
        time.sleep(1)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=('Courier', 24, 'normal'))
        winsound.PlaySound('142608__autistic-lucario__error.wav', winsound.SND_ASYNC)



    #ball-paddle collisions

    if (ball.xcor() > 340  and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('269718__michorvath__ping-pong-ball-hit.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340  and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('269718__michorvath__ping-pong-ball-hit.wav', winsound.SND_ASYNC)
    
