
class Character(object):
    class_name = 'Character'

    def __init__(self, position=(0.0, 0.0)):
        self.health = 100
        self.stamina = 100
        self.position = position

    @classmethod
    def get_character_class(cls):
        return cls.class_name

    def __del__(self):
        print 'I\'m dying!!!'

    def report(self):
        print 'Health: %i\nStamina: %i\nPosition: (%f,%f)' % \
              (self.health, self.stamina, self.position[0], self.position[1])

    def move(self, offset):
        self.position = (self.position[0] + offset[0], self.position[1] + offset[1])

    def attack(self, enemy):
        pass


class Player(Character):
    class_name = 'Player'

    def __init__(self, name, position=(0.0, 0.0)):
        super(Player, self).__init__(position=position)
        self.name = name

    def __del__(self):
        super(Player, self).__del__()
        print 'My name was %s.' % self.name

    def report(self):
        print 'Name: %s' % self.name
        super(Player, self).report()


class Npc(Character):
    class_name = 'Npc'


def main():
    player = Player('Covid')
    enemy = Npc()

    enemy.move((2.5, 4.5))
    enemy.report()

    player.move((2.5, 5.5))
    player.report()


main()
print 'Finished!'


