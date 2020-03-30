Weapons = {
    'fist': 5,
    'knife': 20,
    'gun': 50
}


class Character(object):
    class_name = 'Character'

    def __init__(self, attack=0, weapon='fist', position=(0.0, 0.0)):
        self.health = 100
        self.stamina = 100
        self.position = position
        # self.attack = attack
        self.weapon = weapon

    def __del__(self):
        # print 'I\'m dying!!!'
        pass

    def report(self):
        print 'Health: %i\nStamina: %i\nPosition: (%f,%f)' % \
              (self.health, self.stamina, self.position[0], self.position[1])

    def move(self, offset):
        self.position = (self.position[0] + offset[0], self.position[1] + offset[1])


class Player(Character):
    class_name = 'Player'

    def __init__(self, name, attack=0, weapon='fist', position=(0.0, 0.0)):
        super(Player, self).__init__(attack=attack, weapon=weapon, position=position)
        self.name = name
        self.attack = Weapons[self.weapon]

    def __del__(self):
        super(Player, self).__del__()
        # print 'My name was %s.' % self.name
        pass

    def report(self):
        print 'Name: %s' % self.name
        # super(Player, self).report()
        print 'Fight with : %s / damage : %i' % (self.weapon, Weapons[self.weapon])


def fight(char1, char2):
    count = 0
    while char1.health > 0 and char2.health > 0:
        count += 1
        char1.health -= char2.attack
        char2.health -= char1.attack
        print 'round ' + str(count) + ' : ' + char1.name + ' health : ' + str(
            char1.health) + ' / ' + char2.name + ' health : ' + str(char2.health)

    if char1.health <= 0 and char2.health <= 0:
        print "Draw"
    elif char1.health <= 0:
        print char2.name + ' won'
    elif char2.health <= 0:
        print char1.name + ' won'


def main():
    fighter1 = Player('Covid', 0, 'knife')
    fighter2 = Player('Human', 0, 'gun')
    fighter1.report()
    fighter2.report()
    fight(fighter1, fighter2)


'''
    fighter1.move((2.5, 4.5))
    fighter1.report()
    fighter2.move((2.5, 5.5))
    fighter2.report()
'''
main()
print 'Finished!'
