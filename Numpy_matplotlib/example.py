# import numpy as np
# import matplotlib.pyplot as plt

# # Create a NumPy array
# data = np.array([1, 2, 3, 4, 5,5.5,6.5])

# # Plot the data using Matplotlib
# plt.plot(data)
# plt.xlabel('X-axis label')
# plt.ylabel('Y-axis label')
# plt.title('Simple Line Plot')
# plt.show()

# second example
# import numpy as np
# import matplotlib.pyplot as plt

# # Generate some sample data
# np.random.seed(0)
# x = np.linspace(0, 10, 100)
# y = 2 * x + 1 + np.random.normal(0, 1, 100)

# # Create a scatter plot
# plt.figure(figsize=(8, 6))
# plt.scatter(x, y, label='Data')

# # Fit a linear trend line
# p = np.polyfit(x, y, 1)
# trend_line = np.polyval(p, x)
# plt.plot(x, trend_line, color='red', label='Trend Line')

# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Scatter Plot with Trend Line')

# # Add legend
# plt.legend()

# # Display plot
# plt.show()

# third example
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate some sample data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Create a 3D surface plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap='viridis')

# Add color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Surface Plot')

# Display plot
plt.show()


