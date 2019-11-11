import tkinter as tk

win = tk.Tk()
for i in range(6):
    button = tk.Button(win, text="button {}".format(i+1), width=20)
    # button.grid(row=i//3, column=i % 3, padx=5, pady=5)
    if i == 1:
        button.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
    elif i == 2:
        button.grid(row=0, column=4, padx=5, pady=5)
    else:
        button.grid(row=i//3, column=i % 3, padx=5, pady=5)


win.mainloop()
