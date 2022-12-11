import numpy as np
import matplotlib.pyplot as plt

E_1 = np.array([-34.9194,  -34.81484, -35.27542, -35.00384, -35.2089,  -35.70396, -36.01328, -36.05248, -35.62752])
S_1 = np.array([-8.86,  -9.158, -9.286, -9.254, -9.302, -9.434, -9.496, -9.544, -9.472])
kappa_1 = np.array([-392.448, -419.29482, -431.09898, -428.13258, -432.58602, -444.95178, -450.82008, -455.38968, -448.54392])
c_1 = np.array([-3048.0092384 , -3029.77870057, -3110.48211794, -3062.76399686, -3098.75653552, -3186.51980921, -3241.9767184, -3249.03712537, -3172.88225088])
E_2 = np.array([-15.3656, -17.00776, -17.34272, -17.27696, -17.2902, -18.193, -18.77582, -19.516, -19.64628])
S_2 = np.array([-0.44, -1.812, -2.976, -2.576, -3.476, -3.65, -4.374, -5., -5.108])
kappa_2 = np.array([-0.612, -10.91114667, -29.48858667, -22.08592, -40.24192, -44.375, -63.73958667, -83.3, -86.93888])
c_2 = np.array([-262.15651373, -321.22477358, -334.00836444, -331.47792316, -331.9855456, -367.57823667, -391.51751964, -423.00865778, -428.6767076])

E_1 = np.array([-34724.27999998172, -35214.84000002964, -34936.38000001077, -35025.43999999191, -35394.6999999728, -35620.36000002187, -35758.88000000274, -35519.11999998352, -35720.9800000331])/1000
S_1 = np.array([-8972, -9258, -9254, -9264, -9346, -9394, -9416, -9436, -9478])/1000
kappa_1 = np.array([97516.08, 71447.18, 71817.42, 70891.52, 63261.42, 58763.82, 56694.72, 54809.52, 50837.58])/1000
c_1 = np.array([1005585.9462071728, 939887.6094307804, 1008848.3812371189, 1013446.3820174164, 968663.0297798138, 948874.8836721033, 944481.2528635109, 1007580.2860669261, 992053.9695930874])/1000
E_2 = np.array([-15660.119999999872, -16047.919999999562, -16666.760000002454, -17063.51999999772, -17796.00000000259, -18050.959999995175, -18776.380000001387, -19118.07999999149, -19477.679999999265])/1000
S_1 = np.array([-588, -1004, -2108, -2612, -3560, -3684, -4766, -4874, -5048])/1000
kappa_2 = np.array([332180.85333333333, 329973.27999999997, 318521.12, 310591.52, 291088.0, 288093.8133333333, 257617.47999999998, 254147.08, 248392.31999999998])/1000
c_2 = np.array([1514189.6017617818, 1509449.1818595708, 1495899.0123359095, 1489995.8724551976, 1470613.7599998976, 1469469.8256428596, 1448819.504550609, 1443487.7967932504, 1437144.4242418092])/1000

H_s = np.array([0.01 * i for i in range(1, 10)])

fig, ax = plt.subplots(2, 2)
ax[0][0].plot(H_s, c_1, 'x')
ax[0][1].plot(H_s, c_2, 'x')
ax[1][0].plot(H_s, kappa_1, 'x')
ax[1][1].plot(H_s, kappa_2, 'x')
ax[1][1].set_xlabel('H')
ax[1][0].set_xlabel('H')
ax[0][0].set_ylabel('c')
ax[1][0].set_ylabel(r'$\chi$')
ax[0][1].set_title('T=3')
ax[0][0].set_title('T=2')

#nevem če je ok

plt.show()