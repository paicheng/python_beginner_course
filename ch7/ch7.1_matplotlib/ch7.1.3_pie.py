import matplotlib.pyplot as plt
import os

os.system("cls")

labels = ["East", "South", "West", "North"]
sizes = [5, 10, 20, 15]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, labeldistance=1.1,
        autopct="%3.1f%%", shadow=False, startangle=90, pctdistance=0.6)
plt.axis("equal")
plt.legend()
plt.show()
