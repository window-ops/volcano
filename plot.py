import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X ** 2 + Y ** 2) / 4) * np.sin(np.sqrt(X ** 2 + Y ** 2)) + np.exp(-(X ** 2 + Y ** 2) / 10)

# Create figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(X, Y, Z, cmap='terrain', linewidth=0, antialiased=False)

# Customize axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Volcano')

# Show plot
plt.show()
