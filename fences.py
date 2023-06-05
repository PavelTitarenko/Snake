from turtle import Turtle
COLOR = "white"

class Fences():
    def __init__(self):
        self.segments = []
        self.create_fences()

    def create_fences(self):
        top_row_x = -300
        while top_row_x < 300:
            segment = Turtle(shape="square")
            segment.color(COLOR)
            segment.penup()
            segment.goto(top_row_x, 300)
            self.segments.append(segment)
            top_row_x += 20
        right_colon_y = 300
        while right_colon_y > -300:
            segment = Turtle(shape="square")
            segment.color(COLOR)
            segment.penup()
            segment.goto(300, right_colon_y)
            self.segments.append(segment)
            right_colon_y -= 20
        bottom_row_x = 300
        while bottom_row_x > -300:
            segment = Turtle(shape="square")
            segment.color(COLOR)
            segment.penup()
            segment.goto(bottom_row_x, -300)
            self.segments.append(segment)
            bottom_row_x -= 20
        left_colon_y = -300
        while left_colon_y < 300:
            segment = Turtle(shape="square")
            segment.color(COLOR)
            segment.penup()
            segment.goto(-300, left_colon_y)
            self.segments.append(segment)
            left_colon_y += 20

