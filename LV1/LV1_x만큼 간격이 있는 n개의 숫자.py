# -*- coding: utf-8 -*-
"""Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c75-Cr0TfQuGgHxqaIJ0bE00EscZMsOS
"""

def solution(x, n):
    list_jump = []
    jump = x
    for i in range(n):
      list_jump.append(x)
      x+=jump
    return list_jump

print(solution(2,3))

#한 줄이면 됐는데....
# def number_generator(x, n):
#     # 함수를 완성하세요
#     return [i * x + x for i in range(n)]
# print(number_generator(2, 5))

# def number_generator(x, n):
#     # 함수를 완성하세요
#     a=[]
#     for i in range(n):
#         a.append((i+1)*x)
#     return a