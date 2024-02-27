# Python Programming Internship
# Roaa Fathi
# Last Submission Date: 5 Sep.
# Rock Paper Scissors Game

import tkinter as tk
import tkinter.font as tk_font

import random

pc_score = 0
user_score = 0
r = 1

screen = tk.Tk()
screen.geometry("700x700")
screen.title("Rock Paper Scissors Game")
screen.configure(bg="black")  # Set background color to black

screen.columnconfigure(0, weight=1)  # Column 0 expands to center-align content
screen.columnconfigure(1, weight=1)  # Column 1 expands to center-align content
screen.rowconfigure(1, weight=1)
screen.rowconfigure(5, weight=1)
screen.rowconfigure(10, weight=1)

custom_font = tk_font.Font(family="Courier New", size=12, weight="bold")
w_custom_font = tk_font.Font(family="fangsong", size=14, weight="bold")
score_font = tk_font.Font(family="Times Square", size=18, weight="bold")

# Create frames

round_frame = tk.Frame(screen, bg="black", borderwidth=2, relief="solid")
round_frame.grid(row=0, column=0, padx=10, pady=10)

user_score_frame = tk.Frame(screen, bg="black", borderwidth=2, relief="solid")
user_score_frame.grid(row=0, column=0, padx=10, pady=10)

pc_score_frame = tk.Frame(screen, bg="black", borderwidth=2, relief="solid")
pc_score_frame.grid(row=0, column=1, padx=10, pady=10)

choice_frame = tk.Frame(screen, bg="black", borderwidth=2, relief="solid")
choice_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

ask = tk.Frame(screen, bg="black", borderwidth=2, relief="solid")
ask.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

end = tk.Frame(screen, bg="black", borderwidth=2, relief="solid")
end.grid(row=10, column=0, columnspan=2, padx=10, pady=10)


# Functions
# Generate PC random choice
def generate_choice():
    choices = ["rock", "scissors", "paper"]
    return random.choice(choices)


# User rock function
def rock():
    pc_choice = generate_choice()
    global user_score, pc_score
    if r < 6:
        pc_choice_lbl["text"] = pc_choice
        if pc_choice == "rock":
            user_score += 1
            pc_score += 1

        elif pc_choice == "scissors":
            user_score += 1

        elif pc_choice == "paper":
            pc_score += 1

        u_score_lbl["text"] = str(user_score)
        p_score_lbl["text"] = str(pc_score)
        check_play()


# User paper function
def paper():
    pc_choice = generate_choice()
    global user_score, pc_score

    if r < 6:
        pc_choice_lbl["text"] = pc_choice
        if pc_choice == "paper":
            user_score += 1
            pc_score += 1

        elif pc_choice == "rock":
            user_score += 1

        elif pc_choice == "scissors":
            pc_score += 1

        u_score_lbl["text"] = str(user_score)
        p_score_lbl["text"] = str(pc_score)
        check_play()


# User scissors function
def scissors():
    pc_choice = generate_choice()
    global user_score, pc_score

    if r < 6:
        pc_choice_lbl["text"] = pc_choice
        if pc_choice == "scissors":
            user_score += 1
            pc_score += 1

        elif pc_choice == "paper":
            user_score += 1

        elif pc_choice == "rock":
            pc_score += 1

        u_score_lbl["text"] = str(user_score)
        p_score_lbl["text"] = str(pc_score)
        check_play()


# Check the winner function
def check_winner():
    global winner_lbl, user_score, pc_score
    if user_score == pc_score:
        winner_lbl["text"] = "** TIE MODE **"

    elif user_score > pc_score:
        winner_lbl["text"] = "** CONGRATULATIONS, YOU ARE THE WINNER **"

    elif user_score < pc_score:
        winner_lbl["text"] = "** THE PC is THE WINNER **"


# NO button function
def n_play():
    # End grid
    end_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    end_btn.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    return


# YES button function
def y_play():
    global r, user_score, pc_score
    r = 1
    user_score = 0
    pc_score = 0
    u_score_lbl["text"] = str(user_score)
    p_score_lbl["text"] = str(pc_score)

    round_lbl["text"] = "Round " + str(r)
    pc_choice_lbl.config(text="")
    winner_lbl.config(text="")
    play_lbl.grid_forget()
    y_btn.grid_forget()
    n_btn.grid_forget()
    end_lbl.grid_forget()
    end_btn.grid_forget()


