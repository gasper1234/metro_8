from spin_mag import *

dim = 100


grid = np.array([[True for _ in range(dim)] for _ in range(dim)]).astype(bool)
for k in range(len(grid)):
	for j in range(len(grid)):
		if (k+j) % 2 == 0:
			grid[k, j] = not grid[k, j]

H_s = [0.01 * i for i in range(1, 100)]
E_s = []
S_s = []
kappa_s = []
c_s = []
T_s = [2, 3]
for T in T_s:
	E_s = []
	S_s = []
	kappa_s = []
	c_s = []
	for h in H_s:
		grid_s = time(grid, 10**7, T, H=h, store_t=10**3)
		E_s.append(E_grid(grid_s[-1], h))
		S_s.append(S_grid(grid_s[-1]))
		kappa_s.append(kappa(grid_s[-1], T))
		c_s.append(c_heat(grid_s[-1], T, h))

	#E_s = np.array(E_s)/1000
	#S_s = np.array(S_s)/1000
	#kappa_s = np.array(kappa_s)/1000
	#c_s = np.array(c_s)/1000

	print('E_s = np.array(', E_s, ')')
	print('S_s = np.array(', S_s, ')')
	print('kappa_s = np.array(', kappa_s, ')')
	print('c_s = np.array(', c_s, ')')

'''
plt.xlabel('t')
plt.ylabel('E')
plt.text(-0.1, 9.7, r'$1\mathrm{e}3$')
plt.text(3.8, 9.7, r'$1\mathrm{e}3$')
plt.plot(H_s, E_s)

plt.show()
'''