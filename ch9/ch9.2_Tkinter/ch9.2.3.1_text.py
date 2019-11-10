import tkinter as tk

win = tk.Tk()
text = tk.Text(win, bg="green", fg='red')
text.insert(tk.INSERT, "Tkinter套件是圖形化使用者介面，\n")
text.insert(tk.INSERT, "雖然功能略為陽春，\n")
text.insert(tk.INSERT, "但已經足夠一般應用程式使用，\n")
text.insert(tk.INSERT, "而且是內含在Python系統中，\n")
text.insert(tk.END, "不需要另外安裝即可使用。")
text.pack()
text.insert(tk.INSERT, "\nnew line")
text.config(state=tk.DISABLED)

win.mainloop()
