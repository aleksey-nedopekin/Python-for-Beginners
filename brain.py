# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:57:21 2021

@author: Администратор
"""


# функции для 1 варианты

# cheat_sheet = ''

# def was_asked(memory, q):
#     global cheat_sheet
#     for question, answer in memory:
#         if question == q:
#             cheat_sheet = answer
#             return 1
#     return 0

# def old_answer():
#     global cheat_sheet
#     rez, cheat_sheet = cheat_sheet, ''
#     return rez

# if __name__ == '__main__':
#     memory = [
#         ('Ты умеешь говорить', 'да'),
#         ('Ты умеешь говорить', 'нет'),
#         ]
#     print(was_asked(memory, 'Ты умеешь говорить'))
#     print(old_answer(memory, 'Ты умеешь говорить'))

# функции для 2 варианта

import re
from sys import stderr
from random import randint
from itertools import product
from pprint import pprint
NOT_FOUND = '$'
MIN_WORD_SIMILARITY = 0
MIN_QUESTION_SIMILARITY = 0.5
 
class Brain():
    memory = dict()
    answers = ('да','нет')    
    
    def __fuzzy_key_search(self, words):
        answer = NOT_FOUND
        for key in self.memory:
            rez = []
            for w1, w2 in product(key, words):
                w = self.__compare(w1, w2)
                if w > MIN_WORD_SIMILARITY: 
                    rez += [ (w, w1, w2) ]
            pprint(rez, stderr)
            if sum((x[0] for x in rez)) / len(rez) > MIN_QUESTION_SIMILARITY:
                answer = self.memory[key]
        assert answer != NOT_FOUND    
        return answer
        
    def __compare(self, s1, s2):
        count = 0  
        for ngram in ( s1[i:i+3] for i in range(len(s1)-1) ):
            count += s2.count(ngram)
        return count / max(len(s1), len(s2))
    
    def think(self, question):
        words = tuple(re.sub(r'[!;:?,.-]',' ', question).split())
        try: 
            return "Я уже отвечала, ответ был %s." % self.memory[words] 
        except KeyError: 
            try: 
                answer = self.__fuzzy_key_search(words)
                return "Я, кажется, уже отвечала, ответ был %s." % answer
            except (AssertionError, ZeroDivisionError):
                answer = self.answers[randint(0, len(self.answers)-1)]
                self.memory.update({words:answer})
                return "Мой ответ - %s!" % answer
        
if __name__ == '__main__':
    brain = Brain()
    print(brain.think('Какой-то вопрос?'))  
    print(brain.think('Какой-то вопрос?'))  
    print(brain.think('Какой то вопросик?'))
    print(brain.think('Какой то вопросчек?'))
    print(brain.think('Какой то вопросчечечек?'))
    print(brain.think('Сегодня будет дождь?'))
    print(brain.think('Завтра будет дождь?'))