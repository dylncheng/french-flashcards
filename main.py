from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

global word


'''RANDOM WORD'''
def new_word():
    global word
    word = random.choice(contents)
    canvas.itemconfig(flashcard, image=flashcard_front)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(vocab, text=word["French"], fill='black')
    window.after(3000, func=display_translation)

def display_translation():
    global word
    canvas.itemconfig(flashcard, image=flashcard_back)
    canvas.itemconfig(vocab, text=word['English'], fill='white')
    canvas.itemconfig(language, text='English', fill='white')

def correct():
    global word
    contents.remove(word)
    new_word()


def incorrect():
    global word
    words_to_learn.append(word)
    df = pandas.DataFrame(words_to_learn)
    df.to_csv('./data/words_learn.csv', index=False)
    new_word()


''' READ DATA'''
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except:
    data = pandas.read_csv('./data/french_words.csv')

contents = data.to_dict(orient="records")

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flashcard App')

canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = PhotoImage(file='./images/card_front.png')
flashcard_back = PhotoImage(file='./images/card_back.png')
flashcard = canvas.create_image(400, 262, image=flashcard_front)

language = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
vocab = canvas.create_text(400, 263, text='trouve', font=('Arial', 60, 'bold'))

canvas.grid(row=0, column=0, columnspan=2)

correct_img = PhotoImage(file='./images/right.png')
incorrect_img = PhotoImage(file='./images/wrong.png')

correct_button = Button(image=correct_img, highlightthickness=0, command=correct)
incorrect_button = Button(image=incorrect_img, highlightthickness=0, command=incorrect)

correct_button.grid(row=1, column=0)
incorrect_button.grid(row=1, column=1)

words_to_learn = []

new_word()

window.mainloop()
