class Animal:
    def __init__(self, name, make_sound_metod):
        self. name = name
        self.make_sound_metod = make_sound_metod

def quack():
        print('kwa')

def moo():
        print("Mu")

def bah():
        print("Bah")

bah = Animal("owca", quack)
bah.make_sound_metod()