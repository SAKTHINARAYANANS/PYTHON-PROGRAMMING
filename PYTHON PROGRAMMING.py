#!/usr/bin/env python
# coding: utf-8

# In[13]:


print("Hello World")


# In[14]:


a=int(input("enter value of a"))
b=int(input("enter value of b"))
print("sum is",a+b)


# In[5]:


a=int(input("enter value of a"))
b=int(input("enter value of b"))
a=a+b;
b=a-b;
a=a-b;
print("a is",a,"& b is",b)


# In[9]:


y=float(input("enter kilometer"))
c=y*0.621371
print("mile is",c)


# In[8]:


y=int(input("enter the number:"))
if y==0:
    print("0")
elif y>0:
    print("positive")
else:
    print("negative")


# In[6]:


y=int(input("enter the year"))
if(y%400==0)and(y%100==0):
    print("leap year")
elif(y%4==0)and(y%100!=0):
    print("leap year")
else:
    print("not leap")


# In[10]:


a=int(input("st value"))
b=int(input("end value"))
for i in range(a,b):
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if(c==1):
        print(i)


# In[11]:


a=0
b=1
print(a)
print(b)
for x in range(1,10,1):
    sum=a+b
    print(sum)
    a=b
    b=sum


# In[12]:


y=int(input("enter the sum for n th term"))
sum=0
for x in range(1,y+1):
    sum+=x
print("sum of n terms",sum)


# In[15]:


y=int(input("enter the number"))
sum=0
temp=y
d=temp%10
e=(temp//10)%10
f=int(temp/100)
sum=(d**3)+(e**3)+(f**3)
if sum==y:
    print("armstrong")
else:
    print("not armstrong")


# In[19]:


x=int(input("number of line"))
for i in range(1,x+1):
    print("* "*i)


# In[20]:


str1 = "hello students"
n = int(input("number of character removed"))
print("Initial String", str1)
res = ''
for i in range(0, len(str1)):
    if i >= n:
        res +=str1[i]
print("Resultant String", res)


# In[21]:


li=[23,45,65,44,32,34,510,20]
for x in li:
    if x%5==0:
        print(x)


# In[22]:


str1="hihello hi heeelo hihihi"
n=str1.count("hi")
print(n)


# In[23]:


for x in range(1,6):
    for y in range(1,x+1):
        print(x,end="")
    print("\n")


# In[25]:


number = int(input("Enter a number: "))
temp = number
reverse = 0

while(temp > 0):
    digit = temp % 10
    reverse = (reverse * 10) + digit
    temp = temp // 10

if(number == reverse):
    print(number, "is a palindrome number")
else:
    print(number, "is not a palindrome number")


# In[26]:


def interchange_first_last(list):
    list[0], list[-1] = list[-1], list[0]
    return list

my_list = [1, 2, 3, 4, 5]
print(interchange_first_last(my_list))


# In[28]:


def swap_elements(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]
    return list

my_list = [1, 2, 3, 4, 5]
print(swap_elements(my_list, 1, 3))


# In[29]:


my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)


# In[30]:


my_list = [1, 2, 3, 4, 5]
count = 0
for _ in my_list:
    count += 1
print(count)


# In[31]:


num1 = 10
num2 = 5

maximum = max(num1, num2)
print(maximum)


# In[32]:


a = 5
b = 3
minimum = min(a, b)
print(minimum)


# In[33]:


def is_symmetrical(string):
    return string == string[::-1]

def is_palindrome(string):
    string = string.lower().replace(" ", "") 
    return is_symmetrical(string)

my_string = "Madam"
if is_palindrome(my_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# In[34]:


def remove_char(string, i):
    return string[:i] + string[i+1:]

my_string = "Hello World"
new_string = remove_char(my_string, 4)
print(new_string)


# In[35]:


my_string = "Hello, World!"
length = len(my_string)
print(length)


# In[36]:


def print_even_length_words(string):
    words = string.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)

my_string = "This is a sample string with words of varying lengths"
print_even_length_words(my_string)


# In[37]:


my_tuple = (1, 2, 3, 4, 5)
size = len(my_tuple)
print(size)


# In[38]:


my_tuple = (5, 2, 9, 1, 7)
maximum = max(my_tuple)
minimum = min(my_tuple)
print("Maximum element:", maximum)
print("Minimum element:", minimum)


# In[1]:


matrix = [(1, 2, 3),
          (4, 5, 6),
          (7, 8, 9)]

row_sums = [sum(row) for row in matrix]
print(row_sums)


# In[41]:


my_list = [1, 2, 3, 4, 5]
result = [(num, num**3) for num in my_list]
print(result)

