from turtle import Turtle

MOVE_DISTANCE=10
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.snake_lis=[]
        for i in range(3):
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.setx(i * -20)
            self.snake_lis.append(snake)
        self.head=self.snake_lis[0]

    def add_position(self):
        posi=self.snake_lis[-1].pos()
        new_snake = Turtle()
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.penup()
        self.snake_lis.append(new_snake)
        new_snake.setpos(posi)


    def move(self):
        for snake_no in range(len(self.snake_lis) - 1, 0, -1):
            pos_x = self.snake_lis[snake_no - 1].xcor()
            pos_y = self.snake_lis[snake_no - 1].ycor()
            self.snake_lis[snake_no].goto(pos_x, pos_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)

