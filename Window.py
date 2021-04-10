from PyQt5 import QtWidgets
from MayaviQWidget import MayaviQWidget

if __name__ == "__main__":
    # Don't create a new QApplication, it would unhook the Events
    # set by Traits on the existing QApplication. Simply use the
    # '.instance()' method to retrieve the existing one.
    app = QtWidgets.QApplication.instance()
    container = QtWidgets.QWidget()

    mayavi_widget = MayaviQWidget(container)

    container.setWindowTitle("Embedding Mayavi in a PyQt5 Application")
    # define a "complex" layout to test the behaviour
    layout = QtWidgets.QHBoxLayout(container)

    layout.addWidget(mayavi_widget)
    container.show()
    window = QtWidgets.QMainWindow()
    window.setCentralWidget(container)

    mayavi_widget.visualization.animate(mayavi_widget.visualization)

    # window.show()
    window.showMaximized()


    # Start the main event loop.
    app.exec_()

