from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("/Users/mac/Downloads/flash-card-project-start/data/french_words.csv")

data_dic = data.to_dict(orient='records')
current_card = {}


def on_button_click():
    create_flashcards()
    clicked()


def clicked():
    global data_dic
    if data_dic:
        data_dic.remove(current_card)
        new_data = pd.DataFrame(data_dic)
        new_data.to_csv("words_to_learn.csv", index=False)


def create_flashcards():
    global current_card
    global data_dic
    if data_dic:
        shuffle = random.randint(0, len(data_dic)-1)
        current_card = data_dic[shuffle]
        Language.config(text="French")
        Word.config(text=current_card["French"])
        window.after(3000,flip_card)
    else:
        Language.config(text="")
        Word.config(text="No more words")
        
def flip_card():
    global current_card
    Language.config(text="English")
    Word.config(text= current_card["English"])


######### UI ##############
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50)
window.title("Flashy")
canvas = Canvas(window, width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
image=PhotoImage(file="/Users/mac/Downloads/flash-card-project-start/images/card_front.png")
FlashCard=canvas.create_image(400,260, image=image,anchor="center")
Language=Label(text="Language",font=("Ariel",40, "italic"),bg="white",anchor='center',fg='black')
Language.place(x=310,y=120)
Word = Label(text='Word', font=("Arial", 60,'bold'),bg="white",anchor='center',fg='black')
Word.place(x=310,y=265)
canvas.grid(row=1,column=1,columnspan=2, pady=50)
RightImage = PhotoImage(file="/Users/mac/Downloads/flash-card-project-start/images/right.png")
Right = Button(image=RightImage,highlightthickness=0,bg=BACKGROUND_COLOR,command=on_button_click)
Right.grid(row=2,column=2)
WrongImage = PhotoImage(file="/Users/mac/Downloads/flash-card-project-start/images/wrong.png")
Wrong = Button(image=WrongImage,highlightthickness=0,bg=BACKGROUND_COLOR, command=create_flashcards)
Wrong.grid(row=2,column=1)


window.mainloop()