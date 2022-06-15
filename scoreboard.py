from turtle import Turtle

ALIGNMENT = "center"
STYLE = ("Arial", 12, "italic")
STYLE_GAME_OVER = ("Arial", 40, "italic")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 330)
        self.display()

    def update(self):
        self.goto(0, 330)
        self.clear()
        self.score += 1
        self.display()

    def display(self):
        message = f"Score: {self.score} - High Score: {self.high_score}"
        self.write(message, True, align=ALIGNMENT, font=STYLE)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.update()

    def game_over(self):
       self.color("red")
       self.goto(0, 0)
       self.write("GAME OVER!", True, align=ALIGNMENT, font=STYLE_GAME_OVER)
