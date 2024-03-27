import numpy as np
import matplotlib.pyplot as plt

def y_func(x):
    # return x * x    
    return np.sin(x)

def y_prime(x):
    # return 2 * x
    return np.cos(x)

x = np.arange(-100, 100, 0.1)
x = np.arange(-5, 5, 0.1)
y = y_func(x)

current_pos = (3, y_func(3))

learning_rate=0.01

for _ in range(1000):
    new_x = current_pos[0] - learning_rate * y_prime(current_pos[0])
    new_y = y_func(new_x)
    current_pos = (new_x, new_y)

    plt.plot(x, y)
    plt.scatter(current_pos[0], current_pos[1], color='red')
    plt.pause(0.01)
    plt.clf()

