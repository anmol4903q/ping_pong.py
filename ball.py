# 🎱 Ball control + 🧱 Border Collision + 🛑 Game Over logic
from turtle import *
import random

# 🎯 Possible starting directions for the ball
L = [55, 70, 250, 340]                                           
ch = random.choice(L)

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("Blue")                  # 🔵 Set ball color
        self.shape("circle")               # ⚪ Shape of the ball
        self.penup()                       # ✋ No drawing on move
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)  # ⚖️ Slightly smaller ball
        self.just_bounced = False          # 🚫 To avoid multiple bounces in a row

    def ball_init(self):
        self.setheading(ch)                # 🧭 Set a random initial angle
        self.fd(25)                        # ➡️ Initial kick

    def move(self):
        self.fd(14)                        # 🔁 Regular movement
        self.just_bounced = False          # 🔓 Allow bounce again next time

    def bounce(self):
        y = self.ycor()
        if y >= 290 or y <= -290:          # 🧱 If it hits top or bottom
            self.setheading(-self.heading())  # 🔄 Reverse vertical direction

    def paddle_bounce(self, paddle):
        if not self.just_bounced:          # ✅ Only bounce if not just done
            new_heading = 180 - self.heading()  # ↩️ Reflect angle horizontally
            self.setheading(new_heading % 360)
            self.fd(14)                    # ⏩ Move a bit to avoid getting stuck
            self.just_bounced = True       # 🚫 Mark as bounced to prevent spam

    def border(self):
        x = self.xcor()
        y = self.ycor()
        if x >= 300 or x <= -300:          # ❌ Out of left/right border = game over
            return False
        return True                        # ✅ Ball is still in play

    def game_over(self, hiscore):
        self.goto(0, 0)                    # 📍 Center the ball
        self.write(f"   GAME OVER!\nWinner's Score: {hiscore}", 
                   align="center", font=("Courier", 15, "bold"))  # 🏆 Show final score
        
        