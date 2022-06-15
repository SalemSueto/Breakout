from turtle import Turtle


class Paddle:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.segment_x_pos = [-80, -60, -40, -20, 0, 20, 40, 60, 80]
        self.segments = []
        self.move_distance = 20
        self.create()

    def create(self):
        """ Create the segments that made up the paddle """
        for n in range(0, 9):
            segment = Turtle()
            segment.shape("square")
            segment.penup()
            segment.goto(x=self.segment_x_pos[n], y=-self.height/2+30)

            if n in [0, 1, 2, 6, 7, 8]:
                segment.color("red")
            else:
                segment.color("white")
            self.segments.append(segment)

    def go_left(self):
        """ Move the paddle to the left """
        if abs(self.segments[0].xcor()) + self.move_distance <= self.width/2:
            self.screen.tracer(0, 0)
            for i in reversed(self.segments):
                now_index = self.segments.index(i)
                if now_index != 0:
                    antecedent_index = self.segments[now_index - 1]
                    new_x = antecedent_index.xcor()
                    new_y = antecedent_index.ycor()
                    i.setposition(x=new_x, y=new_y)
                else:
                    i.setposition(x=i.xcor() - self.move_distance, y=-self.height/2+30)
            self.screen.update()

    def go_right(self):
        """ Move the paddle to the right """
        if abs(self.segments[len(self.segments)-1].xcor()) + self.move_distance <= self.width/2:
            self.screen.tracer(0, 0)
            for i in self.segments:
                now_index = self.segments.index(i)
                if now_index != len(self.segments)-1:
                    next_seg = self.segments[now_index + 1]
                    new_x = next_seg.xcor()
                    new_y = next_seg.ycor()
                    i.setposition(x=new_x, y=new_y)
                else:
                    i.setposition(x=i.xcor() + self.move_distance, y=-self.height / 2 + 30)
            self.screen.update()
