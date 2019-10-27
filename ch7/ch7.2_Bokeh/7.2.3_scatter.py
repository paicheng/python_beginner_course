from bokeh.plotting import figure, show, output_file
import os

os.system("cls")
p = figure(width=800, height=400, title="零用金統計")
p.xaxis.axis_label = "X軸"
p.yaxis.axis_label = "Y軸"

listx = [1, 5, 7, 9, 13, 16]
listy = [15, 50, 80, 40, 70, 50]

listy1 = [x+10 for x in listy]
sizes = [10, 20, 30, 30, 20, 10]
colors = ["red", "blue", "green", "pink", "violet", "gray"]

p.circle(listx, listy, size=sizes, color="red", alpha=0.5, legend="高雄")
p.square(listx, listy1, size=sizes, alpha=0.5, color="green", legend="台北")
show(p)
