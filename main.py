from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from blocks import Blocks
from collision import Collision

# Game Settings
num_blocks = 5
ball_speed = 5
width = 900
height = 700
game_prep = False


# Function
def create_new_phase():
    """ Create a new phase with increased speed for the ball """
    global game_prep
    game_prep = True
    screen.tracer(0, 0)
    global num_blocks
    blocks = Blocks(num_blocks)
    global ball_speed
    collision = Collision(screen, width, height, paddle.segments, blocks.segments, ball, scoreboard, ball_speed)
    screen.update()
    # Game preparation
    try:
        while game_prep:
            screen.update()
            ball.set_ball_pos(paddle.segments[4].pos())
    except Exception:
        pass

    # Start Game
    try:
        if game_prep == False:
            collision.start_game()

        if collision.next_phase:
            num_blocks += 0
            ball_speed += 1
            create_new_phase()
    except:
        pass



def end_prep():
    global game_prep
    game_prep = False


# --- GUI Settings --- #
# Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=width, height=height)
screen.title("Breakout!")
screen.colormode(255)
# File Classes
screen.tracer(0, 0)
paddle = Paddle(screen, width, height)
ball = Ball(screen, width, height, paddle.segments)
screen.update()
# Listener
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkey(end_prep, "space")
scoreboard = Scoreboard()
# Start the Program
create_new_phase()
