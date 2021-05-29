from turtle import Turtle


class Snake:

    def __init__(self, num_segments):
        self.segments = []
        self.num_segments = num_segments
        self.seg_size = 20
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for x in range(0, self.num_segments + 1):
            self.add_segment((0, 0))

        # place segments adjacent to each other
        count = 0
        previous_position = 0
        for turtle in self.segments:
            if count == 0:
                previous_position = turtle.pos()
                count += 1
            else:
                # The size of a turtle is 20 pixels. Each turtle should be moved back 20 pixels from the position of the
                # previous turtle
                x_pos = previous_position[0] - 20
                y_pos = previous_position[1]
                turtle.goto(x_pos, y_pos)
                previous_position = (x_pos, y_pos)

    def add_segment(self, position):
        next_turtle = Turtle(shape="square")
        next_turtle.color("white")
        next_turtle.penup()
        next_turtle.goto(position)
        self.segments.append(next_turtle)

    def extend(self):
        extend_pos = self.segments[len(self.segments)-1].pos()
        self.add_segment(extend_pos)

    def move(self):
        # start at the end of the list and move each turtle to the next turtle's position
        for seg_num in range(len(self.segments) - 1, -1, -1):
            # make sure you are not at the very first turtle
            if seg_num > 0:
                next_pos = self.segments[seg_num - 1].pos()
                self.segments[seg_num].goto(next_pos)
            else:
                self.segments[seg_num].forward(self.seg_size)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)


