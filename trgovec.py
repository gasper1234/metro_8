from mesta import *
from matplotlib import gridspec

N = 100
T_val = 0.01


mesta = np.zeros((N, 2))

for i in range(N):
	mesta[i][0] = np.random.random()
	mesta[i][1] = np.random.random()


store_t_val = 100000
mesta_s = time(mesta, 10**8, T=T_val, store_t=store_t_val)


fig = plt.figure(figsize=(6, 8)) 
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 2]) 
ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])
ax0.set_title('T='+str(T_val))
ax0.set_ylabel('l')

E_s = [leng(i) for i in mesta_s]
t_s = [i for i in range(store_t_val)]
min_val = E_s[0]
for i in range(len(E_s)):
	if E_s[i] < min_val:
		min_val = E_s[i]
		ind = i

ax0.plot(t_s, E_s)



for i in range(N):
	ax1.plot([mesta_s[ind][i-1][0], mesta_s[ind][i][0]], [mesta_s[ind][i-1][1], mesta_s[ind][i][1]], 'ko-')
	ax1.axis('equal')
	#ax1.set_xlim(-0.05, 1.05)
	#ax1.set_ylim(-0.05, 1.05)

plt.show()
