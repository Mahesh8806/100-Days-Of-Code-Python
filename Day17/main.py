from data import question_data
from question_model import Question
from quize_brain import QuizeBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text , question_ans)
    question_bank.append(new_question)

Quize = QuizeBrain(question_bank);

while Quize.still_has_question():
    Quize.next_question()

print("\n\nYou have completed Quize...")
print(f"Your current score is: {Quize.score} / {Quize.question_number}")