from animals import Bird
from equipment import Transport, Rocket, Tiltrotor
from launch_pad import LaunchPad
from strange_machine import ufo

rocket = Rocket()
tiltrotor = Tiltrotor()
bird = Bird()
launchPad = LaunchPad([100, 500], ufo)

# rocket.start()
# rocket.set_height(400)
# rocket.landing()
# tiltrotor.start()
# tiltrotor.set_height(8)
# tiltrotor.landing()
# bird.start()
# bird.set_height(3)
# bird.landing()
launchPad.launcher_start()
launchPad.launcher_height(3000000)
launchPad.launcher_landing()