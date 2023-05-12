import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from sympy import *
from mpl_toolkits.mplot3d import Axes3D

# Уравнение 1 второго критерия:
def equation_1_2crit(SIGMA_1, SIGMA_3, THETA, NU):
    expr1_2 = SIGMA_1 * (math.cos(THETA) ** 2 - NU * math.sin(THETA) ** 2) + SIGMA_3 * (
        math.sin(THETA) ** 2 - NU * math.cos(THETA) ** 2)
    return expr1_2
def equation_2_2crit(SIGMA_1, SIGMA_3, THETA, NU):
    expr2_2 = SIGMA_1 * (math.sin(THETA) ** 2 - NU * math.cos(THETA) ** 2) + SIGMA_3 * (
             math.cos(THETA) ** 2 - NU * math.sin(THETA) ** 2)
    return expr2_2
def equation_1_1crit(SIGMA_1, sigma_2, THETA, NU):
    expr1_1 = SIGMA_1 * (math.cos(THETA))**2+sigma_2*(math.sin(THETA))**2
    return expr1_1
def equation_2_1crit(SIGMA_1, sigma_2, THETA, NU):
    expr = SIGMA_1 * (math.sin(THETA))**2+sigma_2*(math.cos(THETA))**2
    return expr
def max_val(sigma_1, sigma_2, theta):
    eq_str1 = (equation_1_2crit(sigma_1, sigma_2, theta, 0.25))
    eq_str2 = (equation_2_2crit(sigma_1, sigma_2, theta, 0.25))
    eq_str3 = (equation_1_1crit(sigma_1, sigma_2, theta, 0.25))
    eq_str4 = (equation_2_1crit(sigma_1, sigma_2, theta, 0.25))
    print(eq_str1,eq_str2,eq_str3,eq_str4)
    maxval=max(abs(eq_str1), abs(eq_str2),abs(eq_str3),abs(eq_str4))
    if (maxval == abs(eq_str1)):
        return eq_str1
    elif maxval == abs(eq_str2):
        return eq_str2
    elif maxval == abs(eq_str3):
        return eq_str3
    elif maxval == abs(eq_str4):
        return  eq_str4
    else:
        return -999
# Задаем размеры рисунка
fig, ax = plt.subplots(figsize=(6, 6))
fig2 = plt.figure(figsize=(6, 6))

sigma_1=0
n=0
theta=math.radians(0)
Rcx=1
Rcy=1
Rtx=1
Rty=1
while(sigma_1>-2):
    sigma_2=0
    while(sigma_2>-2):
        eq_str1 = (equation_1_2crit(sigma_1, sigma_2, theta, 0.25))
        eq_str2 = (equation_2_2crit(sigma_1, sigma_2, theta, 0.25))
        eq_str3 = (equation_1_1crit(sigma_1, sigma_2, theta, 0.25))
        eq_str4 = (equation_2_1crit(sigma_1, sigma_2, theta, 0.25))
        if min(eq_str1,eq_str2,eq_str3,eq_str4)==eq_str1:
            ax.scatter(sigma_1, sigma_2, color="salmon", linewidths=0.1)
        elif min(eq_str1, eq_str2, eq_str3, eq_str4) == eq_str2:
            ax.scatter(sigma_1, sigma_2, color="tomato", linewidths=0.1)
        elif min(eq_str1, eq_str2, eq_str3, eq_str4) == eq_str3:
            ax.scatter(sigma_1, sigma_2, color="teal", linewidths=0.1)
        elif min(eq_str1, eq_str2, eq_str3, eq_str4) == eq_str4:
            ax.scatter(sigma_1, sigma_2, color="aqua")
        else:
            ax.scatter(sigma_1, sigma_2, color="white")
        sigma_2 = sigma_2-0.1
    sigma_1 = sigma_1-0.1

x=np.linspace(-2,0,20)
y=np.linspace(-2,0,20)
xgrid, ygrid = np.meshgrid(x,y)

ax.scatter(2, 2, color="salmon", linewidths=0.1, label="крит 2, ур 1")
ax.scatter(2, 2, color="tomato", linewidths=0.1, label="крит 2, ур 2")
ax.scatter(2, 2, color="teal", linewidths=0.1, label="крит 1, ур 1")
ax.scatter(2, 2, color="aqua", linewidths=0.1, label="крит 1, ур 2")
# Создание переменных SymPy
SIGMA_1, SIGMA_3, THETA, NU = symbols('SIGMA_1, SIGMA_3, THETA, NU')
R_BANGED = -1
R_UNBOUND = -1
# Уравнение 1 второго критерия:
expr1_2 = (SIGMA_1 * (cos(THETA) ** 2 - NU * sin(THETA) ** 2) + SIGMA_3 * (
        sin(THETA) ** 2 - NU * cos(THETA) ** 2) - R_UNBOUND)
# Уравнение 2 второго критерия:
expr2_2 = (SIGMA_1 * (sin(THETA) ** 2 - NU * cos(THETA) ** 2) + SIGMA_3 * (
        cos(THETA) ** 2 - NU * sin(THETA) ** 2) - R_BANGED)

# Замена коэф. Пуассона значением 0,25
expr1_2 = expr1_2.subs(NU, 0.25)
expr2_2 = expr2_2.subs(NU, 0.25)

# Выражение СИГМА2 из двух уравнений
SIGMA_3_1_2 = solve(expr1_2, SIGMA_3)  # Сигма 3 по первому уравнению второго критерия
SIGMA_3_2_2 = solve(expr2_2, SIGMA_3)  # Сигма 3 по второму уравнению второго критерия
SIGMA_3_1_2 = SIGMA_3_1_2[0]
SIGMA_3_2_2 = SIGMA_3_2_2[0]

# График первого критерия
x1_list = []
y2_list = []

for i in range(-2, 1):
    x1 = R_UNBOUND * cos(theta) ** 2 + R_BANGED * sin(theta) ** 2
    y2 = R_UNBOUND * sin(theta) ** 2 + R_BANGED * cos(theta) ** 2
    x1_list.append(x1)
    y2_list.append(y2)

ax.plot(range(-2, 1), y2_list, color="blue", label='Первый критерий', linewidth=2)
ax.plot(x1_list, range(-2, 1), color="blue", linewidth=2)

# График второго критерия
x_list = []
y1_list = []
y2_list = []

for x in range(-2, 1):
    y1 = SIGMA_3_1_2.subs([(SIGMA_1, x), (THETA, theta)])
    y2 = SIGMA_3_2_2.subs([(SIGMA_1, x), (THETA, theta)])
    x_list.append(x)
    y1_list.append(y1)
    y2_list.append(y2)

ax.plot(x_list, y1_list, color="red", label='Второй критерий', linewidth=2)
ax.plot(x_list, y2_list, color="red", linewidth=2)

ax.set_xlim(-2, 0.05)
ax.set_ylim(-2, 0.05)
ax.set_xlabel("SIGMA_1")
ax.set_ylabel("SIGMA_3")
ax.set_title(r'$\theta$ = '+f"{round(np.degrees(theta), 1)}\N{DEGREE SIGN}")
ax.legend(fontsize=6, loc="upper left", framealpha=1)
plt.show()