import time
from turtle import Screen
import snake
import food
import scoreboard

# Set up screen for snake game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey McSnakeyFace")
screen.tracer(0)

cur_snake = snake.Snake(3)
cur_food = food.Food()
cur_scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(cur_snake.up, "Up")
screen.onkey(cur_snake.down, "Down")
screen.onkey(cur_snake.left, "Left")
screen.onkey(cur_snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.07)

    cur_snake.move()

    # detect snake-food collision
    if cur_snake.segments[0].distance(cur_food) < 15:
        cur_food.move_food()
        cur_scoreboard.increase_score()
        cur_snake.extend()

    # detect wall collision
    if cur_snake.head.xcor() > 285 or cur_snake.head.ycor() > 285 or cur_snake.head.xcor() < -285 or cur_snake.head.ycor() < -285:
        game_on = False
        cur_scoreboard.game_over()

    # detect collision with tail
    for seg in cur_snake.segments[1:]:
        if cur_snake.head.distance(seg) < 10:
            print("tail collision")
            game_on = False
            cur_scoreboard.game_over()

screen.exitonclick()
