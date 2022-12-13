from spin_mag import *

dim = 100

import statistics

grid = np.array([[True for _ in range(dim)] for _ in range(dim)]).astype(bool)
for k in range(len(grid)):
	for j in range(len(grid)):
		if (k+j) % 2 == 0:
			grid[k, j] = not grid[k, j]

var_s = []
H_val_s = [0.02*i for i in range(1, 50)]
for H_val in H_val_s:
	grid_s = time(grid, 10**7, T=3, H=H_val, store_t=10**3)
	E_s = [E_grid(grid_s[i], H=H_val) for i in range(10**3)]

	var_s.append(statistics.variance(E_s[200:]))	

print(var_s)
plt.plot(H_val_s, var_s)
plt.show()