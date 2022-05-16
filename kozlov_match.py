from time import sleep
from random import randint
class Hero():
    def __init__(self, name, health, armor, strength, weapon, wins):
        self.name = name
        self.health = health
        self.armor = armor
        self.strength = strength
        self.weapon = weapon
        self.wins = wins
    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.strength)
        print('Оружие:', self.weapon)
        if self.wins == 0:
            print('Коэффицент на победу:', len1*len1, '\n')
        elif self.wins == len1*len1:
            self.wins = len1*len1 - 1/len1
            print('Коэффицент на победу:', len1*len1/self.wins, '\n')  
        else:
            print('Коэффицент на победу:', len1*len1/self.wins, '\n')        
    def strike(self):
        print('-> УДАР!')
        print(self.name, 'атакует', name, 'используя', self.weapon, '\n')
        print(name,'покачнулся(-ась)')
        print('Класс брони упал до', armor)
        print('Уровень здоровья снизился до', health, '\n')
class Hero1():
    def __init__(self, name1, health1, armor1, strength1, weapon1, wins1):
        self.name1 = name1
        self.health1 = health1
        self.armor1 = armor1
        self.strength1 = strength1
        self.weapon1 = weapon1
        self.wins1 = wins1
heroes = list()
heroes1 = list()
heroes1.append(Hero1('Ричард', 50, 25, 20, 'меч', 0))
heroes1.append(Hero1('Хелен', 100, 10, 15, 'лук', 0))
heroes.append(Hero('Ричард', 50, 25, 20, 'меч', 0))
heroes.append(Hero('Хелен', 100, 10, 15, 'лук', 0))
print('Поприветствуйте наших героев!\n')
for i in heroes:
    print('Имя нашего героя -', i.name)
    print('Уровень здоровья:', i.health)
    print('Класс брони:', i.armor)
    print('Сила удара:', i.strength)
    print('Оружие:', i.weapon, '\n')

answer = input('Кто-то, кроме наших участников, хочет сражаться?')
while answer != 'нет':
    name = input('Имя участника:')
    health = int(input('Уровень здоровья:'))
    armor = int(input('Уровень брони:'))
    strength = int(input('Сила удара:'))
    weapon = input('Оружие:')
    wins = 0
    heroes.append(Hero(name, health, armor, strength, weapon, wins))
    heroes1.append(Hero1(name, health, armor, strength, weapon, wins))
    answer = input('Хочет ли кто-то ещё?')
print('\n')
game = 1
heroes2 = list()
for i in range(len(heroes1)):
    heroes2.append(heroes1[i])
len1 = len(heroes)
b = len1*len1
print('Считаем коэффиценты...\n')
while b!=0:    
    game = 1
    while game == 1:
        i = randint(0, len(heroes1)-1)
        a = randint(0, len(heroes1)-1)
        while a == i:
            a = randint(0, len(heroes1)-1)
        heroes1[i].armor1 -= heroes1[a].strength1
        if heroes1[i].armor1 < 0:
            heroes1[i].health1 = heroes1[i].health1 + heroes1[i].armor1
            heroes1[i].armor1 = 0
        if heroes1[i].health1 <= 0:
            heroes1[i].wins1 = heroes1[i].wins1 + 1/len1*(len1 - len(heroes1))
            for k in range(len(heroes)):
                if heroes1[i].name1 == heroes[k].name:
                    heroes[k].wins = heroes1[i].wins1
                    break
            heroes1.remove(heroes1[i])
        if len(heroes1) == 1:
            game = 0
            heroes1[0].wins1 = heroes1[0].wins1 + 1
            for k in range(len(heroes)):
                if heroes1[0].name1 == heroes[k].name:
                    heroes[k].wins = heroes1[0].wins1
                    break
            heroes1.remove(heroes1[0])
    for i in range(len(heroes2)):
        heroes1.append(heroes2[i])
    for i in range(len(heroes)):
        heroes1[i].name1 = heroes[i].name
        heroes1[i].armor1 = heroes[i].armor
        heroes1[i].strength1 = heroes[i].strength
        heroes1[i].weapon1 = heroes[i].weapon
        heroes1[i].health1 = heroes[i].health
        heroes1[i].wins = heroes[i].wins
    b -= 1
game = 1
print('Вот список участников:')
for i in heroes:
    i.print_info()
winner = input('На кого ставите?')
price = int(input('Сколько?'))
print('Ставка принята\n')
print('Обратный отсчёт!\n')
print(3, '\n')
sleep(1)
print(2, '\n')
sleep(1)
print(1, '\n')
print('Да начнётся битва!!!\n')
while game == 1:
    i = randint(0, len(heroes)-1)
    a = randint(0, len(heroes)-1)
    while a == i:
        a = randint(0, 1)
    name = heroes[i].name
    heroes[i].armor -= heroes[a].strength
    if heroes[i].armor < 0:
        heroes[i].health = heroes[i].health + heroes[i].armor
        heroes[i].armor = 0
    health = heroes[i].health
    armor = heroes[i].armor 
    heroes[a].strike()
    if heroes[i].health <= 0:
        print(heroes[i].name, 'пал(-а) в тяжёлом бою!')
        heroes.remove(heroes[i])
    if len(heroes) == 1:
        print('Битва окончена!\n')
        if heroes[0].name == winner:
            print('Вы были правы!\nПобедил(-а)', winner, '\n')
            if heroes[0].wins > 0 and heroes[0].wins:    
                print('Вам на счёт скоро перечислят - ', 1/heroes[0].wins*2*len1*price)
            elif heroes[0].wins == 0:
                print('Вам на счёт скоро перечислят - ', len1*len1*price)

        else:
            print('Ваша ставка не сыграла!\nПобедил(-а)', heroes[0].name, '\n')
        game = 0
    sleep(2)
print('До встречи в следующий раз!')
