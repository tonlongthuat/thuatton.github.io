from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
my_turtle = Turtle()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('my snake game')
screen.tracer(0)

snake=Snake()
food=Food()
score_board=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_on=True
while game_on:
    screen.update()
    score_board
    time.sleep(0.1)
    snake.move()

    # detect food
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend_segment()
        score_board.increase_score()
    
    # detect the wall
    if snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.xcor()< -280 or snake.head.ycor()< -280:
        score_board.reset()
        snake.reset_segments()
        snake.move()       
    
    # detect tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_segments()
screen.exitonclick()