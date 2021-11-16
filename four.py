# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 23:03:17 2021

@author: Администратор
"""

import numpy
x = numpy.array(range(100))
print(x)

import numpy as np
x = np.array(range(100))
summa = sum(x)
print(x, "сумма=  ", summa)


z = int(input('Введи число  '))
x = np.array(range(z))
summa = sum(x)
print(x, "сумма=  ", summa)

np.random
x=np.random.randint(0, 10, 100)
srednee = np.mean(x)
print(x, "среднее=  ", srednee)