from class_enimals import Enimals, Cat, Dog, Bird
from class_enimals import Insect

murzik = Cat(4, 1, 2, 'wool', 30, 'Murzilka')

enimal = Enimals(4, 1, 2, 'wool_coating')

sharik = Dog(4, 1, 2, 'wool', 20, 'Sharik')

bird = Bird(2, 1, 2, 'перья', 2, 'Popka')

insect = Insect(40, 60)

if __name__ == '__main__':
    # print(murzik.name)
    # murzik.make_sound()
    # murzik.sleep()
    # murzik.move()
    # print(sharik.name)
    # sharik.make_sound()
    # sharik.sleep()
    # sharik.move()
    # print(bird.name)
    # bird.make_sound()
    # bird.sleep()
    # bird.move()
    # bird.freeze()
    # bird.eat()
    bird.detect_enemy(insect)
    insect.moves()



