import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

x = 0
H = 0.01
massiv_h = []
massiv_t = []
tau = 0.01
for i in range(10):
    massiv_h.append(H/(2**i))
    massiv_t.append(tau / (2**i))
N = int(1/H)

a = (tau**2)/(H**2)
T = int(1/tau)
def pogresh(h, t):
    U = np.zeros((T+1, N+1), dtype=np.float64)
    x = 0
    for i in range(T):
        U[i][0] = 0.
        U[i][N-1] = 0.

    for j in range(N):
        U[0][j] = 20*x*(1-x)
        U[1][j] = U[0][j]
        x=x+h
    print(U)
    for i in range(1, T):
        for j in range(1, N):
            U[i+1][j] = np.dot(a, (U[i, j-1] - (2*U[i, j]) + U[i, j+1])) - U[i-1, j] + np.dot(2, U[i, j])
    last_second = []
    for l in range(N):
        last_second.append(U[N - 1][l])
    last_x = []
    for l in range(N):
        last_x.append(U[l][N - 2])

    return (last_second, last_x)
massiv_pogresh = []


for k in massiv_t:

    massiv_t1, massiv_x1 = pogresh(k,k)

    massiv_t2, massiv_x2 = pogresh(k/2, k/2)

    eps = max(abs(np.array( massiv_t1) - np.array( massiv_t2)))
    #print(eps)
    massiv_pogresh.append(eps)
#Отрисовка
fig = plt.figure()
# Используйте axisartist.Subplot метод для создания области рисования объекта ax
ax = axisartist.Subplot(fig, 111)
# Добавить объекты области рисования на холст
fig.add_axes(ax)
# Установите стили нижней и левой оси области рисования с помощью метода set_axisline_style
# "- |>" представляет сплошную стрелку: "->" представляет полую стрелку
ax.axis["bottom"].set_axisline_style("-|>", size=1.5)
ax.axis["left"].set_axisline_style("-|>", size=1.5)
plt.title("погрешность для шага по времени")
plt.plot(massiv_t, massiv_pogresh, color = "red")

#plt.ylim(bottom = min(massiv_teta_2), top = max(massiv_teta_2))
#plt.xlim(left = 0)
plt.show()
"""for i in range(T):
    print("{")
    for j in range(N):
        print( U[i][j], end = ", ")
    print("},")"""