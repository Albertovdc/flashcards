from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card ={}
words = {}
try:
# Read the data
  data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  original_data = pandas.read_csv("data/french_words.csv")
  words = original_data.to_dict(orient="records")
else:
  words = data.to_dict(orient="records")

#print(type(words))
# print(type(current_card))

def save_word():
  words.remove(current_card)
  print(len(words))
  data = pandas.DataFrame(words)
  data.to_csv("data/words_to_learn.csv", index=False)
  generate_word()
 


# Generate the word 
def generate_word():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(words)
  canvas.itemconfig(language, text="French", fill="black")
  canvas.itemconfig(word, text=current_card["French"], fill="black")
  canvas.itemconfig(canvas_image, image=card_front)
  flip_timer=window.after(3000, func=flip_card)


def flip_card():
  canvas.itemconfig(canvas_image, image=card_back)
  canvas.itemconfig(language, text="English", fill="white")
  canvas.itemconfig(word,text=current_card["English"], fill="white") 



# Configure the user interface
window = Tk()
window.title("Flashcards")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Add the words to learn
new_word = random.choice(words)
language = canvas.create_text(400, 150, text="French", font=(FONT_NAME , 40, "italic"))
word  = canvas.create_text(400, 263, text=f"{new_word["French"]}", font=(FONT_NAME,60,"bold"))

# Create the check button
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=save_word)
check_button.grid(row=1, column=1)

# Create the cancel button
cancel_image = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cancel_image, highlightthickness=0,command=generate_word)
cancel_button.grid(row=1, column=0)

generate_word()

window.mainloop()