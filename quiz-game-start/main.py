from question_model import Question
from data import DataCenter
from quiz_brain import QuizBrain


def main():
    dc = DataCenter()

    user_cat, difficulty = dc.game_setup()
    question_data = dc.get_questions(user_cat, difficulty)

    question_bank = []

    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_question():
        quiz.next_question()

    print("Congratulations you have completed the quiz!")
    print(f"Your final score was: {quiz.score}/{len(question_bank)}")


if __name__ == "__main__":
    is_game_over = False
    while not is_game_over:
        main()
        will_continue = input("Want to play again? (Y/N): ").lower()

        if will_continue == "n":
            is_game_over = True
