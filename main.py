Items = {
    'weapons': {
        'fist': {
            'damage': 5
        },
        'knife': {
            'damage': 20
        },
        'gun': {
            'damage': 50
        },

    },
    'armors': {
        'unarmored': {
            'defense': 0
        },
        'armor1': {
            'defense': 10
        },
        'armor2': {
            'defense': 20
        },
        'armor3': {
            'defense': 40
        },
    }
}


def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n


class Weapon(object):
    def __init__(self, name='fist'):
        self.name = name
        self.damage = Items['weapons'][self.name]['damage']


class Armor(object):
    def __init__(self, name='unarmored'):
        self.name = name
        self.defense = Items['armors'][self.name]['defense']

    def deplete_defense(self, val):
        self.defense -= val
        if self.defense <= 0:
            self.defense = 0


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

    def __init__(self, name, weapon=Weapon(), armor=Armor(), position=(0.0, 0.0)):
        super(Fighter, self).__init__(position=position)
        self.name = name
        self.weapon = weapon
        self.armor = armor
        # self.attack = weapon.damage
        # self.defense = armor.defense

    def __del__(self):
        super(Fighter, self).__del__()
        # print 'My name was %s.' % self.name
        pass

    def report(self):
        print 'Name: %s' % self.name
        # super(Fighter, self).report()
        print 'Fight with: %s / damage: %i // Armor: %s / defense: %i' % (
            self.weapon.name, self.weapon.damage, self.armor.name, self.armor.defense)


def fight(char1, char2):
    count = 0
    while char1.health > 0 and char2.health > 0:
        count += 1
        char1.health -= clamp(char2.weapon.damage - char1.armor.defense, 0, 100)
        char1.armor.deplete_defense(char2.weapon.damage)
        char2.health -= clamp(char1.weapon.damage - char2.armor.defense, 0, 100)
        char2.armor.deplete_defense(char1.weapon.damage)

        print 'round ' + str(count) + ' : ' + char1.name + ' health: ' + str(
            char1.health) + ' / Armor: ' + str(char1.armor.defense) + ' //// ' + char2.name + ' health: ' +\
              str(char2.health)  + ' / Armor: ' + str(char2.armor.defense)

    if char1.health <= 0 and char2.health <= 0:
        print "Draw"
    elif char1.health <= 0:
        print char2.name + ' won'
    elif char2.health <= 0:
        print char1.name + ' won'


def main():
    weapon1 = Weapon('fist')
    armor1 = Armor('armor3')
    weapon2 = Weapon('knife')
    armor2 = Armor('armor2')
    fighter1 = Fighter('Covid', weapon1, armor1)
    fighter2 = Fighter('Human', weapon2, armor2)
    fighter1.report()
    fighter2.report()
    fight(fighter1, fighter2)


main()
print 'Finished!'
