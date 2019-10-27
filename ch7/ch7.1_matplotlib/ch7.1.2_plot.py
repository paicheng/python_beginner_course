import matplotlib.pyplot as plt
import os

os.system("cls")

listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]


plt.plot(listx1, listy1, label="Male")
plt.plot(listx2, listy2, color="red", lw=5, ls="--", label="Female")

plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.title("Pocket Money")
plt.xlabel("Age")
plt.ylabel("Money (USD)")
plt.show()
