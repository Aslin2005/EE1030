import matplotlib.pyplot as plt
import numpy as np

def read_points_from_file(filename):
    points = {'A': None, 'B': None, 'C': None}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("Point A"):
                    parts = line.split(': ')[1].strip('()').split(', ')
                    x = float(parts[0])
                    y = float(parts[1])
                    points['A'] = (x, y)
                elif line.startswith("Point B"):
                    parts = line.split(': ')[1].strip('()').split(', ')
                    x = float(parts[0])
                    y = float(parts[1])
                    points['B'] = (x, y)
                elif line.startswith("Point C"):
                    parts = line.split(': ')[1].strip('()').split(', ')
                    x = float(parts[0])
                    y = float(parts[1])
                    points['C'] = (x, y)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    except ValueError as e:
        print(f"Error processing file data: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    # Check if all points are read
    if None in points.values():
        print("Error: One or more points are missing.")
        return None
    
    return points

def plot_points(points):
    if not points:
        print("No points to plot.")
        return
    
    # Extract coordinates
    labels = list(points.keys())
    coords = np.array(list(points.values()))
    
    if coords.shape[0] != 3:
        print("Error: Expected exactly 3 points.")
        return
    
    x_coords = coords[:, 0]
    y_coords = coords[:, 1]
    
    # Plotting the points
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, color='red', zorder=5)
    
    # Annotate each point
    for i, label in enumerate(labels):
        plt.text(x_coords[i], y_coords[i], f'{label} ({x_coords[i]:.2f}, {y_coords[i]:.2f})', fontsize=12, ha='right', zorder=10)
    
    # Connect points with lines
    for i in range(len(labels)):
        plt.plot([x_coords[i], x_coords[(i + 1) % len(labels)]], [y_coords[i], y_coords[(i + 1) % len(labels)]], 'k-', zorder=2)
    
    # Set labels and title
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.title('Plot of Points A, B, and C')
    plt.grid(True)
    
    # Show the plot
    plt.show()

def main():
    filename = 'points.txt'
    points = read_points_from_file(filename)
    if points:
        plot_points(points)

if __name__ == "__main__":
    main()

