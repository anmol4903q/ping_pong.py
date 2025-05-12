# 🏓 Paddle Control + 🧮 Scoreboard
from turtle import *

up = 90       # ⬆️ Direction for moving up
down = 270    # ⬇️ Direction for moving down

class Stick:
    def __init__(self):
        self.tiny = Turtle()  # 🤍 Right paddle
        self.tin = Turtle()   # 🖤 Left paddle

    def left_paddle(self):
        self.tin.penup()                                # 🛑 No line drawing
        self.tin.color("black")                         # 🎨 Black color
        self.tin.shape("square")                        # ◻️ Paddle shape
        self.tin.shapesize(stretch_len=1, stretch_wid=5)  # 📏 Stretch to paddle shape
        self.tin.goto(x=-288, y=0)                      # 📍 Place at left edge

    def right_paddle(self):
        self.tiny.penup()
        self.tiny.color("white")                        # ⚪ White paddle
        self.tiny.shape("square")
        self.tiny.shapesize(stretch_len=1, stretch_wid=5)
        self.tiny.goto(x=284, y=0)                      # 📍 Place at right edge

    # 🎮 Movement for right paddle (arrow keys)
    def right_up_move(self):
        newx = self.tiny.ycor() + 20                    # 🔼 Move up
        self.tiny.goto(self.tiny.xcor(), newx)

    def right_down_move(self):
        newy = self.tiny.ycor() - 20                    # 🔽 Move down
        self.tiny.goto(self.tiny.xcor(), newy)

    # 🎮 Movement for left paddle (W/S keys)
    def left_up_move(self):
        new = self.tin.ycor() + 20                      # 🔼 Move up
        self.tin.goto(self.tin.xcor(), new)

    def left_down_move(self):
        new = self.tin.ycor() - 20                      # 🔽 Move down
        self.tin.goto(self.tin.xcor(), new)

    # 🧮 Score display for both players
    def score(self, tun, tim, score1, score2):
        tim.penup()
        tim.hideturtle()
        tim.color("Black")
        tim.goto(150, 200)                              # 📍 Right side score
        tim.clear()
        tim.write(f"Score = {score1}", align="center", font=("Courier", 15, "normal"))

        tun.penup()
        tun.hideturtle()
        tun.color("Black")
        tun.goto(-150, 200)                             # 📍 Left side score
        tun.clear()
        tun.write(f"Score = {score2}", align="center", font=("Courier", 15, "normal"))
      
    
         
    