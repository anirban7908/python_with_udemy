from tkinter import * # type: ignore
import pandas # type: ignore
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    # Pandas dataframe
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# --------------------------------------------Helper Functions-------------------------
def new_card():
    global current_card,flip_timer
    
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    key = list(current_card.keys())[0]
    value = list(current_card.values())[0]
    canvas.itemconfig(card_title, text=key, fill="black")
    canvas.itemconfig(card_word, text=value, fill="black")
    canvas.itemconfig(card_background, image=canvas_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    key = list(current_card.keys())[1]
    value = list(current_card.values())[1]
    canvas.itemconfig(card_title, text=key, fill="white")
    canvas.itemconfig(card_word, text=value, fill="white")
    canvas.itemconfig(card_background, image=canvas_back_image)

def is_known():
    to_learn.remove(current_card)
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_card()
# ---------------------------------------------UI--------------------------------------
window = Tk()
window.title("Flash card project")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
canvas_front_image = PhotoImage(file="images/card_front.png")
canvas_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=canvas_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
unknown_img = PhotoImage(file="images/wrong.png",)
unknown_button = Button(image=unknown_img, highlightthickness=0, command=new_card)
unknown_button.grid(row=1, column=0)

known_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_img,highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

new_card()
window.mainloop()