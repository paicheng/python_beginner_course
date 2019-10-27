from bokeh.plotting import show, figure, output_file
import os

os.system("cls")
listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]

listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]

p = figure(width=800, height=400, title="零用錢統計")
p.title.text_color = "green"
p.title.text_font_size = "18pt"
p.xaxis.axis_label = "年齡"
p.xaxis.axis_label_text_color = "violet"
p.yaxis.axis_label = "零用錢"
p.yaxis.axis_label_text_color = "violet"
dashs = [12, 4]

p.line(listx1, listy1, line_width=4, line_color='red',
       line_alpha=0.3, line_dash=dashs, legend="男")
p.line(listx2, listy2, line_width=4, legend="女")
show(p)
