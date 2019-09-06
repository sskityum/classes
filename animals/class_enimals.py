class Enimals:
    def __init__(self, paws, tail, ears, wool_coating):
        self.paws = paws            # лапы
        self.tail = tail            # хвост
        self.ears = ears            # уши
        self.wool_coating = wool_coating            # волосяное покрытие
        self.__position = 0

    def make_sound(self):           # издавать звук
        print('arrr...')

    def move(self):                  # передвигаться
        if self.paws == 2:
            print('я летаю или прыгаю и хожу по земле!')
        else:
            print('я бегаю, прыгаю, ползаю, нах!')

    def freeze(self):               # замирать
        print('я замер')            

    def sleep(self):                # спать
        print('тссс, я сплю')

    def eat(self):                  # есть
        print('я ем')

    def detect_enemy(self, animal):
        try:
            animal.move()
            
            print('Ok :),- The duck typing principle applies!')
            return True

        except:
            print('SSSSS!!! >.<')
            return False


class Cat(Enimals):
    def __init__(self, paws, tail, ears, wool_coating, mustache, name):
        super().__init__(paws, tail, ears, wool_coating)
        self.mustache = mustache    # усы
        self.name = name            # имя

    def make_sound(self):           # издавать звук
        print('myau-u-u-u...')

class Dog(Cat):
    def __init__(self, paws, tail, ears, wool_coating, mustache, name):
        super().__init__(paws, tail, ears, wool_coating, mustache, name)

    def make_sound(self):           # издавать звук
        print('gav gav...')

class Bird(Enimals):
    def __init__(self, paws, tail, ears, wool_coating, wings, name):
        super().__init__( paws, tail, ears, wool_coating)
        self.wings = wings
        self.name = name            # имя

    def make_sound(self):           # издавать звук
        print('ku ku...')

class Insect:
    def __init__(self, paws, eyes):
        self.paws = paws
        self.eyes = eyes

    def moves(self):
        print('я ползаю с помощью 40 ножек и не запуталась ни разу')