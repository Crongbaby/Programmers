# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

def solution(k, score): #되게 불필요한 코드로 맞춤.,..다른 사람 코드 보고 배우기.
  Hall_of_fame = []
  result = []
  for day in range(len(score)):
    if len(Hall_of_fame) == k and Hall_of_fame[-1] < score[day]:
      Hall_of_fame[-1] = score[day]
    elif len(Hall_of_fame) >= k and Hall_of_fame[-1] >= score[day]:
      Hall_of_fame = sorted(Hall_of_fame, reverse = True)
    else:  
      Hall_of_fame.append(score[day])
    Hall_of_fame = sorted(Hall_of_fame, reverse = True)
    result.append(Hall_of_fame[-1])

  return result

print(solution(3,	[10, 100, 20, 150, 1, 100, 200]))
print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))

#다른 사람의 풀이1..
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer

#다른 사람의 풀이2...힙을 사용하여 짠 코드드
import heapq

def solution(k, score):
    max_heap = []
    answer = []

    for sc in score:
        heapq.heappush(max_heap, (-sc, sc)) #범위
        answer.append(max(heapq.nsmallest(k, max_heap))[1])

    return answer

#다른 사람의 풀이3..나와 비슷하지만 더 간단하게 구현한 코드
def solution(k, score):
    answer = []
    ppt_score = []
    for i in score:
        ppt_score.append(i)
        if len(ppt_score) > k:
            min_ = ppt_score.index(min(ppt_score))
            del ppt_score[min_]
        ppt_score.sort(reverse=True)
        answer.append(ppt_score[-1])
    return answer

def solution(k, score):
    answer = []
    a=[]
    for i in score:
        a.append(i)
        a.sort(reverse=True)
        if len(a)>k:
            del a [-1]
        answer.append(min(a))
    return answer