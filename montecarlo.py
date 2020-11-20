# import important modules
import math as M
import random as r

# Function to calculate kwarter of a cirkel
def f(x):
    y = M.sqrt(1-x**2)
    return y

# define domain and range
x_min = 0
x_max = 1
y_min = 0
y_max = 1

# calculate area box for given domain
area_box = (x_max-x_min)*(y_max-y_min)

# generate random points and check if in or out area
inside, outside = 0, 0
for i in range(1000000):
    P = (r.uniform(x_min, x_max),r.uniform(y_min, y_max))
    if P[1] < f(P[0]):
         inside += 1
    else: outside += 1

# calculate area under function f(x)
area = inside/(outside+inside) * area_box

print(area)
