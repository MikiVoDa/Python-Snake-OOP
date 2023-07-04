from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segmente = []
        self.create_snake()
        self.sarpe1 = self.segmente[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.shapesize(0.9)
        new_segment.goto(position)
        self.segmente.append(new_segment)

    def extend(self):
        self.add_segment(self.segmente[-1].position())

    def move(self):
        for seg_num in range(len(self.segmente) - 1, 0, -1):
            new_x = self.segmente[seg_num - 1].xcor()
            new_y = self.segmente[seg_num - 1].ycor()
            self.segmente[seg_num].goto(new_x, new_y)
        self.segmente[0].forward(20) #speed

    def up(self):
        if self.sarpe1.heading() != 270:
            self.sarpe1.setheading(90)


    def down(self):
        if self.sarpe1.heading() != 90:
            self.sarpe1.setheading(270)

    def left(self):
        if self.sarpe1.heading() != 0:
            self.sarpe1.setheading(180)

    def right(self):
        if self.sarpe1.heading() != 180:
            self.sarpe1.setheading(0)

    def reset(self):
        for seg in self.segmente:
            seg.goto(1000,1000)
        self.segmente.clear()
        self.create_snake()
        self.sarpe1 = self.segmente[0]
