#!/usr/bin/env python
# coding: utf-8

# # today Topics
#   - comphersions(list,tuple,set and dict)
#   - special Functions(map,filters,lambda)
#   - Models and packages
#   - Files

# In[4]:


#comphersions(list,tuple,set and dict)
li = [1,2,3,4,5,6,7,8,9,10]
l1 = []
for i in range(5):
    j = input()
    l1.append(j)
l1
    


# In[1]:


l2 = []
while True:
    n = input('enter element:')
    if n == 'EXIT':
        break
    else:
        l2.append(n)
print(l2)


# In[2]:


s = 'abcde'
list(s)


# In[3]:


li = [i for i in range(1,11)]


# In[4]:


li


# In[11]:


n = 9**(1/2)
print(n)


# In[17]:


li = [i for i in range(int(input()),50) if i%2==0]
li


# In[24]:


def Is_Prime(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i == 0:
            cnt+=1
    if cnt == 2:
        return True
    else:
        return False


# In[27]:


start = int(input('enter start range: '))
end = int(input('enter end range: '))
prime_list = [i for i in range(start,end+1) if Is_Prime(i)]


# In[28]:


len(prime_list)


# In[29]:


t = [i for i in range(1,10)]
print(tuple(t))


# In[30]:


s = {i for i in range(1,10) if i%2!=0}
s


# In[32]:


d = {i:i**2 for i in range(1,11) if Is_Prime(i)}
d


# In[36]:


### special functions
# Map
li = ['1','2','3','4']
# sum = 10
l = []
for i in li:
    l.append(int(i))
sum(l)


# In[38]:


sum(list(map(int,li)))


# In[45]:


l = '1 2 3 4 5 6 7'
#list(map(int,list(l)))
#list(l)

sum(list(map(int,l.split())))/len(l.split())


# In[40]:


l = '2 4 6 8 10'
30/10


# In[41]:


s = '1 2 3 4 5 6'
21/6


# In[48]:


# lambda
# l = lambda var:expression
a = int(input())
b = int(input())
a+b
l = lambda a,b : a-b**a
l(89,98)
l(a,b)


# In[49]:


#Filters
li = [1,0,'True',False,'0']
# filter(fun,elements)
a = filter(None,li)
list(a)


# In[ ]:


# letter = 'abcdef'
# vovels = ['a','e','i','o','u']


# In[50]:


# iterator
s = 'python'
for i in s:
    print(i)
print(i)


# In[55]:


a = iter(s)
a.__next__()


# In[56]:


a.__next__()


# In[ ]:


# Module and packages:
- one python file contains no.of functions
- no.of python files in one folder
- if want to use modules first import modules/packages
- predefined modules or packages
- user define modules or packages
- 


# In[1]:


# predefine modules or package
# Math
import math
help(math)


# In[2]:


math.radians(90)


# In[4]:


math.factorial


# In[5]:


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)
fact(9)


# In[6]:


math.pow(2,4)


# In[7]:


import os
help(os)


# In[8]:


os.path


# In[ ]:


# Creating user define module
# creating python file in same location
# creating number of functions in that file
# after that save the file with .py extension
# after import the user define 


# In[9]:


import example


# In[10]:


help(example)


# In[11]:


example


# In[12]:


example.__doc__


# In[21]:


import.sample()


# In[22]:


sample.add()


# In[24]:


import arthamatic


# ### Files
# 
#  - file is save the data
#  - read
#  - write
#  - append
#  - modes
#    - for create file we use 'x'
#    - for read the data from file we use 'r'
#    - for write the data into file we use 'w'
#    - for adding the data into file we use 'a+'
#  - open  
#  - read
#  - write
#  - read(n)
#  - readline()
#  - readlines()
#  - tell()
#  - seek()

# In[30]:


# var = open(filename,mode)
f = open('pace.txt','x')
f.close()


# In[39]:


f = open('pace.txt','r')
data = f.read()
print(data)
f.close()


# In[41]:


f = open('pace.txt','w')
data = 'welcome to cse second year'
f.write(data)
print('data write into the file is successful...')
f.close()


# In[42]:


f = open('pace.txt','a')
data = 'cse-a welcome to python programing'
print(data)
f.close()


# In[46]:


f = open('pace_1.txt','a+')
f.write(' and python programing')
print('data write into the file is done..')
data = f.read()
print('data is:')
print(data)
f.close()


# In[49]:


f = open('pace_3.txt','w+')
f.write('hello')
f.close()


# In[53]:


f = open('pace_3.txt','r')
data = f.readlines()
print(data)
f.close


# In[55]:


f = open('pace_3.txt','a')
data = 'abc\ncde\ndef'
f.write(data)
f.close()


# In[56]:


with open('abc.txt','w') as f:
    data = 'ram: 23,56'
    f.write(data)


# In[57]:


with open('abc.txt','r') as f:
    data = f.read()
    print(data)


# In[58]:


with open('abc.txt','a') as f:
    data = '\ncdf :34,67'
    f.write(data)


# In[63]:


with open('pace.txt','a') as f:
    print(f.tell())
    f.seek(10)
    f.write('\n abc : 24,65')


# In[68]:


with open('pace.txt','r') as f:
    print(f.tell())
    print(f.read())
    f.seek(10)
    print(f.read())


# In[ ]:




