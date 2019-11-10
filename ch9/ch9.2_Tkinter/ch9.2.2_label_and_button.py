import tkinter as tk


def clickme():
    global count
    count += 1
    labeltext.set("你按我 " + str(count) + " 次了。")
    if btntext.get() == "按我":
        btntext.set("恢復原來文字")
    else:
        btntext.set("按我")


win = tk.Tk()
win.geometry("450x100")
win.title("this is main window")

labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(win, fg="red", textvariable=labeltext)
labeltext.set("歡迎光臨")
label1.pack()
button1 = tk.Button(win, textvariable=btntext, command=clickme)
btntext.set("按我")
button1.pack()
win.mainloop()
