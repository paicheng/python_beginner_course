import matplotlib.pyplot as plt
import os

os.system("cls")

listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]

plt.bar(listx1, listy1, label="Male", color="blue")
plt.bar(listx2, listy2, label="女性", color="red")
plt.title("allowance")
plt.xlabel("Age")
plt.ylabel("Money")
plt.show()
