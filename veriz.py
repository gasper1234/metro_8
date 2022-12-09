import numpy as np
import matplotlib as plt
from numba import njit, vectorize
import time
import matplotlib.pyplot as plt

N = 17

loc_s = np.ones(N)*(-1)


@njit
def E(locations, alpha):
	E = 0
	E += 0.5 * (locations[0]**2 + locations[-1]**2)
	for i in range(len(locations)):
		E += alpha * locations[i]
	for i in range(len(locations)-1):
		E += 0.5 * (locations[i+1]-locations[i])**2
	return E

@njit
def random_E(locations, T, alpha):
	locations_0 = np.copy(locations)
	E_0 = E(locations, alpha)
	loc = np.random.randint(0, high=17)
	diff = np.random.randint(2)
	if diff == 0:
		diff = -1
	locations[loc] += diff
	if locations[loc] < -19: locations[loc] = -19
	Energ = E(locations, alpha)
	if Energ < E_0:
		return locations
	elif Energ-E_0 < -T*np.log(np.random.random()):
		return locations
	else:
		return locations_0

@njit
def loop(locations, N, storage_N, last_N, T=0.2, alpha=1):
	E_s = np.zeros(N)
	last_N *= 100
	bet_sol = np.zeros((storage_N, 17))
	last_sol = np.zeros((last_N//100, 17))
	ind = 0
	for i in range(N):
		locations = random_E(locations, T, alpha)
		E_s[i] = E(locations, alpha)
		if i % (N//storage_N) == 0:
			bet_sol[ind] = locations
			ind += 1
		if i-(N-last_N) >= 0:
			if i-(N-last_N) % 100:
				last_sol[(i-(N-last_N))//100] = locations
	return locations, bet_sol, last_sol, E_s

def connect_s(locations_s):
	all_line_dict = [{} for _ in range(len(locations_s[0])+1)]
	for j in range(len(locations_s)):
		if (0, locations_s[j][0]) in all_line_dict[0]:
			all_line_dict[0][(0, locations_s[j][0])] += 1
		else:
			all_line_dict[0][(0, locations_s[j][0])] = 1
	for i in range(len(locations_s[0])-1):
		for j in range(len(locations_s)):
			if (locations_s[j][i], locations_s[j][i+1]) in all_line_dict[i+1]:
				all_line_dict[i+1][(locations_s[j][i], locations_s[j][i+1])] += 1
			else:
				all_line_dict[i+1][(locations_s[j][i], locations_s[j][i+1])] = 1
	for j in range(len(locations_s)):
		if (locations_s[j][-1], 0) in all_line_dict[-1]:
			all_line_dict[-1][(locations_s[j][-1], 0)] += 1
		else:
			all_line_dict[-1][(locations_s[j][-1], 0)] = 1
	return all_line_dict

def plot_dens(all_line_dict, col):
	for i in range(len(all_line_dict)):
		for j in all_line_dict[i]:
			print(j)
			print(all_line_dict[i][j])
			plt.plot([i, i+1], [j[0], j[1]], color=col, linewidth=all_line_dict[i][j]/300)
	plt.title('T=0.2')
	plt.yticks([-i for i in range(20)])
	plt.xticks([i for i in range(19)])

def plot_ver(locations):
	plt.plot(np.arange(len(locations)), locations, 'x-')
	plt.show()

def plot_E(E_s, t):
	plt.plot(np.arange(len(E_s)), E_s, label=t)

alph_s = [0.4, 1, 4]
color_s = ['blue', 'red', 'black']
for i in range(3):
	sol, mid, last, E_s = loop(loc_s, 1000000, 50, 1000, alpha=alph_s[i])
	slov = connect_s(last)
	#plot_E(E_s, t)
	print(slov)
	plot_dens(slov, color_s[i])
plt.plot([], [], color='blue', label='0.4')
plt.plot([], [], color='red', label='1')
plt.plot([], [], color='black', label='4')
plt.ylabel('E')
#plt.xscale('log')
plt.legend(title=r'$\alpha$')
plt.show()
plot_ver(sol)