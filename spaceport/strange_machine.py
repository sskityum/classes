from collections import namedtuple

UFO = namedtuple('UFO', 'start set_height landing')

def ufo_start():
    print('an unidentified flying object flew away, but promised to return...')
def ufo_set_height(h):
    print(f'the flight is at altitude {h} kilometers')
def ufo_landing():
    print('он вернулся ?! ...')

ufo = UFO(
    ufo_start,
    ufo_set_height,
    ufo_landing
)