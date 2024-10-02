import sys                                          # for path to external scripts
sys.path.insert(0, '/home/aslin-garvasis/matgeo/codes/CoordGeo')        # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import subprocess
import shlex
import scipy.linalg as SA
import mpmath as mp
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen



# Function to read triangle vertices from a file
def read_triangle_vertices(filename):
    vertices = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    point = tuple(map(float, line.strip('()').split(',')))
                    vertices.append(np.array(point).reshape(-1, 1))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except ValueError as ve:
        print(f"Error parsing line: {line}. Exception: {ve}")
        return []
    return vertices

# Read vertices from 'data.txt'
vertices = read_triangle_vertices('data.txt')
if not vertices or len(vertices) < 3:
    print("No vertices were read or not enough vertices. Exiting...")
    exit(1)

# Extracting values for A, B, C
A = vertices[0]
B = vertices[1]
C = vertices[2]

# Tangent sides
sides = tri_sides(A, B, C)
print(sides)

# Generating m, n, p
I_circ_mat = SA.circulant([1, 1, 0]).T
insides = LA.inv(I_circ_mat) @ sides
print(sides, insides)

# Points of contact
F = (insides[1] * A + insides[0] * B) / (insides[1] + insides[0])
D = (insides[2] * C + insides[1] * B) / (insides[2] + insides[1])
E = (insides[0] * C + insides[2] * A) / (insides[0] + insides[2])
print(D, E, F)

# Angle bisector verification
D =np.array([[3.66],[1.28]])
m1 = dir_vec(A, B)
m2 = dir_vec(B, C)
m3 = dir_vec(C, A)



BD = LA.norm(B - D)
CD = LA.norm(C - D)
AD = LA.norm(A - D)
AB = LA.norm(A - B)
BC = LA.norm(B - C)
AC = LA.norm(A - C)



plt.figure()
plt.plot([A[0], B[0]], [A[1], B[1]], label='AB')
plt.plot([B[0], C[0]], [B[1], C[1]], label='BC')
plt.plot([C[0], A[0]], [C[1], A[1]], label='CA')
tri_coords =np.hstack([A, B, C, D])
# Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_DA = line_gen(D,A)

# Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:])
plt.plot(x_BC[0,:], x_BC[1,:])
plt.plot(x_CA[0,:], x_CA[1,:])
plt.plot(x_DA[0,:], x_DA[1,:], '--', label='$DA$')

plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['A', 'B', 'C', 'D']

for i, txt in enumerate(vert_labels):
    # Annotate the vertex labels
    plt.annotate(txt, 
                 (tri_coords[0, i].item(), tri_coords[1, i].item()), 
                 textcoords="offset points", 
                 xytext=(0, 10), 
                 ha='center')

    # Annotate the coordinates in the format (x.xx, y.yy)
    coords = f'({tri_coords[0, i].item():.2f}, {tri_coords[1, i].item():.2f})'
    plt.annotate(coords, 
                 (tri_coords[0, i].item(), tri_coords[1, i].item()), 
                 textcoords="offset points", 
                 xytext=(0, -15), 
                 ha='center', 
                 fontsize=9, 
                 color='blue')
# Annotate distances BD and CD
midpoint_BD = (B + D) / 2
midpoint_CD = (C + D) / 2
midpoint_AD = (A + D) / 2
midpoint_AB = (A + B) / 2
midpoint_BC = (B + C) / 2
midpoint_AC = (C + D) / 2

plt.annotate(f'BD = {BD:.2f}', 
             xy=midpoint_BD, 
             textcoords="offset points", 
             xytext=(0, 10), 
             ha='center')
plt.annotate(f'CD = {CD:.2f}', 
             xy=midpoint_CD, 
             textcoords="offset points", 
             xytext=(0, 10), 
             ha='center')
plt.annotate(f'AD = {AD:.2f}', 
             xy=midpoint_AD, 
             textcoords="offset points", 
             xytext=(0, 10), 
             ha='center')




plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

# Show the figure
plt.show()
plt.savefig("/home/aslin-garvasis/Desktop/EE1030/assign5/figs/Fig1.png")
