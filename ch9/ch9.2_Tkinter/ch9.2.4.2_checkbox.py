import tkinter as tk


def choose():
    global balls, choice
    str = "你最喜歡的球類運動:"
    for i in range(len(choice)):
        if choice[i].get() == 1:
            str = str+balls[i]+' '
    msg.set(str)


win = tk.Tk()
choice = []
balls = ['足球', '籃球', '棒球']
msg = tk.StringVar()
label = tk.Label(win, text='選擇喜歡的球類運動')
label.pack()
for i in range(len(balls)):
    tem = tk.IntVar()
    choice.append(tem)
    item = tk.Checkbutton(
        win, text=balls[i], variable=choice[i], command=choose)
    item.pack()
lblmsg = tk.Label(win, fg='red', textvariable=msg)
lblmsg.pack()
win.mainloop()
