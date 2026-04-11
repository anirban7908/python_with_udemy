import requests
import html


class DataCenter:

    def __init__(self) -> None:
        self.category_config = {
            "1": "9",  # g.k
            "2": "17",  # science_and_nature
            "3": "15",  # video_game
            "4": "12",  # music
            "5": "23",  # history
            "6": "31",  # japanese_anime
        }

    def choos_category_and_difficulty(self, category):
        return self.category_config["category"]

    def get_questions(self, category, difficulty):
        chosen_cat = self.category_config[category]

        url = f"https://opentdb.com/api.php?amount=10&category={chosen_cat}&difficulty={difficulty}&type=boolean"
        api_qestions = requests.get(url).json()
        question_data = []
        # print(api_qestions)
        if api_qestions["response_code"] == 0:
            for q in api_qestions["results"]:
                formatted_question = {
                    "text": html.unescape(q["question"]),
                    "answer": q["correct_answer"],
                }
                question_data.append(formatted_question)

        return question_data

    def game_setup(self):
        print(
            """
            Press 1 for G.K
            Press 2 for science and nature
            Press 3 for video game
            Press 4 for music
            Press 5 for history
            Press 6 for japanese anime
        """
        )
        user_cat = input("Select Catagory: ")

        diffculty = input("Choose Difficulty (Easy/Medium/Hard): ").lower()

        return user_cat, diffculty


# print(question_data)
# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {
#         "text": "Approximately one quarter of human bones are in the feet.",
#         "answer": "True",
#     },
#     {
#         "text": "The total surface area of a human lungs is the size of a football pitch.",
#         "answer": "True",
#     },
#     {
#         "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
#         "answer": "True",
#     },
#     {
#         "text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
#         "answer": "False",
#     },
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {
#         "text": "No piece of square dry paper can be folded in half more than 7 times.",
#         "answer": "False",
#     },
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"},
# ]
