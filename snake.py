from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, ):
        self.snake_part = 0
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_part(position)

    def add_snake_part(self, position):
        snake_part = Turtle()
        snake_part.penup()
        snake_part.shape("square")
        snake_part.color("white")
        self.snake_parts.append(snake_part)
        snake_part.setposition(position)

    def extend(self):
        self.add_snake_part(self.snake_parts[-1].position())

    def move(self):
        for parts in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[parts - 1].xcor()
            new_y = self.snake_parts[parts - 1].ycor()
            self.snake_parts[parts].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):

        for snake_part in self.snake_parts:
            snake_part.setposition(1000, 1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]
