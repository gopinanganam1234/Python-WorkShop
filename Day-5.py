#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Regular expression:
#2.oops
#3.numpy
#4.matplolib
#5.pandas


# In[ ]:


# Regular expression:

 - to check the data is valid or not
 - data filters


# In[7]:


l = ['abc','aca','ada']
for i in l:
    if i.endswith('a'):
        print(i)


# In[8]:


import re


# In[9]:


dir(re)


# In[ ]:


# syntax:
# re.methodname(pattern,data)
# pattern is format of required data
# data is given values


# In[11]:


s = 'abaacdaa'
'a' in s


# In[17]:


re.findall('aa',s)


# In[30]:


l = ['ab','aca','aaa','abba','']


# In[31]:


for i in l:
    if re.search('.',i):
        print(i)


# In[32]:


for i in l:
    if len (i) == 3 or len(i) == 2:
        print(i)


# In[43]:


for i in l:
    if re.search('a.+a',i):
        print(i)


# ### * (star)
# 
# - min value 0 maxvalue
# 
# ### + (plus)
# 
# - min value is 1 max any
# 
# ### ^ (cap)
# 
# - starts with
# 
# ### $ (dolar)
# 
# - ends with
# 
# ### \d :
# 
# - digits
# 
# ### []:
# 
# - specific values
# 
# ### {min,max}
# 
# - 

# In[72]:


s = 'abc 123 hello 456'
pattern = '\d+'
li = re.findall(pattern,s)
li
sum(list(map(int,li)))


# In[78]:


names = ['Ram','venkat','gopi','karthik','katrina']
pattern = '^R.{3}$'
pattern1 = '^.+[kt]$'
for name in names:
    if re.match(pattern1,name):
        print(name)


# In[116]:


# how to valid A phone number
#1.10 digits
#2.starts with 6-9
numbers = ['9133452670','5233864748','5465676879','7343945745','4522687320']


# In[117]:


numbers1 = ['+9133452670']


# In[118]:


pattern = '^(\+91)[6-9]\d{9}$'
for number in numbers1:
    if re.match(pattern,number):
        print(number)


# In[ ]:


#1. srarts with any alphabets
#2. any digits
#3. @gmail.com
emails = ['Ramu.Mandava@apssdc.in','abc123@gmail.com','cdef456@gmail.com']


# In[123]:


email = input('enter mail id')
pattern = '^[A-Za-z]{1,15}\d{0,10}[@](gmail\.com)$'
if re.match(pattern,email):
    print(email)


# In[ ]:


### OOps:

 - class
 - object


# In[ ]:


# create a class
  # variables
    # methods


# In[1]:


class Student:
    x = 10


# In[2]:


print(Student.x)


# In[3]:


# creating an object
# rv = ClassName()
s = Student()


# In[4]:


s.x


# In[7]:


class Student:
    x = 10
    def display(self,name):
        print('hello {}'.format(name))
s = Student()
print(s.x)
s.display('venky')


# In[46]:


class Student:
    x = 10
    def __init__(self,name):
        self.name = name
        self.y = 20
        print('This is constructer..')
    def m1(self):
        z = 30 # local var
        print('This is method...')
        print('my name is {}'.format(self.name))
        print(z)


# In[47]:


s = Student('venky')


# In[48]:


s1.m1()


# In[49]:


s1.x


# In[50]:


s1.m1()


# In[ ]:


import matplotlib.pyplot as plt


# In[3]:


s = [90,45,67,89]
s1 = [67,88,90,76]
plt.bar(s,s1)


# In[6]:


help(plt)


# In[ ]:




