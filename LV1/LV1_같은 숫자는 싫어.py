# -*- coding: utf-8 -*-
"""Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c75-Cr0TfQuGgHxqaIJ0bE00EscZMsOS
"""

def solution(arr):
    result=[]
    result.append(arr[0])
    for i in range(1,len(arr)):
        if(arr[i-1] != arr[i]):
            result.append(arr[i])
    return result

# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a

# def no_continuous(s):
#     # 함수를 완성하세요
#     return [s[i] for i in range(len(s)) if [s[i]] != s[i+1:i+2]]

# def no_continuous(s):
#     result = []
#     for c in s:
#         if (len(result) == 0) or (result[-1] != c):
#             result.append(c)
#     return result