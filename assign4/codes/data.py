import sys   
sys.path.insert(0, '/home/aslin-garvasis/matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt
import ctypes 
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

import numpy as np
import matplotlib.pyplot as plt

def parse_data_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = {}
    for line in lines:
        if '=' in line:
            key, value = line.split('=')
            data[key.strip()] = float(value.strip())
    return data

data = parse_data_file('data.txt')

a = data.get('a', 0)
b = data.get('b', 0)

B = np.array([-a, -b]).reshape(-1,1)
A = np.array([a, b]).reshape(-1,1)
def line_gen(start_point, end_point):
    # Create a line segment between start_point and end_point
    t = np.linspace(0, 1, 100)
    line_segment = start_point + t * (end_point - start_point)
    return line_segment
x_BA = line_gen(B, A)

vector_norm = np.linalg.norm(A - B)
plt.plot(x_BA[0,:], x_BA[1,:], label='$B A$')
plt.annotate("B\n({:.1f},{:.1f})".format(-a, -b), (-a, -b), textcoords="offset points", xytext=(20,5), ha='center')
plt.annotate("A\n({:.1f},{:.1f})".format(a, b), (a, b), textcoords="offset points", xytext=(20,5), ha='center')
plt.annotate(f'Norm={vector_norm:.2f}', ((a + (-a)) / 2, (b + (-b)) / 2), textcoords="offset points", xytext=(20,5), ha='center')

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.show()
plt.savefig("/home/aslin-garvasis/Desktop/Assign4/Figs/Fig1.png")

