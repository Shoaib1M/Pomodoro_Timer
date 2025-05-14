import tkinter



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global rep
    rep=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global rep
    rep+=1
    work=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    if rep%8==0:
        count_down(long_break)
        title_label.config(text="Break",fg=RED)
    elif rep%2==0:
        count_down(short_break)
        title_label.config(text="Break",fg=PINK)
    else:
        count_down(work)
        title_label.config(text="Work",fg=GREEN)
        no_mark=""
        for i in range(rep//2):
            no_mark=no_mark+"✅"
        check_marks.config(text=no_mark)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    min=count//60
    sec=count%60
    if len(str(sec))!=2:
        sec="0"+str(sec)
    if len(str(min)) != 2:
        min = "0" + str(min)

    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down ,count - 1)
    else:
        start_timer()







# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100,bg=YELLOW)

title_label=tkinter.Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
title_label.grid(column=1,row=0)

canvas=tkinter.Canvas(window,width=200,height=224,bg=YELLOW,highlightthickness=0)
image=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button=tkinter.Button(text="Start",highlightthickness=0,bg=YELLOW,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=tkinter.Button(text="Reset",highlightthickness=0,bg=YELLOW,command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks=tkinter.Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)


tkinter.mainloop()
