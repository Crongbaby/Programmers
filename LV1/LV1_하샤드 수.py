# -*- coding: utf-8 -*-
"""Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c75-Cr0TfQuGgHxqaIJ0bE00EscZMsOS
"""

def solution(x):
    list_x = list(map(int, str(x)))
    if(x%sum(list_x) == 0):
        return True
    else:
        return False

# def Harshad(n):
#     # n은 하샤드 수 인가요?
#     return n % sum([int(c) for c in str(n)]) == 0