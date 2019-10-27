from bokeh.plotting import show, figure, output_file
import os
p = figure(width=800, height=600)

listx = [1, 5, 7, 9, 13, 16]
listy = [15, 30, 50, 60, 80, 90]
p.line(listx, listy)
mydir = os.path.dirname(__file__)
newpath = os.path.join(mydir, "lineout.html")
output_file(newpath)
show(p)
