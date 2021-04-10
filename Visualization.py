import numpy as np
import time
from mayavi import mlab
from traits.api import HasTraits, Instance, on_trait_change, Range
from traitsui.api import View, Item, Group
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, SceneEditor


class Visualization(HasTraits):
    scene = Instance(MlabSceneModel, ())

    # Ask the user for the equation.
    # Ex.
    # x**2 + y**2 + z**2
    # x**2 + y**2 + z**2 + np.sin(x*y)
    # (x**2)/4 - (y**2)/4 - z/4

    user_f = input("Enter your implicit function: ")
    w = float(input("Enter the range of the function (Choose a number from 1-5 for the best results): "))
    W = Range(low=-w, high=w, value=0)

    def __init__(self):
        super().__init__()

        res = 100
        xyzres = res * 1j
        self.wres = res * 5

        r = self.w # int(input("Enter the range of the x, y, and z values: "))

        x, y, z = np.ogrid[-r:r:xyzres, -r:r:xyzres, -r:r:xyzres]
        self.F = eval(self.user_f)

        self.s = self.scene.mlab.contour3d(self.F, contours=[1])

    def setZoom(self):
        self.W = 0
        self.scene.scene_editor.reset_zoom()

    @mlab.animate(delay=10)
    def animate(self):
        for i in np.linspace(-self.w, self.w, self.wres):
            self.W = i
            if i == -self.w:
                self.setZoom()
            # self.s.mlab_source.set(scalars=self.F + i)
            yield

        self.W = 0
        # self.s.mlab_source.set(scalars=self.F)

    @on_trait_change('scene.activated')
    def change_view(self):
        self.scene._update_view(1, 1, 1, 0, 0, 1)
        self.scene.scene_editor.reset_zoom()
        self.scene.mlab.orientation_axes()

    @on_trait_change('W')
    def update_plot(self):
        self.s.mlab_source.set(scalars=self.F - self.W)

    # the layout of the dialog created
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=1080, width=1920, show_label=False), Group('_', 'W'),
                resizable=True)
