from spin_TF import *

dim = 100


grid = np.array([[True for _ in range(dim)] for _ in range(dim)]).astype(bool)
for k in range(len(grid)):
	for j in range(len(grid)):
		if (k+j) % 2 == 0:
			grid[k, j] = not grid[k, j]


fig = plt.figure()
spec = fig.add_gridspec(3, 2)
ax0 = fig.add_subplot(spec[2, :])
axes = [fig.add_subplot(spec[i//2, i%2]) for i in range(4)]
n_i = 40
T_s = [i/n_i*4 for i in range(n_i)]
E_s = []
S_s = []
for i in range(len(T_s)):
	print(i)
	grid_s = time(grid, 10**7//2, T=T_s[i], store_t=10**3)
	E_s.append(E_grid(grid_s[-1]))
	S_s.append(S_grid(grid_s[-1]))

print(E_s)
print(S_s)
print(T_s)