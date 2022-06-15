import random
from turtle import Turtle


class Blocks:
    def __init__(self, num_blocks):
        self.segments = []
        self.num_blocks = num_blocks
        self.shape_list = ["turtle", "circle", "classic"]
        self.create_structure()
        self.create_misc()

    def create_structure(self):
        """ Create the square blocks """
        for n in range(0, self.num_blocks):
            block = Turtle()
            block.penup()
            block.color(random.randrange(255), random.randrange(255), random.randrange(255))
            block.goto(x=random.randrange(-400, 400), y=random.randrange(-200, 300))
            block.shape("square")
            block.shapesize(stretch_len=2)
            self.segments.append(block)

    def create_misc(self):
        """ Create the classic blocks """
        for n in range(0, random.choice(range(0, 4))):
            block = Turtle()
            block.penup()
            block.color(random.randrange(255), random.randrange(255), random.randrange(255))
            block.goto(x=random.randrange(-400, 400), y=random.randrange(-200, 300))
            block.setheading(random.randrange(0, 360))
            block.shape(random.choice(self.shape_list))
            if block.shape() != "circle":
                block.shapesize(stretch_len=2)
            self.segments.append(block)
