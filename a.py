import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
new_x = x.reshape(2, -1)
new_y = x.reshape(3, -1)
# print(new_x)
print(new_y)