class Transport:
    def start(self):
        pass
    def move(self):
        pass
    def stop(self):
        pass


class Rocket(Transport):
    def start(self):
        print('rocket launched')
    def set_height(self, h):
        print(f'the flight is at altitude {h} kilometers')
    def landing(self):
        print('the rocket landed')

class Tiltrotor(Transport):
    def start(self):
        print('tiltrotor launched')
    def set_height(self, h):
        print(f'the flight is at altitude {h} kilometers')
    def landing(self):
        print('the tiltrotor landed')

