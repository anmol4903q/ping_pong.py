# 🎮 main.py — Ping Pong Game Setup & Main Loop

from turtle import *
import time
from tuddle_sticks import Stick     # 🏓 Paddle controls
from ball import Ball               # 🔵 Ball class

tim = Turtle()
screen = Screen()
screen.tracer(0)                    # ❌ No automatic animation
screen.setup(width=600, height=600)
screen.bgcolor("DeepSkyBlue")       # 🌊 Background color
screen.title("Ping pong GAME")

# 🟨 Dashed center line
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.goto(x=0, y=300)
tim.pendown()
for i in range(1, 22):
    tim.setheading(270)
    tim.pensize(5)
    tim.penup()
    tim.fd(15)
    tim.pendown()
    tim.fd(15)

# 🏓 Create paddles and ball
stick = Stick()
ball = Ball()
stick.left_paddle()
stick.right_paddle()

# 🧠 High Score tracking
hiscore = 0

# 🎧 Keybindings for controls
screen.listen()
screen.onkey(key="Up", fun=stick.right_up_move)
screen.onkey(key="Down", fun=stick.right_down_move)
screen.onkey(key="w", fun=stick.left_up_move)
screen.onkey(key="W", fun=stick.left_up_move)
screen.onkey(key="S", fun=stick.left_down_move)
screen.onkey(key="s", fun=stick.left_down_move)

# 🧮 Scores
score1 = 0
score2 = 0

# 🚀 Ball launch direction
ball.ball_init()

# 🎮 Game Loop starts
game_on = True
speed = 0.09  # 🐢 Initial speed

tun = Turtle()  # 🧾 Left Score Display
tig = Turtle()  # 🧾 Right Score Display

while game_on:
    time.sleep(speed)        # ⏳ Slow down for animation
    screen.update()          # 🔄 Manual refresh
    ball.move()              # 🔵 Ball keeps moving

    if not ball.border():    # 🚫 If out of border
        game_on = False

    # 🔁 Ball hits top/bottom
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()

    # 🏓 Ball hits RIGHT paddle
    if ball.distance(stick.tiny) < 50 and ball.xcor() > 267:
        ball.paddle_bounce(stick.tiny)
        score1 += 1

    # 🏓 Ball hits LEFT paddle
    if ball.distance(stick.tin) < 50 and ball.xcor() < -267:
        ball.paddle_bounce(stick.tin)
        score2 += 1

    # 📈 Score update on screen
    stick.score(tun, tig, score1, score2)

    # ⏩ Increase game speed as score goes up
    if score1 > 5 or score2 > 5:
        speed = 0.05
    if score1 > 10 or score2 > 10:
        speed = 0.02

    # 🏆 Update high score
    if score1 > hiscore or score2 > hiscore:
        hiscore = max(score1, score2)

    # ☠️ Game ends
    if not game_on:
        ball.game_over(hiscore)
        break

exitonclick()  # 🖱️ Exit on click
