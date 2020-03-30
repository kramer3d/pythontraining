Weapons = {
    'fist': 5,
    'knife': 20,
    'gun': 50
}

Armors = {
    'unarmored': 0,
    'armor1': 10,
    'armor2': 20,
    'armor3': 40
}


def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n


class Character(object):
    class_name = 'Character'

    def __init__(self, position=(0.0, 0.0)):
        self.health = 100
        self.stamina = 100
        self.position = position

    def __del__(self):
        # print 'I\'m dying!!!'
        pass

    def report(self):
        print 'Health: %i\nStamina: %i\nPosition: (%f,%f)' % \
              (self.health, self.stamina, self.position[0], self.position[1])

    def move(self, offset):
        self.position = (self.position[0] + offset[0], self.position[1] + offset[1])


class Fighter(Character):
    class_name = 'Fighter'

    def __init__(self, name, weapon='fist', armor='unarmored', position=(0.0, 0.0)):
        super(Fighter, self).__init__(position=position)
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.attack = Weapons[self.weapon]
        self.defense = Armors[self.armor]

    def __del__(self):
        super(Fighter, self).__del__()
        # print 'My name was %s.' % self.name
        pass

    def report(self):
        print 'Name: %s' % self.name
        # super(Fighter, self).report()
        print 'Fight with : %s / damage : %i / defense : %i' % (self.weapon, self.attack,self.defense)


def fight(char1, char2):
    count = 0
    while char1.health > 0 and char2.health > 0:
        count += 1
        char1.health -= clamp(char2.attack - char1.defense, 0, 100)
        char2.health -= clamp(char1.attack - char2.defense, 0, 100)
        print 'round ' + str(count) + ' : ' + char1.name + ' health : ' + str(
            char1.health) + ' / ' + char2.name + ' health : ' + str(char2.health)

    if char1.health <= 0 and char2.health <= 0:
        print "Draw"
    elif char1.health <= 0:
        print char2.name + ' won'
    elif char2.health <= 0:
        print char1.name + ' won'


def main():
    fighter1 = Fighter('Covid', 'knife','armor3')
    fighter2 = Fighter('Human', 'gun')
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