# check game round function

def check_play():
    global r

    if r == 5:
        r += 1
        check_winner()

        play_lbl.grid(row=0, column=0, columnspan=2, sticky="ew")

        y_btn.grid(row=1, column=0, padx=30, pady=10, sticky="ew")

        n_btn.grid(row=1, column=1, padx=30, pady=10, sticky="ew")

    else:
        r += 1
        round_lbl["text"] = "Round " + str(r)


# Create labels
# Score panel labels
user_lbl = tk.Label(user_score_frame, text="Your Score", fg="#ff9933", bg="black", font=score_font)
pc_lbl = tk.Label(pc_score_frame, text="PC Score", fg="#ff9933", bg="black", font=score_font)
p_score_lbl = tk.Label(pc_score_frame, text=str(pc_score), fg="#ff9933", bg="black", font=score_font)
u_score_lbl = tk.Label(user_score_frame, text=str(user_score), fg="#ff9933", bg="black", font=score_font)

# User choice label and buttons
choice_lbl = tk.Label(choice_frame, text="CHOOSE...", fg="#D3E6CE", bg="black", font=custom_font)
btn_rock = tk.Button(choice_frame, text="   ROCK   ", command=rock, fg="#D3E6CE", bg="#0E65A3", font=custom_font)
btn_paper = tk.Button(choice_frame, text="  PAPER   ", command=paper, fg="#D3E6CE", bg="#0E65A3", font=custom_font)
btn_scissors = tk.Button(choice_frame, text=" SCISSORS ", command=scissors, fg="#D3E6CE", bg="#0E65A3", font=custom_font)

# Round labels
round_num = tk.Label(choice_frame, text=" 5 Rounds ", fg="#ff9933", bg="black", font=score_font)
round_lbl = tk.Label(choice_frame, text="Round " + str(r), fg="#D3E6CE", bg="black", font=custom_font)

# PC choice labels
c_pc_lbl = tk.Label(choice_frame, text="Computer chooses...", fg="#D3E6CE", bg="black", font=custom_font)
pc_choice_lbl = tk.Label(choice_frame, text="", fg="#D3E6CE", bg="#0E65A3", font=custom_font)

# winner label
winner_lbl = tk.Label(screen, text="", fg="#ff4d4d", bg="black", font=w_custom_font)

# Play again label
play_lbl = tk.Label(ask, text="    Play again?     ", fg="#D3E6CE", bg="black", font=custom_font)
y_btn = tk.Button(ask, text="    Yes    ", command=y_play, fg="#D3E6CE", bg="#0E65A3", font=custom_font)
n_btn = tk.Button(ask, text="    No     ", command=n_play, fg="#D3E6CE", bg="#0E65A3", font=custom_font)

# End label and button
end_lbl = tk.Label(end, text="** Thanks for choosing our game! **", fg="#66B266", bg="black", font=custom_font)
end_btn = tk.Button(end, text="END", command=quit, fg="white", bg="#0E65A3", font=custom_font)

# Layout within frames using grid
# Score panel grid
user_lbl.grid(row=0, column=0, sticky="ew")
u_score_lbl.grid(row=1, column=0, sticky="ew")

pc_lbl.grid(row=0, column=1, sticky="ew")
p_score_lbl.grid(row=1, column=1, sticky="ew")

# Round grid
round_num.grid(row=0, column=0, columnspan=3, sticky="ew")
round_lbl.grid(row=1, column=0, columnspan=3, sticky="ew")

# User choice and buttons grid
choice_lbl.grid(row=2, column=0, columnspan=3, sticky="ew")
btn_rock.grid(row=3, column=0, padx=5, pady=10, sticky="ew")
btn_paper.grid(row=3, column=1, padx=5, pady=10, sticky="ew")
btn_scissors.grid(row=3, column=2, padx=5, pady=10, sticky="ew")

# PC choice grid
c_pc_lbl.grid(row=6, column=0, columnspan=3, pady=10, sticky="ew")
pc_choice_lbl.grid(row=8, column=0, columnspan=3, pady=10, sticky="news")

# Winner gird
winner_lbl.grid(row=4, column=0, columnspan=3, pady=10, sticky="ew")

# Run the main event loop
screen.mainloop()
