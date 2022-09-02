from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# my_question = Question()
question_bank=[]
for question in question_data:
    print(question['question'])
#     for i in range(len(question)):
#         q_text=question[i]['question']
#         answer=question[i]['correct_answer']
#         question_bank.append(Question(q_text,answer))
# # print(question_bank)
# quiz=QuizBrain(question_bank)
# while not quiz.still_have_questions():
#     quiz.next_question()
# print('you have comleted the quiz')
# print(f'your final score was: {quiz.score}/{quiz.question_num}')












# is_on=True
# q_count=0
# n=0
# current_score=0
# while is_on:
#     q_count+=1
#     ask=input(f"Q.{q_count}: {question_bank[n].q_text}. (True or False)?: ").lower()
#     if ask==question_bank[n].answer.lower():
#         print('you got it right!')
#         print(f'the answer is {question_bank[n].answer}')
#         current_score+=1
#         print(f'your_current score is {current_score}/{q_count}')
#         n+=1
#     else:
#         is_on=False
#         print('you got it wrong!')
#         print(f'the answer is {question_bank[n].answer}')
#         print(f'your_current score is {current_score}/{q_count}')


