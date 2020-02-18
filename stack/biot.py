import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

I = 1
u0 = 4e-7 * np.pi


def pointB(angle1, angle2, distance):
    return u0 * I / (4 * np.pi * distance / 100) * \
        (np.cos(angle1) - np.cos(angle2))


x = np.linspace(0, 3, 1001)
y = np.linspace(0, 3, 1001)
[x, y] = np.meshgrid(x, y)

corners = [(1, 1), (1, 2), (2, 2), (2, 1)]


B = pointB(np.arctan2((x - 1), (y - 1)),
           np.arctan2((x - 1), (y - 2)), (x - 1)) - \
    pointB(np.arctan2((x - 2), (y - 1)),
           np.arctan2((x - 2), (y - 2)), (x - 2)) + \
    pointB(np.arctan2((y - 1), (x - 1)),
           np.arctan2((y - 1), (x - 2)), (y - 1)) - \
    pointB(np.arctan2((y - 2), (x - 1)),
           np.arctan2((y - 2), (x - 2)), (y - 2))

B[333:667, 333:667] *= -1
B *= -1
# B[:, 331:334] = np.nan
# B[:, 665:668] = np.nan
# B[331:334, :] = np.nan
# B[665:668, :] = np.nan


#
# fig, (ax0, ax1, ax01) = plt.subplots(ncols=3)
# ax0.imshow(np.arctan2((x - 1), (y - 1)))
# ax1.imshow(np.arctan2((x - 1), (y - 2)))
# ax01.imshow((np.cos(np.arctan2((x - 1), (y - 1))) -
#             np.cos(np.arctan2((x - 1), (y - 2)))/(x - 1)))
#
# fig, (ax2, ax3, ax23) = plt.subplots(ncols=3)
# ax2.imshow(np.arctan2((x - 2), (y - 1)))
# ax3.imshow(np.arctan2((x - 2), (y - 2)))
# ax23.imshow((np.cos(np.arctan2((x - 2), (y - 1))) -
#             np.cos(np.arctan2((x - 2), (y - 2)))/(x - 2)))
#
#
# fig, (ax4, ax5, ax45) = plt.subplots(ncols=3)
# ax4.imshow(np.arctan2((y - 1), (x - 1)))
# ax5.imshow(np.arctan2((y - 1), (x - 2)))
# ax45.imshow((np.cos(np.arctan2((y - 1), (x - 1))) -
#             np.cos(np.arctan2((y - 1), (x - 2)))/(y - 1)))
#
# fig, (ax6, ax7, ax67) = plt.subplots(ncols=3)
# ax6.imshow(np.arctan2((y - 2), (x - 1)))
# ax7.imshow(np.arctan2((y - 2), (x - 2)))
# ax67.imshow((np.cos(np.arctan2((y - 2), (x - 1))) -
#             np.cos(np.arctan2((y - 2), (x - 2)))/(y - 2)))


fig, ax0 = plt.subplots()
im = ax0.imshow(np.log10(B), extent=[0, 3, 0, 3])
cb = fig.colorbar(im, ax=ax0)
cb.set_label("Logarithmic magnetic filed [log10(B)]")


ax0.set_title('Magnetic field in a square loop - current 1A')
ax0.set_xlabel("x coordinates [cm]")
ax0.set_ylabel("y coordinates [cm]")

plt.savefig("images/B.png")


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, np.log10(np.abs(B)), cmap=plt.cm.viridis)
plt.savefig("images/B-3d.png")

# fig, (ax0, ax1) = plt.subplots(ncols=2)
#
# cax0 = ax0.imshow(np.arctan((x - 1) / (y - 1)))
# cax1 = ax1.imshow(np.arctan((x - 1) / (y - 2)))
#
# fig.colorbar(cax0, ax=ax0)
# fig.colorbar(cax1, ax=ax1)


# fig, ((axC1a, axC1b), (axC1c, axC1d)) = plt.subplots(nrows=2, ncols=2)
# caxC1a = axC1a.imshow((np.cos(np.arctan2((x - 1), (y - 1)))))
# caxC1b = axC1b.imshow((np.cos(np.arctan2((x - 1), (y - 2)))))
# caxC1c = axC1c.imshow(np.arctan2((x - 1), (y - 1)))
# caxC1d = axC1d.imshow(np.arctan2((x - 1), (y - 2)))
#
# fig.colorbar(caxC1a, ax=axC1a)
# fig.colorbar(caxC1a, ax=axC1b)

# fig, axC1 = plt.subplots()
# caxC1 = axC1.imshow((np.cos(np.arctan2((x - 1) , (y - 1)))-np.cos(np.arctan2((x - 1) , (y - 2)))))
#
# fig.colorbar(caxC1, ax=axC1)
#
#
# fig, axC2 = plt.subplots()
# caxC2 = axC2.imshow((np.cos(np.arctan2((x - 2) , (y - 1)))-np.cos(np.arctan2((x - 2) , (y - 2)))))
#
# fig.colorbar(caxC2, ax=axC2)
#
# fig, axC3 = plt.subplots()
# caxC3 = axC3.imshow((np.cos(np.arctan2((y - 1) , (x - 1)))-np.cos(np.arctan2((y - 1) , (x - 2)))))
#
# fig.colorbar(caxC3, ax=axC3)
#
# fig, axC4 = plt.subplots()
# caxC4 = axC4.imshow((np.cos(np.arctan2((y - 2) , (x - 1)))-np.cos(np.arctan2((y - 2) , (x - 2)))))
#
# fig.colorbar(caxC4, ax=axC4)

plt.show()
