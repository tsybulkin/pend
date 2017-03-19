#
# pendulum
#
# d2a/dt2 = 3/2 * g/L * sin(a) + 3/(m*L**2)*U

from matplotlib import pyplot as plt
import numpy as np
import sys


TAU = 0.001
U_MAX = 2.
G = 9.81
m = 1.
L = 1.
Et = 0.97*m*G*L/2


def control(a,da):
	#return lim(U_MAX, 0.3 * np.sign(da))

	E = m*(L*da)**2/6 + m*G*L/2*np.cos(a)	
	if E < Et:
		return lim(U_MAX, 0.3 * np.sign(da))
	elif abs(a) < 0.5:
		return lim(U_MAX, -9.1*a - 3.*da)
	elif abs(2*np.pi - a) < 0.5:
		return lim(U_MAX, -10.1*(a-6.28) - 2.8*da)
	return 0.


def run(T=1):
	t = 0
	a = np.pi + np.random.random()
	da = 0.
	log = []
	
	while t < T:
		u = control(a,da)
		a,da = dynamics(a,da,u,TAU) 
		log.append((t,a,da,u))
		t += TAU

	[Ti, A, dA, U] = zip(*log)
	#plt.plot(Ti, A, '--')
	plt.scatter(A,dA)
	plt.grid(True)
	plt.show()



def lim(LIM, val):
	if val < - LIM: return -LIM
	elif val > LIM: return LIM
	return val


def dynamics(a,da,u,tau):
	da += (3*G/(2*L) * np.sin(a) + 3/(m*L**2)*u)*tau
	a += da * tau
	return a, da


if __name__ == '__main__':
	args = sys.argv[:]
	if len(args) == 2:
		run(float(args[1]))
	else:
		run()

