import tkinter as tk

win = tk.Tk()
win.geometry("400x150")
for i in range(3):
    button = tk.Button(win, text="button {}".format(i+1), width=20)
    if i == 0:
        button.place(relx=0.5, rely=0.5, anchor="center")
    elif i == 1:
        button.place(relx=0.1, rely=0.1, anchor="nw")
    else:
        button.place(relx=0.1, rely=0.8, anchor="w")

win.mainloop()
