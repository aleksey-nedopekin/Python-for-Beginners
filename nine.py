# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:33:19 2021

@author: Администратор
"""

# x = 1

# def foo1(x):
#     x += 1
#     print(1, x)

# foo1(2)
# print(2, x)

# def foo2( ):
#     # x += 1
#     print(3, x)

# foo2( )
# print(4, x)


# x = [1]

# def foo():
#     x[0] += 1
#     print(5, x)

# foo()
# print(6, x)


# class A:
#     x = 1

# a = A()
    
# def foo():
#     A.x += 1
#     print(7, A.x)
    
# foo()
# print(8, x)    

# def foo():
#     a.x += 1
#     print(9, a.x)
    
# foo()
# print(10, a.x)    

# class A:
#     def __init__(self, x):
#         self.x = x

# a = A(1)

# def foo():
#     a.x += 1
#     print(11, a.x)
        
# foo()
# print(12, a.x)

# from nine_mod import x
# print(13, x)

# вариант 1 запоминает ответы на вопросы
# from random import randint
# from brain import was_asked, old_answer
# memory = []
# prompt = "Что вас интересует?"
# answers = ("да", "нет")
# question = ""
# while question != "хватит":
#     print (prompt, end = '')
#     question = input()
#     if was_asked(memory, question):
#         print(old_answer())
#     else:
#         answer = answers[randint(0, len(answers)-1)]
#         print (answer)
#         memory += [ (question, answer) ]
        
# вариант 2
from brain import Brain

brain = Brain()
prompt = "Что вас интересует?"

question = ""
while question != "хватит":
    print (prompt, end='')
    answer = brain.think(input())
    print(answer)















        
