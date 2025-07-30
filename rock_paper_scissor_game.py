import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    comp_choice = random.choice(choices)
    comp_label.config(text="Computer chose: " + comp_choice)
    if user_choice == comp_choice:
        result = "Draw!"
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors") or
        (user_choice == "Paper" and comp_choice == "Rock") or
        (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "You Lose!"
    result_label.config(text=result)

def reset():
    comp_label.config(text="Computer chose: ")
    result_label.config(text="")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x220")

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16)).pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

comp_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
comp_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

tk.Button(root, text="Reset", command=reset).pack()

root.mainloop()