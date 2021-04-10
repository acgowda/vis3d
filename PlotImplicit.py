import numpy as np
from mayavi import mlab


class PlotImplicit:

    def __init__(self, f, w, r):
        self.res = 100
        self.w = w

        x, y, z = np.mgrid[-r:r:(self.res * 1j), -r:r:(self.res * 1j), -r:r:(self.res * 1j)]

        self.F = eval(f)
        self.s = mlab.contour3d(self.F, contours=[0])
        self.s.scene.show_axes = True

    # Ask the user for the equation.
    # Ex.
    # x**2 + y**2 + z**2
    # (x**2)/4 - (y**2)/4 - z/4

    @mlab.animate(delay=10)
    def animate(self):
        for W in np.linspace(self.w, -self.w, self.res * 5):
            self.s.mlab_source.set(scalars=self.F + W)
            yield

        self.s.mlab_source.set(scalars=self.F)


User_F = input("Enter your implicit function: ")
wrange = int(input("Enter the range of the w value: "))
xyzrange = int(input("Enter the range of the x, y, and z values: "))

G = PlotImplicit(User_F, wrange, xyzrange)
G.animate(G)

mlab.show()
