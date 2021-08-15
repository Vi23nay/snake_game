from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 8, "normal")      #arial

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score : {self.score} " , align=ALIGNMENT, font=FONT)


    def collision_with_food(self):
        self.clear()                 # it only clear screen...no change of orientation and turtle positioning
        self.score += 1
        self.write(f"Score : {self.score}  ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER  ", align=ALIGNMENT, font=("courier", 18, "normal"))





