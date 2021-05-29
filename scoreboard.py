from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("green")
        self.goto(0, 280)
        self.update()

    def update(self):
        self.clear()
        self.write("Score: " + str(self.score), align='center', font=('Calibri', 14, 'normal'))

    def increase_score(self):
        self.score = self.score + 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Times New Roman', 21, 'normal'))
