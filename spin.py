import numpy as np
import matplotlib as plt
from numba import njit, vectorize
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def E_grid(grid):
	l = len(grid)-1
	J = 1
	E = 0
	# zadnja vrsta
	for i in range(len(grid)-1):
		E += grid[l,i]*grid[l-1,i] + grid[l,i]*grid[0,i]+ grid[l,i]*grid[l,i-1]+ grid[l,i]*grid[l,i+1]
	# zadnji elem
	E += grid[l,l]*grid[l,l-1] + grid[l,l]*grid[l-1,l]+ grid[l,l]*grid[l,0]+ grid[l,l]*grid[0,l]
	for i in range(len(grid)-1):
		for j in range(len(grid)-1):
			E += grid[i,j]*grid[i-1,j] + grid[i,j]*grid[i+1,j]+ grid[i,j]*grid[i,j+1]+ grid[i,j]*grid[i,j-1]
	#zadnji stolpec
	for i in range(len(grid)-1):
		E += grid[i,l]*grid[i,l-1] + grid[i,l]*grid[i,0]+ grid[i,l]*grid[i-1,l]+ grid[i,l]*grid[i+1,l]
	return E

@njit
def D_E(grid, loc):
	l = len(grid)-1
	i, j = loc[0], loc[1]
	loc_state = grid[i,j]*(-1)
	if i < l:
		if j < l:
			E = loc_state*grid[i-1,j] + loc_state*grid[i+1,j]+ loc_state*grid[i,j+1]+ loc_state*grid[i,j-1]
		else:
			E = loc_state*grid[i,l-1] + loc_state*grid[i,0]+ loc_state*grid[i-1,l]+ loc_state*grid[i+1,l]
	else:
		if j < l:
			E = loc_state*grid[l-1,j] + loc_state*grid[0,j]+ loc_state*grid[l,j-1]+ loc_state*grid[l,j+1]
		else:
			E = loc_state*grid[l,l-1] + loc_state*grid[l-1,l]+ loc_state*grid[l,0]+ loc_state*grid[0,l]
	return E

def swap(grid, T):
	l = len(grid)
	loc = np.random.randint(l, size=2)
	if 2*D_E(grid, loc) < 0:
		grid[loc[0], loc[1]] *= -1
	elif 2*D_E(grid, loc) < -T*np.log(np.random.random()):
		grid[loc[0], loc[1]] *= -1
	return grid

def time(grid, t, T=2, store_t=None):
	if store_t == None:
		store_t = t//len(grid)
	grid_s = np.zeros((store_t, len(grid), len(grid)))
	ind = 0
	for i in range(t):
		grid = swap(grid, T)
		if i%(t//store_t) == 0:
			grid_s[ind] = grid
			ind += 1
	return grid_s