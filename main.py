import matplotlib.pyplot as plt
import numpy as np
import time

y = [float(i) for i in open('start.dat.txt', 'r')]
e = np.eye(len(y))
i = -1*np.eye(len(y)-1)
a = np.zeros(len(y)-1)
b = np.zeros((len(y), 1))
A = np.vstack([a,i])
A = np.column_stack([A, b])
A = A + e

def func(y):
    y1 = y - 0.5 * A * y
    return y1

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(y)
for i in range(20):
    y = func(y)
    line.set_ydata(y)
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.02)
plt.ioff()
plt.show()
