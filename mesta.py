import numpy as np
import matplotlib.pyplot as plt
from numba import njit

@njit
def leng(mesta):
	l = 0
	for i in range(len(mesta)):
		l += np.sqrt( (mesta[i-1][0] - mesta[i][0]) ** 2 + (mesta[i-1][1] - mesta[i][1]) ** 2 )
	return l

def D_l(mesta, a, b):
	l = 0
	N = len(mesta)
	l -= np.sqrt( (mesta[a-1][0] - mesta[a][0]) ** 2 + (mesta[a-1][1] - mesta[a][1]) ** 2 ) - np.sqrt( (mesta[a-1][0] - mesta[b][0]) ** 2 + (mesta[a-1][1] - mesta[b][1]) ** 2 )
	l -= np.sqrt( (mesta[b-1][0] - mesta[b][0]) ** 2 + (mesta[b-1][1] - mesta[b][1]) ** 2 ) - np.sqrt( (mesta[b-1][0] - mesta[a][0]) ** 2 + (mesta[b-1][1] - mesta[a][1]) ** 2 )
	if a < N-1:
		if b < N-1:
			l -= np.sqrt( (mesta[a+1][0] - mesta[a][0]) ** 2 + (mesta[a+1][1] - mesta[a][1]) ** 2 ) - np.sqrt( (mesta[a+1][0] - mesta[b][0]) ** 2 + (mesta[a+1][1] - mesta[b][1]) ** 2 )
			l -= np.sqrt( (mesta[b+1][0] - mesta[b][0]) ** 2 + (mesta[b+1][1] - mesta[b][1]) ** 2 ) - np.sqrt( (mesta[b+1][0] - mesta[a][0]) ** 2 + (mesta[b+1][1] - mesta[a][1]) ** 2 )
		else:
			l -= np.sqrt( (mesta[a+1][0] - mesta[a][0]) ** 2 + (mesta[a+1][1] - mesta[a][1]) ** 2 ) - np.sqrt( (mesta[a+1][0] - mesta[b][0]) ** 2 + (mesta[a+1][1] - mesta[b][1]) ** 2 )
			l -= np.sqrt( (mesta[0][0] - mesta[b][0]) ** 2 + (mesta[0][1] - mesta[b][1]) ** 2 ) - np.sqrt( (mesta[0][0] - mesta[a][0]) ** 2 + (mesta[0][1] - mesta[a][1]) ** 2 )
	else:
		l -= np.sqrt( (mesta[0][0] - mesta[a][0]) ** 2 + (mesta[0][1] - mesta[a][1]) ** 2 ) - np.sqrt( (mesta[0][0] - mesta[b][0]) ** 2 + (mesta[0][1] - mesta[b][1]) ** 2 )
		l -= np.sqrt( (mesta[0][0] - mesta[b][0]) ** 2 + (mesta[0][1] - mesta[b][1]) ** 2 ) - np.sqrt( (mesta[0][0] - mesta[a][0]) ** 2 + (mesta[0][1] - mesta[a][1]) ** 2 )
	return l

@njit
def swap_0(mesta_0, a, b):
	mesta = np.copy(mesta_0)
	N = len(mesta)
	dif = abs(a-b)
	dif_1 = abs(a-b+N)
	dif_2 = abs(a-b-N)
	n = int(abs(np.floor(np.log(np.random.random()))))
	if n < dif and n < dif_1 and n < dif_2:
		for i in range(n):
			ind_a = i+a
			if ind_a >= N:
				ind_a = ind_a % N
			change_a = mesta_0[ind_a]
			ind_b = i+b
			if ind_b >= N:
				ind_b = ind_b % N
			change_b = mesta_0[ind_b]
			mesta[ind_a] = change_b
			mesta[ind_b] = change_a
	else:
		change_b = mesta_0[b]
		change_a = mesta_0[a]
		mesta[a] = change_b
		mesta[b] = change_a
	return mesta

@njit
def swap(mesta, T):
	l_0 = leng(mesta)
	N = len(mesta)
	a = np.random.randint(N)
	b = np.random.randint(N)
	if a == b:
		return mesta
	mesta_1 = swap_0(mesta, a, b)
	l_1 = leng(mesta_1)
	D_E = l_1 - l_0
	if D_E < 0:
		return mesta_1
	log_val = -T*np.log(np.random.random())
	if D_E < log_val:
		return mesta_1
	return mesta

@njit
def time(grid, t, T=2, store_t=None):
	if store_t == None:
		store_t = t//len(grid)
	grid_s = np.zeros((store_t, len(grid), 2))
	ind = 0
	for i in range(t):
		grid = swap(grid, T)
		if i%(t//store_t) == 0:
			grid_s[ind] = grid
			ind += 1
	return grid_s


