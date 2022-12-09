from spin import *

def animate(n):
	ax.imshow(grid_s[n])

ani = animation.FuncAnimation(fig, animate, frames = len(grid_s), repeat = True)
ani.save('im_vecna_napredno.gif')
plt.show()