# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

def solution(absolutes, signs):
    for i in range(len(absolutes)):
      if(signs[i]==False):
        absolutes[i] = "-"+str(absolutes[i])
      else:
        absolutes[i] = str(absolutes[i])
    return sum(list(map(int, absolutes)))

print(solution([4,7,12],[True,False,True]))
print(solution([1,2,3],[False,False,True]))

#삼항 연산자 할 생각을 못했네...zip이랑
# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))