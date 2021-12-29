#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# test 모듈 생성
PI = 3.14

def number_input():
    output = input("숫자 입력>")
    return float(output)

def get_circum(radius):
    return radius * PI * 2

def get_circle_area(radius):
    return radius * radius * PI
