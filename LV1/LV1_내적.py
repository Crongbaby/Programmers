# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

def solution(a, b):
  return(sum([i*j for i,j in zip(a,b)]))

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1]	,[1,0,-1]))