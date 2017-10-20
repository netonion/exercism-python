from string import ascii_uppercase
from random import choice

class Robot(object):
    names = set()

    def __init__(self):
        self.set_name()

    def set_name(self):
        self.name = self.gen_name()
        while self.name in Robot.names:
            self.name = self.gen_name()
        Robot.names.add(self.name)

    def reset(self):
        self.set_name()

    def gen_name(self):
        return "{}{}{:03d}".format(choice(ascii_uppercase), choice(ascii_uppercase), random.randint(0, 999))
