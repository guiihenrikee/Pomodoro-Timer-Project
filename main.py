from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
NEW = "#222831"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    start_button["state"] = "active"

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sex = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sex)
        timer_label.config(text="BREAK", bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", bg=YELLOW, fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", bg=YELLOW, fg=GREEN)
    start_button["state"] = "disabled"

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for x in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img_tomato = PhotoImage(file="tomato.gif")
canvas.create_image(100, 112, image=img_tomato)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label = Label(bg=YELLOW, fg=GREEN, font="bold")
checkmark_label.grid(column=1, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
