# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:45:57 2021

@author: Администратор
"""
roup1=[['Петров В.В.', 'муж.', 'Россия', 'Пермь', 1971, 165, 75, 'инженер'],
        ['Зотов К.С.', 'муж.', 'Россия', 'Лысьва', 1995, 174, 80, 'техник'],
        ['Иванова П.П.', 'жен.', 'Россия', 'Сызрань', 1970, 170, 55, 'специалист'],
        ['Соколов М.М.', 'муж.', 'Россия', 'Пермь', 1976, 187, 84, 'начальник']]


from pprint import pprint
class Workman:
    def __init__(self, name, sex, country, city, born, height, weight, position):
        self.name, self.sex, self.country, self.city, self.born, self.height, self.weight, self.position = name, sex, country, city, born, height, weight, position
        self.key = (name, born)
    def __repr__(self):
        return "Workman('%s' ,'%s','%s','%s','%s','%s','%s','%s')" % (self.name, self.sex, self.country, self.city, self.born, self.height, self.weight, self.position)
    
petrov = Workman('Петров В.В.', 'муж.', 'Россия', 'Пермь', 1971, 165, 75, 'инженер')
zotov = Workman('Зотов К.С.', 'муж.', 'Россия', 'Лысьва', 1995, 174, 80, 'техник')
ivanov = Workman('Иванова П.П.', 'жен.', 'Россия', 'Сызрань', 1970, 170, 55, 'специалист')
sokolov = Workman('Соколов М.М.', 'муж.', 'Россия', 'Пермь', 1976, 187, 84, 'начальник')

people = {
    petrov.key: petrov,
    zotov.key: zotov,
    ivanov.key: ivanov,
    sokolov.key: sokolov
}
pprint(people)
pprint(people[petrov.key])