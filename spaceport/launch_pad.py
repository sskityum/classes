class LaunchPad:
    def __init__(self, coordinates, launcher):
        self.coordinates = coordinates
        self.launcher = launcher

    def launcher_start(self):
        self.launcher.start()

    def launcher_height(self, h):
        self.launcher.set_height(h)

    def launcher_landing(self):
        self.launcher.landing()