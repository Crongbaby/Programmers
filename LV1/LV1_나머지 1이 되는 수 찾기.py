# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13mWhZYkQO9wpiT8QLRAJ5CzpID7bEYxH
"""

def solution(n):
    for x in range(1,1000001):
        if((n%x) == 1):
            break
    return x

# def solution(n):
#     return [x for x in range(1,n+1) if n%x==1][0]

