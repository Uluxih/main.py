import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from sympy import *
from mpl_toolkits.mplot3d import Axes3D
from mayavi import mlab
from scipy import array, newaxis
from matplotlib.colors import LinearSegmentedColormap

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
def max_val(sigma_1, sigma_2, theta, nu=0.25):
    eq_str1 = (equation_1_2crit(sigma_1, sigma_2, theta, nu))
    eq_str2 = (equation_2_2crit(sigma_1, sigma_2, theta, nu))
    eq_str3 = (equation_1_1crit(sigma_1, sigma_2, theta, nu))
    eq_str4 = (equation_2_1crit(sigma_1, sigma_2, theta, nu))
    print(sigma_1, sigma_2, eq_str3,eq_str4,eq_str1,eq_str2)
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
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
cmap = LinearSegmentedColormap.from_list('red_blue', ['b', 'w', 'r'], 256)
ax.set_title('Поверхность интенсивности эквивалентных напряжений ')


xs = []
ys = []
zs = []
theta=math.radians(0)
degree=0
nu=0.1
while(degree<=0):
    xs=[]
    ys=[]
    zs=[]
    sigma_1=2
    while(sigma_1>-2):
        sigma_2=2
        while(sigma_2>-2):
            xs.append(sigma_1)
            ys.append(sigma_2)
            mv = max_val(sigma_1,sigma_2,math.radians(degree))
            zs.append(abs(mv))
            sigma_2 = sigma_2 - 0.05
        sigma_1 = sigma_1 - 0.05
    ax.cla()
    ax.set_zlim([0, 3])
    surf = ax.plot_trisurf(xs, ys, zs, linewidth=0, cmap=cmap)
    # ax.view_init(90, 90)
    ax.set_title('Поверхность интенсивности эквивалентных напряжений '+ str(int(degree)))
    ax.set_xlabel('σ₁')
    ax.set_ylabel('σ₂')
    ax.set_zlabel('σᵢ')
    plt.savefig(str(int(degree)))
    degree+=0.05
