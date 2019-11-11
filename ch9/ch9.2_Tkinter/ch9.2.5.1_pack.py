import tkinter as tk

win = tk.Tk()
for i in range(4):
    button = tk.Button(win, text="button {}".format(i), width=20)
    # button.pack()
    # button.pack(padx=20, pady=5)
    if i == 0:
        button.pack(padx=20, pady=5, side="right")
    elif i == 1:
        button.pack(padx=20, pady=5, side="left")
    elif i == 2:
        button.pack(padx=20, pady=5)
    else:
        button.pack(padx=20, pady=5)


win.mainloop()
