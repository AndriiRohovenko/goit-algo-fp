import matplotlib.pyplot as plt
import numpy as np

def draw_pyt_tree(depth, x, y, size, angle):
    global ax 

    if depth == 0:
        return

    x_new = x + size * np.cos(np.deg2rad(angle))
    y_new = y + size * np.sin(np.deg2rad(angle))

    next_size = size * np.sqrt(2) / 2

    x_vals = [x, x_new]
    y_vals = [y, y_new]

    ax.plot(x_vals, y_vals, color='black')

    draw_pyt_tree(depth - 1, x_new, y_new, next_size, angle - 45)
    draw_pyt_tree(depth - 1, x_new, y_new, next_size, angle + 45)


fig, ax = plt.subplots()

ax.set_aspect('equal', adjustable='box')

# Get recursion depth from user
depth = int(input("Enter the recursion depth for the fractal tree: "))

draw_pyt_tree(depth, 0, 0, 1, 90)

ax.axis('off')
plt.show()