#!/usr/bin/env python
# coding: utf-8

# In[6]:


# boolean practice : == , != , <, >, >=, <=
print(not 1==2) # not
print('가방' < '하마')  # sort() 순서
x = float(input())
print(10<x<20) # and연산자. 둘다 True일때만 True / False을 첫 조건으로 하면 뒤 조건 미수행
print(10<x or x<5) # or연산자. 둘다 False 일때만 False / True을 첫 조건으로 하면 뒤 조건 미수행


# In[7]:


# if 조건문
if True:
    print('True!!!')
print('-------')
if False:
    print('False!!!')


# In[70]:


# 정수 판별
x = input("정수를 입력해 주세요 :")
if not x.isdigit() :
    print("정수가 아닙니다")
else:
    x = int(x)
    if x>0:
        print("양수입니다")
    elif x<0:
        print("음수입니다")
    else:
        print('0입니다')


# In[76]:


# 홀짝 판별 or, in, % 로 3가지 방법 사용 가능
홀짝 = input("정수입력 :")
if not 홀짝.isdigit():
    print("정수가 아닙니다")
else:
    if 홀짝[-1] in "02468":
        print("짝수입니다")
    else:
        print('홀수입니다')


# In[60]:


# 시간을 다루는 모률 datetime
import datetime as time

now = time.datetime.now()
print('{}년'.format(now.year))


# In[52]:


type(now.hour)


# In[80]:


bool(2%3) # not 0 이면 True


# In[61]:


# 오전 오후 판별
if now.hour<12:
    print("오전")
else:
    print("오후")
    
# 계절 판별
if now.month<=2 or now.month==12:
    print('겨울')
elif (3 <= now.month <=5):
    print('봄')
elif (6 <= now.month <=8):
    print('여름')
else:
    print("가을")


# In[116]:


a = input("계산식 입력 :")
if not( a[0].isdigit() and a[-1].isdigit() ):                                            
    print("계산불가")
else:
    if '+' in a:
        a=a.split('+')
        print("a + b :", int(a[0])+int(a[-1]))
    elif '-' in a:
        a= a.split('-')
        print("a - b :", int(a[0])-int(a[-1]))
    elif '*' in a:
        a= a.split('*')
        print("a * b :", int(a[0])*int(a[-1]))
    elif '/' in a:
        a= a.split('/')
        print("a / b :", int(a[0])/int(a[-1]))


# In[120]:


'1,2,3' in '9999993'


# In[150]:


a_list = [(1,2), 3, [4,5], {2}]
len(a_list)
a2_list = a_list*3
print(a2_list)
a2_list.append(7)
print(a2_list)
print(a2_list.append(888)) # append 와 print 는 리턴 값이 없음
len(a2_list)
print("a_list : ", a_list)
print("a2_list", a2_list)
a_list.extend(a2_list) # 파괴적
print("a_list : ", a_list)


# In[153]:


del a_list[1]
print(a_list)


# In[156]:


a_list.remove(3)
print(a_list)


# In[158]:


a_list.count(1)


# In[163]:


list_a = [1, 2, 3]
list_b = list_a.copy() # 주소를 복사, 실제로 복사가 됨
list_b
list_b.remove(1)
list_b


# In[167]:


# 반복분
for i in range(10):
    a = '*'*i
    print(a, i, len(a))


# In[184]:


# 두 숫자를 입력받아 두 수 사이의 합
a = input("첫 번째 숫자 입력 :")
b = input("두 번째 숫자 입력 :")
if a.isdigit() and b.isdigit():
    if int(a)<int(b):
        a_1 = int(a)
        b_1 = int(b)
    else:
        a_1 = int(b)
        b_1 = int(a)
    
    sum = 0
    for i in range(a_1+1,b_1):
        sum = sum + i
    print(sum)
else:
    print("숫자가 아닙니다")


# In[173]:


a = int(input())


# In[188]:


list_4 = [[1,2,3], [4,5,6,7], [8,9]]
for a in range(len(list_4)):
    for b in range(len(list_4[a])):
        print(list_4[a][b])


# In[190]:


numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

for number in numbers:
    output[number%3 -1].append(number)

print(output)


# In[203]:


dict_a = {
    'name' : "7D 건조 망고",
    'type' : '당절임'
}
print(dict_a)
print(dict_a['name'])

dict_a['ingredient'] = ['망고', '설탕', '나트륨']
dict_a

del dict_a['type']
dict_a

if 'name' in dict_a:
    print('type key 존재함')
else:
    print("존재하지 않는 키")
    
# for 반복문으로 각 요소의 값 출력
for key in dict_a:
    print('{} : {}'.format(key, dict_a[key]))
print(type(list_a), type(dict_a), type(dict_a['name']))

dict_a.items()
for key, value in dict_a.items():
    print('{} : {}'.format(key, value))


# In[ ]:





# In[210]:


list_a = []
dict_a = {}

list_a.append(10)
dict_a['name'] = '홍길동'

del list_a[0]
num = 0
sum = 0
for i in range(5):
    num = int(input('숫자를 5번 입력하세요'))
    list_a.append(num)
    sum += num
print('데이터 합 :',sum)
print(list_a)


# In[238]:


print("--------2번---------")


dict_score_name = {}

for t in range(100):
    write = input("이름 국어 영어 수학 점수입력 :").split()
    list_name = []
    list_score = []
    sum = 0
    name = write[0]
    if name == 'quit':
        break
        
    for i in range(1,4):
        list_score.append(int(write[i]))
    for i in range(3):
        sum += list_score[i]
    list_score.append(sum)
    dict_score_name[name] = list_score
print(dict_score_name)

    


# In[234]:


print('------3번-------')


# In[252]:


numbers = [1,2,3,4,5,1,2,3,1,2,2,2,2,3,3,3,3,1,1,1,1 ]
counter = {}

for number in numbers:
    counter[number] = 0
    for i in range(len(numbers)):
        if numbers[number] == numbers[i]:
            counter[number] += 1
        else:
            counter[number] += 0
    
print(counter)


# In[243]:


len(numbers)


# In[ ]:




