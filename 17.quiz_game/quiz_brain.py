class QuizBrain:
    def __init__(self,q_list):
        self.question_num=0
        self.question_list=q_list
        self.score=0
    def still_have_questions(self):
        return self.question_num == len(self.question_list)
    def next_question(self):
        current_answer=self.question_list[self.question_num]
        self.question_num+=1
        user_answer=input(f"Q.{self.question_num}: {current_answer.q_text} (True or False)?: ").lower()
        self.check_answer(user_answer,current_answer.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score+=1
        else:           
            print("That wrong!")
        print(f'the correct answer is {correct_answer}')
        print(f'your score is {self.score}/{self.question_num} \n')
        