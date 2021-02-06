from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard:
    def __init__(self):
        self.level = 1

    def game_over(self):
        game_over = Turtle()
        game_over.color("black")
        game_over.penup()
        game_over.hideturtle()
        game_over.write("Game Over", align="center", font=FONT)

    def score(self):
        score = Turtle()
        score.color("black")
        score.penup()
        score.hideturtle()
        score.goto(-220, 260)
        score.write(f"Level: {self.level}", align="center", font=FONT)
        score.clear()
        
    def update_score(self):
        self.level += 1
