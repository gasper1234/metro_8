from spin_mag import *

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
T_s = [1, 2, 3, 4]
for i in range(4):
	print(i)
	grid_s = time(grid, 10**4//2, T=T_s[i], store_t=10**3)
	plot_E(grid_s, ax0, T_s[i])
	ax0.legend(title='T')
	ax0.set_xlabel('t')
	ax0.set_ylabel('E')
	axes[i].imshow(grid_s[-1], cmap='Greys')
	axes[i].set_title('T='+str(T_s[i]))

plt.show()