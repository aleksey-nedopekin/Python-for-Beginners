# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:45:57 2021

@author: Администратор
"""

from pprint import pprint






def compare(s1, s2):
    s1, s2 = [s.lower() for s in [s1, s2]]
    ngrams = [s1[i+i:3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count/max(len(s1), len(s2))

def int_val(s):
    try:
        return int(s)
    except ValueError:
        return 0

queries = [
    'страна Россия',    
    'город Пермь']
   #  'выше, 180',
   #  'тяжелее, 70',
   #  'фамилия Зотов',
   #  'зовут нова']



if __name__ == '__main__':
    out = []
    for a, b in  queries[0]:
        out += [(a, b, compare(s1, s2))]
        pprint(out)
    pprint ([int_val(s) for s in queries ] )



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


# s1 = queries
# s2 = group1[1][0]
# c = compare (s1, s2)

# print (c, S1, S2)


# queries = [
#     ('страна Россия'),
#     ('город Пермь'),
#     ('выше, 180'),
#     ('тяжелее, 70'),
#     ('фамилия Зотов'),
#     ('зовут нова')]


# people = {
#     petrov.key: petrov,
#     zotov.key: zotov,
#     ivanov.key: ivanov,
#     sokolov.key: sokolov
# }
# pprint(people)
# pprint(people[petrov.key])




