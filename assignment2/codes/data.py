import matplotlib.pyplot as plt
import numpy as np

def read_points_from_file(filename):
    points = {'A': None, 'B': None, 'C': None}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            # Extract lines for points A, B, and C
            point_lines = {label: next((line for line in lines if line.startswith(f"Point {label}")), None) for label in 'ABC'}
            
            # Extract coordinates from each line
            def extract_point(line):
                if line:
                    parts = line.split(': ')[1].strip().strip('()').split(', ')
                    try:
                        return float(parts[0]), float(parts[1])
                    except ValueError:
                        print(f"Error: Could not convert {parts} to float.")
                        return None
                return None
            
            points = {label: extract_point(line) for label, line in point_lines.items()}
            
            # Check if any point could not be parsed
            if None in points.values():
                print("Error: One or more points are missing or invalid.")
                return None
    
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    except ValueError as e:
        print(f"Error processing file data: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
    return points

def plot_points(points):
    if not points:
        print("No points to plot.")
        return
    
    # Extract coordinates
    labels = np.array(list(points.keys()))
    coords = np.array(list(points.values()))
    
    if coords.shape[0] != 3:
        print("Error: Expected exactly 3 points.")
        return
    
    x_coords, y_coords = coords[:, 0], coords[:, 1]
    
    # Plotting the points
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, color='red', zorder=5)
    
    # Annotate each point
    annotations = [f'{label} ({x:.2f}, {y:.2f})' for label, x, y in zip(labels, x_coords, y_coords)]
    for x, y, annotation in zip(x_coords, y_coords, annotations):
        plt.text(x, y, annotation, fontsize=12, ha='right', zorder=10)
    
    # Connect points with lines
    indices = np.arange(len(labels))
    lines_x = np.concatenate([x_coords[indices], x_coords[np.roll(indices, shift=-1)]])
    lines_y = np.concatenate([y_coords[indices], y_coords[np.roll(indices, shift=-1)]])
    plt.plot(lines_x.reshape(-1, 2).T, lines_y.reshape(-1, 2).T, 'k-', zorder=2)
    
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

