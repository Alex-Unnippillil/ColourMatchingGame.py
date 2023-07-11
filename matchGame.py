import tkinter as tk
import random

# Function to handle Colour selection
def select_Colour(Colour):
    global score, high_score
    if Colour == word_Colours[selected_word]:
        result_label.config(text="Correct!")
        score += 1
        if score > high_score:
            high_score = score
            save_high_score()
        score_label.config(text=f"Score: {score}")
    else:
        result_label.config(text="Wrong!")
        score = 0
        score_label.config(text=f"Score: {score}")
    start_game()

# Function to start the game
def start_game():
    global selected_word
    selected_word = random.randint(0, len(words) - 1)
    result_label.config(text="")
    word_label.config(text=words[selected_word], fg=word_Colours[selected_word])
    for button, Colour in zip(Colour_buttons, Colours):
        button.config(bg=Colour)

# Function to save the high score
def save_high_score():
    global high_score
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))
    high_score_label.config(text=f"High Score: {high_score}")
    
# Function to load the high score
def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Create a window
window = tk.Tk()
window.title("Colour Matching Game")
window.geometry("500x500")  # Set the window size

# Create a title label
title_label = tk.Label(window, text="Colour Matching Game", font=("Helvetica", 20))
title_label.pack(pady=20)

# Create a frame for Colour selection
Colour_frame = tk.Frame(window, width=300, height=200, bd=2, relief=tk.SOLID)
Colour_frame.pack()

# Create Colour buttons
Colours = ["Red", "Green", "Blue", "Yellow"]
Colour_buttons = []
for i, Colour in enumerate(Colours):
    button = tk.Button(Colour_frame, width=10, height=5, bg=Colour, command=lambda Colour=Colour: select_Colour(Colour))
    button.grid(row=i // 2, column=i % 2, padx=5, pady=5)
    Colour_buttons.append(button)

# Create a label for the displayed word
word_label = tk.Label(window, text="", font=("Helvetica", 16))
word_label.pack(pady=10)

# Create a label for the game result
result_label = tk.Label(window, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

# Create a label for the score
score_label = tk.Label(window, text="Score: 0", font=("Helvetica", 16))
score_label.pack(pady=10)

# Load the high score
high_score = load_high_score()

# Create a label for the high score
high_score_label = tk.Label(window, text=f"High Score: {high_score}", font=("Helvetica", 16))
high_score_label.pack(pady=10)

# List of words and corresponding Colours
words = ["Red", "Green", "Blue", "Yellow"]
word_Colours = ["Red", "Green", "Blue", "Yellow"]

# Variable to store the index of the selected word
selected_word = -1

# Score counter
score = 0

# Start the game
start_game()

# Start the main event loop
window.mainloop()
