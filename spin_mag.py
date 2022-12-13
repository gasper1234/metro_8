import numpy as np
import matplotlib as plt
from numba import njit, vectorize
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

@njit
def T_F_int(T, F):
	if T != F:
		return 1
	else:
		return -1

# implement field
@njit
def E_grid(grid, H):
	l = len(grid)-1
	J = 1
	E = 0
	# zadnja vrsta
	for i in range(len(grid)-1):
		E += T_F_int(grid[l,i],grid[i,l-1]) + T_F_int(grid[l,i],grid[i,0])+ T_F_int(grid[l,i],grid[i-1,l])+ T_F_int(grid[l,i],grid[i+1,l])
	# zadnji elem
	E += T_F_int(grid[l,l],grid[l,l-1]) + T_F_int(grid[l,l],grid[l-1,l])+ T_F_int(grid[l,l],grid[l,0])+ T_F_int(grid[l,l],grid[0,l])
	for i in range(len(grid)-1):
		for j in range(len(grid)-1):
			E += T_F_int(grid[i,j],grid[i-1,j]) + T_F_int(grid[i,j],grid[i+1,j])+ T_F_int(grid[i,j],grid[i,j+1])+ T_F_int(grid[i,j],grid[i,j-1])
	#zadnji stolpec
	for i in range(len(grid)-1):
		E += T_F_int(grid[i,l],grid[l-1,j]) + T_F_int(grid[i,l],grid[0,j])+ T_F_int(grid[i,l],grid[l,j-1])+ T_F_int(grid[i,l],grid[l,j+1])
	for i in range(l+1):
		for j in range(l+1):
			if grid[i,j]:
				E -= H
			else:
				E += H
	return E

# spin
def S_grid(grid):
	S = 0
	for i in range(len(grid)):
		for j in range(len(grid)):
			if grid[i, j]:
				S += 1
			else:
				S += -1
	return S

def kappa(grid, T):
	N = len(grid)
	return (N**4 - S_grid(grid)**2)/N**2/T

def c_heat(grid, T, H):
	N = len(grid)
	return ((4+H)**2 * N**4 - E_grid(grid, H)**2)/T**2/N**2


@njit
def D_E(grid, loc, H):
	l = len(grid)-1
	i, j = loc[0], loc[1]
	loc_state = not grid[i,j]
	if i < l:
		if j < l:
			E = T_F_int(loc_state,grid[i-1,j]) + T_F_int(loc_state,grid[i+1,j])+ T_F_int(loc_state,grid[i,j+1])+ T_F_int(loc_state,grid[i,j-1])
		else:
			E = T_F_int(loc_state,grid[i,l-1]) + T_F_int(loc_state,grid[i,0])+ T_F_int(loc_state,grid[i-1,l])+ T_F_int(loc_state,grid[i+1,l])
	else:
		if j < l:
			E = T_F_int(loc_state,grid[l-1,j]) + T_F_int(loc_state,grid[0,j])+ T_F_int(loc_state,grid[l,j-1])+ T_F_int(loc_state,grid[l,j+1])
		else:
			E = T_F_int(loc_state,grid[l,l-1]) + T_F_int(loc_state,grid[l-1,l])+ T_F_int(loc_state,grid[l,0])+ T_F_int(loc_state,grid[0,l])
	if grid[i, j]:
		E -= 2*H
	else:
		E += 2*H
	return E

@njit
def swap(grid, T, H):
	l = len(grid)
	rand_1 = np.random.randint(l)
	rand_2 = np.random.randint(l)
	loc = np.array([rand_1, rand_2])
	delta_E = 2*D_E(grid, loc, H)
	if delta_E < 0:
		grid[loc[0], loc[1]] = not grid[loc[0], loc[1]]
	elif delta_E < -T*np.log(np.random.random()):
		grid[loc[0], loc[1]] = not grid[loc[0], loc[1]]
	return grid

@njit
def time(grid, t, T=2, H=0, store_t=None):
	if store_t == None:
		store_t = t//len(grid)
	grid_s = np.zeros((store_t, len(grid), len(grid)))
	ind = 0
	for i in range(t):
		grid = swap(grid, T, H)
		if i%(t//store_t) == 0:
			grid_s[ind] = grid
			ind += 1
	return grid_s

def plot_E(grid_s, ax, lab):
	E_s = [E_grid(grid_s[i]) for i in range(len(grid_s))]
	t_s = np.arange(len(grid_s))
	ax.plot(t_s, E_s, label=lab)