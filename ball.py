from turtle import Turtle


class Ball(Turtle):
    def __init__(self, screen, width, height, paddle_segments):
        super().__init__()
        # Screen Parameters
        self.screen = screen
        self.screen_width = width
        self.screen_height = height
        self.paddle_ycor_checkpoint = -1*(height/2)
        # Paddle Parameters
        self.paddle_segments = paddle_segments
        # Ball Parameters
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(x=0, y=self.paddle_segments[4].pos()[1] + 22)
        self.setheading(90)

    def set_ball_pos(self, paddle_central_pos):
        """ The Ball follows the position of the paddle by being over its middle segment """
        self.goto(x=paddle_central_pos[0], y=paddle_central_pos[1] + 22)
