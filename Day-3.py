#!/usr/bin/env python
# coding: utf-8

# # python data structures
# 
#     - List is a seqence,typically used to srore collection of homogenuos items
#     - Lists are mutable
#     - using a pair of seqence brackets,separating items with commas[a,b,c]
# 

# In[20]:


l1 = [1,2,3,4,5,6,7,8]
l2 = ['welcome',7,8,9]
l2
l3 = l1+l2
print(l3[0])
print([6])
print(l3[-1])

# list slicing:

print(l3[0:])
print(l3[8:9])


# In[23]:


# List Methods:
a = []
dir(list)
dir(l1)
dir(a)


# In[31]:


a=[1,2,3,4,5]
#a.append(5)
a.append([6,7])
a


# In[42]:


# Extend
a.extend([8,9,20])
a[5][0]


# In[63]:


# count
a=[1,2,3,4,5]
a.append(6)
a.append([7,8])
a.extend([9,10,11,12])
a.count(3)
a.index(6)
#difference b/w pop,remove,clear,del

a.pop()#last in first out
a.pop(0)#index based
a.remove(2)#value based
del a[0]
a.clear()#removing all values in list
del a # removing variable
a


# In[69]:


# sort and Reverse
x=[1,2,3,4,5]
# sort
x.sort()
# reverse
x.reverse()
x.sort(reverse = True)
x


# In[74]:


# Insert (position,value)
vowles=['a','i']
vowles.insert(1,'e')
vowles.insert(3,'o')
vowles.insert(4,'u')
vowles


# In[81]:


# copy
y=x.copy()
x.append(100)
print(y)
print(x)


# In[88]:


z=x=y
x
y


# In[89]:


y


# In[90]:


z


# In[101]:



m=[]
n=int(input('Enter range of numbers'))
for i in range(0,n+1):
    m.append(i)
print(m)


# In[104]:


x[0]=99
x


# In[ ]:


# Tples

  - tuples are immutable sequence,typically used to store collection of hetrogenuos data
  - using a pair of parentheses to denote the empty typle:()  


# # Tuples
# 
# t=()
# t=(1,2,3,4,5,'a','b','c')
# t[0]
# t[-1]
# t[::-1]

# In[5]:


dir(t)


# In[ ]:


#Task
# li = [1,2,3,1,2,3,4]
#output = [1,2,3,4]


# In[1]:


li = [1,2,3,4,5,1,2,3]
l1 = []
for i in li:
    if i not in l1:
        l1.append(i)
l1


# In[2]:


# packing

student=('abc','123456','cse')
(name,rollno,dpt)=student
print(rollno)
print(name)


# # Dicyionaries
# 
#   - creating a dictionary is an simple as placing items inside curly braces

# In[7]:


address={'name':'abc','place':'ongole'}
address


# In[10]:


address['pincode']=523183
address['street']="xyz"
address


# In[11]:


dir(dict)


# In[15]:


address.get('pincode')


# In[17]:


address.values()


# In[18]:


address.popitem()


# In[20]:


address.pop('pincode')


# In[21]:


address


# In[25]:


address1={'pincode':523183,'street':'xyz'}
address1


# In[27]:


address.update(address1)
address


# In[28]:


address


# In[29]:


address['name']="xyz"


# In[30]:


address


# In[33]:


address2=dict.fromkeys(address,'fields')


# In[34]:


address2


# In[35]:


for i in range

{% for i in range (0,10)%}


# In[ ]:


# Sets

  - a set is an unordered


# In[36]:


# sets

s={1,2,3,4,5,6,7,8,1,2,3,4}
s


# In[38]:


dir(set)


# In[39]:


b={1,2,3,4}
b


# In[40]:


s


# In[42]:


s.union(b)


# In[44]:


s.intersection(b)


# In[46]:


s.add(9)
s


# In[49]:


b.difference(s)


# In[50]:


print(s.difference(b))
print(b.difference(s))


# In[51]:


b.pop()


# In[52]:


s.pop()


# In[53]:


s.remove(2)


# In[54]:


s


# In[58]:


s.isdisjoint(b)


# In[ ]:




