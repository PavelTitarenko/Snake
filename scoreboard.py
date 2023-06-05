from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
FILE_PATH = "high_score.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.score = 0
        with open(FILE_PATH) as file:
            self.high_score = int(file.read())
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_PATH, "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", move=False, align=ALIGNMENT, font=FONT)