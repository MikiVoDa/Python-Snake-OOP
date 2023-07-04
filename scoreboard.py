from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Courier", 20, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()


