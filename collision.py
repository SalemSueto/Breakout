import random


class Collision:
    def __init__(self, screen, width, height, paddle_segments, block_segments, ball, scoreboard, speed):
        self.screen = screen
        self.screen_width = width
        self.screen_height = height
        self.paddle_segments = paddle_segments
        self.paddle_ycor_checkpoint = -1 * (height / 2)
        self.block_segments = block_segments
        self.ball = ball
        self.scoreboard = scoreboard
        self.ball_speed = speed
        # Game Parameter
        self.continue_game = True
        self.next_phase = False
        self.game_is_on = True

    def start_game(self):
        """  """
        while self.game_is_on:
            self.move()
            # Game Over
            if self.continue_game == False:
                self.game_is_on = False
                self.scoreboard.game_over()
                # self.screen.bye()
                # Competed Phase
            if self.next_phase:
                self.game_is_on = False

    def move(self):
        """ Move the ball """
        # Hit all Blocks -> Phase Completed
        if len(self.block_segments) == 0:
            self.next_phase = True
            self.scoreboard.reset_scoreboard()

        # Normal Movement
        self.screen.tracer(0, 0)
        self.ball.forward(self.ball_speed)
        self.screen.update()

        # Collision with the vertical walls
        distance_vertical_walls = self.screen_width/2 - abs(self.ball.xcor())
        if distance_vertical_walls <= 20:
            if self.ball.heading() < 90:
                self.ball.setheading(90 + self.ball.heading())
            elif self.ball.heading() > 90:
                self.ball.setheading(180 - self.ball.heading())
            elif self.ball.heading() == 0:
                self.ball.setheading(350)

        # Collision with the upper horizontal wall
        if self.ball.ycor() > 0:
            if (self.screen_height/2 - self.ball.ycor()) <= 10:
                if self.ball.heading() < 90:
                    self.ball.setheading(360 - self.ball.heading())
                elif self.ball.heading() > 90:
                    self.ball.setheading(90 + self.ball.heading())
                elif self.ball.heading() == 90:
                    self.ball.setheading(90+180)

        # Collision with the down horizontal wall -> Game OVER
        if self.ball.ycor() < 0 and 180 < self.ball.heading() < 360:
            if (self.screen_height/2 - abs(self.ball.ycor())) <= 20:
                self.continue_game = False

        # Collision with the paddle
        if self.ball.ycor() < 0 and 180 < self.ball.heading() < 360:    # Downward Direction
            if self.ball.ycor() - self.paddle_ycor_checkpoint <= 54:
                closest_segment = 0
                min_dist_seg = 1000
                for n in range(0, len(self.paddle_segments)):
                    dist = self.ball.distance(self.paddle_segments[n])
                    if dist < min_dist_seg:
                        min_dist_seg = dist
                        closest_segment = n
                if min_dist_seg <= 20:
                    if closest_segment < 4:
                        self.ball.setheading(180 - (180/9 * (closest_segment + 1)))
                    elif closest_segment == 4:
                        self.ball.setheading(90)
                    else:
                        self.ball.setheading(180/9 * (9 - closest_segment))

        # Collision with Blocks
        for n in self.block_segments:
            if self.ball.distance(n) <= 20:
                n.hideturtle()
                self.block_segments.remove(n)
                self.screen.update()
                # Square Collision
                if n.shape() == "square":
                    if self.ball.heading() in [0, 90, 180, 270, 360]:
                        self.ball.setheading(self.ball.heading() + 180 + random.choice(range(1, 20)))
                    elif 0 < self.ball.heading() < 90:
                        self.ball.setheading(self.ball.heading() + 270)
                    elif 90 < self.ball.heading() < 180:
                        self.ball.setheading(self.ball.heading() + 90)
                    elif 180 < self.ball.heading() < 270:
                        self.ball.setheading(self.ball.heading() + 90)
                    else:
                        self.ball.setheading(self.ball.heading() - 270)
                # Classic Collision
                if n.shape() == "classic":
                    self.ball.setheading(n.heading())
                # Circle Collision
                if n.shape() == "circle":
                    self.ball.setheading(random.choice(range(0, 360)))
                # Turtle Collision
                if n.shape() == "turtle":
                    self.ball.goto(x=random.randrange(-400, 400), y=random.randrange(-200, 300))
