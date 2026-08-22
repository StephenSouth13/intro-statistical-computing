import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

doanhThu = np.array([100, 200, 300, 400, 500])
chiPhi = np.array([50, 150, 250, 350, 450])

# z = x^2 - y^2 ==> Vẽ biểu đồ 3D
x, y = np.meshgrid(doanhThu, chiPhi)
z = x**2 - y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k', alpha=0.8)
ax.set_xlabel('doanhThu')
ax.set_ylabel('chiPhi')
ax.set_zlabel('z = x^2 - y^2')
plt.show()