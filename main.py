from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import Scoreboard

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake=Snake()
food = Food()
scorecount=Scoreboard()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.down, 'Down')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.add_position()
        scorecount.collision_with_food()

    #Detect collision with wall
    if snake.head.xcor()> 285 or snake.head.xcor()< -285 or snake.head.ycor()> 285 or snake.head.ycor()< -285:
        game_is_on = False
        scorecount.game_over()

    #Detect collision with tail
    # for i in snake.snake_lis:
    #     if i == snake.head:
    #         pass
    #     elif snake.head.distance(i) < 5:
    #         game_is_on = False
    #         scorecount.game_over()

             #orrr good way---slicing

    for i in snake.snake_lis[1:]:     # we don't want to use first position i.e "0"
        if snake.head.distance(i) < 5:
            game_is_on = False
            scorecount.game_over()


screen.exitonclick()