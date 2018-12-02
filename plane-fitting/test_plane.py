import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



def rightPowerPlane(x, y):
    if x >= 0:
        if y >= 0:
            z = y - x
        elif y >= -x:
            z = -x - y
        else:
            z = x + y
    else:
        if y >= -x:
            z = y
        elif y >= 0:
            z = -x
        elif y >= x:
            z = (2 * y) - x
        else:
            z = y

    return z

def getPower(x, y):
    l = rightPowerPlane(-x, y)
    r = rightPowerPlane(x, y)

    return l, r

plt.figure()
ax = plt.subplot(121, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

X,Y = np.meshgrid(np.arange(-1,1,0.02),np.arange(-1,1,0.02))

L = np.zeros(X.shape)
R = np.zeros(X.shape)
for r in range(X.shape[0]):
    for c in range(X.shape[1]):
        L[r,c],R[r,c] = getPower(X[r,c],Y[r,c])
# ax.plot_wireframe(X,Y,L, color='k')

# plt.show()
ax.plot_wireframe(X,Y,L, color='k')

bx = plt.subplot(122, projection='3d')
bx.set_xlabel('x')
bx.set_ylabel('y')
bx.set_zlabel('z')

# plt.show()
bx.plot_wireframe(X,Y,R, color='k')

plt.show()


# plot raw data
# plt.figure()
# ax = plt.subplot(111, projection='3d')
# ax.scatter(xs, ys, zs, color='b')

# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('l')
# plt.show()
# exit()

# print(getPower(-0.7, 0.7))
