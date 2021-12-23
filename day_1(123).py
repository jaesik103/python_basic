#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # python
# ### 기본문법 1일차

# In[ ]:


print('hello')
print(10 * 20)
10+20


# In[ ]:


import keyword
keyword.kwlist


# In[ ]:


1+1


# In[ ]:


print('test print')
print(10+20)


# In[ ]:


# print() 함수 사용해 보기
print('hello python!!')
print('연산식 :',10+20)
print('여러 자료 출력 :', 10, 20, ' end')
print() # 빈 라인 출력
print(10+20)


# In[ ]:


# 자료형 확인
print(type('문자열'))
print(type(1.1))


# In[ ]:


print('"안녕하세요"')


# In[ ]:


print("\"안녕하세요\"")


# In[ ]:


# \n : 줄 바꿈, \t : tab 띄움
# \\ : \를 출력
print('\\ \\ \\ \\')


# In[ ]:


print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("구름\t3\t강서구")


# In[ ]:


print('동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세')

print('''하느님이보우하사 
마르고닳도록''')


# In[ ]:


print('test'*3)


# In[ ]:


print('a'+'b')


# In[ ]:


print('안녕하세요'[0])


# In[ ]:


print('안녕하세요그래요'[0:-1:3])


# In[ ]:


5//2


# In[ ]:


print(pi)


# In[ ]:


import numpy as np
print(np.pi)


# In[ ]:


pi


# In[ ]:


pi=3.14
pi


# In[ ]:


print(pi)
print(np.pi)


# In[ ]:


print(type(np.pi))


# In[ ]:


b =np.pi
b += 10
print(b)


# In[ ]:


print("안녕하세요"-"안녕")


# In[ ]:


string_data = input("인풋데이터 : ")
print(string_data)
print(type(string_data))
string_data += "456"
print(string_data)


# In[ ]:





# In[ ]:


a = float(input("a : "))
b = float(input("b : "))


# In[ ]:


print("a+b :",a+b)
print("a-b :",a-b)
print("a*b :",a*b)
print("a/b :",a/b)


# In[ ]:


a = "{}만 원".format(1000)
b = "{}{}{}".format(1000, 2000, 3000)
print(a)
print(b)


# In[ ]:


a = "{:d}".format(52)

b = "{:5d}".format(52)

c = "{:10d}".format(52)

d = "{:05d}".format(52)

e = "{:05d}".format(-52)

print(a, b, c, d, sep="\n")


# In[ ]:


a = "asdeeeeQQQ"
a.upper()


# In[ ]:


a = """        asdddd      
ASsddDDDD   """
print(a)
print(a.strip())


# In[ ]:


print(a[:4].isspace())


# In[ ]:


a = "asdasdQ3Q3Q21"
print(a.find('dQ'))


# In[ ]:


print("asd" in a)


# In[ ]:


a_list = a.split("Q")
print(a_list)


# In[ ]:


print(type(a_list[3]))


# In[ ]:


b = 1234561456189
b.split(1)


# In[ ]:


a_list[0][1:-1]


# In[ ]:


zero = input("두 수를 띄어쓰기로 구분하여 입력하시오")
a = float(zero.split(" ")[0])
b = float(zero.split(" ")[1])
print("a+b :", a+b)
print("a-b :", a-b)


# In[ ]:


print(type(zero))


# In[ ]:


a = input("영문자입력 :")
print("대문자로 :", a.upper())
print("소문자로 :", a.lower())
print("알파벳으로 이루어져 있는가? :", a.isalpha())


# In[ ]:


b = input("숫자입력 :")
print(type(b))
print("숫자로만 이루어져 있는가? :", b.isdigit())


# In[ ]:


c = input("문자열 5개 띄어쓰기로 구분하여 입력 :")
print("3번 째 문자열 처음 문자 :", c.split()[2][0])
print("5번 째 문자열의 마지막 문자 :", c.split()[4][-1])
print("문자열 길이 :", len(c))
print("test가 입력됐는가? :", 'test' in c)


# In[ ]:


d = input("숫자 세 개를 띄어쓰기로 구분하여 입력 :")
print(d)
print(type(d))
print('처음과 마지막 숫자의 합 :', float(d.split()[0])+float(d.split()[-1]))
print('두번 쨰와 마지막 숫자의 곱 :', float(d.split()[1])*float(d.split()[-1]))


# In[ ]:


d = input("숫자 세 개를 띄어쓰기로 구분하여 입력 :").split()
print(d)


# In[ ]:




