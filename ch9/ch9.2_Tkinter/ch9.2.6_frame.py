import tkinter as tk

win = tk.Tk()

frame1 = tk.Frame(win, bg='red')
frame1.pack()
label1 = tk.Label(frame1, text="label1")
entry1 = tk.Entry(frame1)
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

frame2 = tk.Frame(win, bg="green")
frame2.pack()
button1 = tk.Button(frame2, text="submit")
button2 = tk.Button(frame2, text='cancel')
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
win.mainloop()
