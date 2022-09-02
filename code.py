question_data = [
        {
            "category": "Science: Computers",
            "type": "boolean",
            "difficulty": "medium",
            "question": "The HTML5 standard was published in 2014.",
            "correct_answer": "True",
            "incorrect_answers": ["False"],
        },
        {
            "category": "Science: Computers",
            "type": "boolean",
            "difficulty": "medium",
            "question": "The first computer bug was formed by faulty wires.",
            "correct_answer": "False",
            "incorrect_answers": ["True"],
        }],
for question in question_data:
    print(question[2])