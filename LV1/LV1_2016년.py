# -*- coding: utf-8 -*-
"""연습용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cI7vkqxs5WMh_9o0NpCARdKUabvS0EOe
"""

import calendar #calendar.weekday 함수로 요일 정보 추출
def solution(a, b):
  date = {6:"SUN",0:"MON",1:"TUE",2:"WED",3:"THU",4:"FRI",5:"SAT"}
  return(date[calendar.weekday(2016, a, b)])
  
print(solution(5,24))

#다른 사람의 풀이1..이건 예술...
def getDayName(a,b):
    answer = ""
    if a>=2:
        b+=31
        if a>=3:
            b+=29#2월
            if a>=4:
                b+=31#3월
                if a>=5:
                    b+=30#4월
                    if a>=6:
                        b+=31#5월
                        if a>=7:
                            b+=30#6월
                            if a>=8:
                                b+=31#7월
                                if a>=9:
                                    b+=31#8월
                                    if a>=10:
                                        b+=30#9월
                                        if a>=11:
                                            b+=31#10월
                                            if a==12:
                                                b+=30#11월
    b=b%7

    if b==1:answer="FRI"
    elif b==2:answer="SAT" 
    elif b==3:answer="SUN"
    elif b==4:answer="MON"
    elif b==5:answer="TUE"
    elif b==6:answer="WED"
    else:answer="THU"
    return answer

#다른 사람의 풀이2...
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

#다른 사람의 풀이3..
def getDayName(a,b):
    day_name = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month_dict = {
        "1":31, 
        "2":29, 
        "3":31, 
        "4":30, 
        "5":31, 
        "6":30, 
        "7":31, 
        "8":31, 
        "9":30, 
        "10":31, 
        "11":30, 
        "12":31
    }
    days = 0
    for i in range(1, a):
        days += month_dict[str(i)]
    days += b
    index = days % 7

    return day_name[index]

#다른 사람의 풀이4...
def solution(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    dayLen = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    now = 5
    for i in range(0, a - 1) :
        now += dayLen[i]

    answer = (now + b - 1) % 7

    return days[answer]