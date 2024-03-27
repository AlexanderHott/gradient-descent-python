import numpy as np
import matplotlib.pyplot as plt

def z_func(x, y) -> float:
    # return x * x    
    return np.sin(5 * x) * np.cos(5 * y) / 5

# ∇z = <dz/dx, dz/dy>
def gradient_vector(x, y) -> tuple[float, float]:
    # return 2 * x
    return (np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * y) * np.sin(5 * x))

x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)

Z = z_func(X, Y)

ax = plt.subplot(projection='3d', computed_zorder=False)

current_pos = (0.4, 0.7, z_func(0.4, 0.7))

learning_rate=0.01

for _ in range(1000):
    X_prime, Y_prime = gradient_vector(current_pos[0], current_pos[1])
    X_new = current_pos[0] - learning_rate * X_prime
    Y_new = current_pos[1] - learning_rate * Y_prime
    current_pos = (X_new, Y_new, z_func(X_new, Y_new))

    ax.plot_surface(X, Y, Z, cmap='viridis', zorder=0)
    ax.scatter(current_pos[0], current_pos[1], current_pos[2], color='magenta', zorder=1)

    plt.pause(0.001)
    ax.clear()

