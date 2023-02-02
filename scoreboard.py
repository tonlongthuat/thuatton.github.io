from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        try:
            file=open("./high_score.txt")
        except :
            file=open("./high_score.txt","w")
            file.write('0')
        else:
            self.high_score=int(file.read())
        finally:
            file.close()
        # with open("18,19.Snake_game\high_score.txt", "r") as file:
        #     self.high_score=int(file.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()
    def update_score(self):
        self.clear()   
        self.write(f"Score:{self.score} High Score:{self.high_score} ",align='center',font=('arial',20,'normal'))
    def increase_score(self):
        self.score+=1
        self.update_score()
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("./high_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_score()
