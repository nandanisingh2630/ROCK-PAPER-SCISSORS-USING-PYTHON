from tkinter import *
from PIL import Image, ImageTk
from random import randint

#HomeScreen 

import tkinter as tk
from tkinter import Label, Button

class RPSHomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x400")
        self.root.configure(bg="#b2d5e9")

        # Create a container frame to center content
        self.container = tk.Frame(root, bg="#52b0db")
        self.container.pack(expand=True)

        # Welcome Label
        self.label = Label(self.container, text="Welcome to Rock, Paper, Scissors!", 
                           font=("Arial", 50, "bold"), bg="#f0f0f0")
        self.label.pack(pady=10)

        # Start Button
        self.start_button = Button(self.container, text="Start Game", font=("Arial", 45,"bold"), command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        self.label.config(text="Let's play!")
            # Here you can destroy the home screen and open the game screen if needed
        self.root.destroy()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RPSHomeScreen(root)
    root.mainloop()

# main window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="light blue")

# Resize and load images
def resize_image(path):
    img = Image.open(path)
    img = img.resize((500, 500), Image.Resampling.LANCZOS)  # Resize to 500X500
    return ImageTk.PhotoImage(img)

rock_img = resize_image("rockcomp.png.jpeg")
paper_img = resize_image("papercomp.png.jpeg")
scissor_img = resize_image("scissorcomp.png.jpeg")
rock_img_comp = resize_image("rock.png")
paper_img_comp = resize_image("paper.png")
scissor_img_comp = resize_image("scissors.png")

# insert picture
user_label = Label(root, image=scissor_img, bg="light blue")
comp_label = Label(root, image=scissor_img_comp, bg="light blue")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
playerscore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerscore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerscore.grid(row=1, column=1)
playerscore.grid(row=1, column=3)

# indicators
user_indicator = Label(root, font=50, text="USER", bg="black", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="black", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="blue", fg="white")
msg.grid(row=3, column=2)

def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

def updateCompScore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)

# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()

# update choices
choices = ["rock", "paper", "scissor"]

def updateChoice(x):
    compchoice = choices[randint(0, 2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(x, compchoice)

# Buttons
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock"))
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper"))
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor"))
rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
scissor.grid(row=2, column=3)

root.mainloop()