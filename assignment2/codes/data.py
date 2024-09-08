import matplotlib.pyplot as plt
import numpy as np

# Define the points
point1 = (--6, 5)
point2 = (-2, 3)

# Calculate the midpoint
midpoint = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# Plotting
plt.figure(figsize=(10, 6))

# Plot the original points
plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'ro', label='Points (-6, 5) and (-2, 3)')
plt.text(point1[0], point1[1], '(-6, 5)', fontsize=12, ha='right')
plt.text(point2[0], point2[1], '(-2, 3)', fontsize=12, ha='left')

# Plot the midpoint
plt.plot(midpoint[0], midpoint[1], 'bo', label='Midpoint (-4, 4)')
plt.text(midpoint[0], midpoint[1], f'(-4, 4)', fontsize=12, ha='left')

# Plot the line segment
plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'g--', label='Line Segment')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Points, Midpoint')
plt.legend()

# Show plot
plt.show()
