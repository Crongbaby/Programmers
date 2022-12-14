# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

def solution(s):
    result = ''
    new_s = s.split(' ')
    for i in new_s:
        for index,value in enumerate(i):
            if index % 2 == 0:
                result += i[index].upper()
            else:
                result += i[index].lower()
        result+= ' '
    return result[:-1]

print(solution("try hello world"))
#print(solution("    try hello world       a"))

#다른 사람의 풀이1....
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

#다른 사람의 풀이2...
def toWeirdCase(s):
    # 함수를 완성하세요
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])