# -*- coding: utf-8 -*-
"""TCS CODING SOLUTIONS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lKrdZSUo0dioqH-WmMTZDdEDhGHTty_D
"""

#fibonacci series

a=-1
b=1
limit=6
for i in range(0,limit+1):
    sum=a+b
    a=b
    b=sum
    print(sum)



#swap two numbers
a=10
b=20
print(a,b)
a,b=b,a
print(a,b)

#swapping withoutn using a third variable
a=10
b=20
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)

s="sourabh"
print(s[::-1])

#HCF OF TWO NUMBERS

def hcf(x,y):
  if x > y:
      smaller = y
  elif x<y:
      smaller = x
  else:
    return x
  for i in range(1, smaller+1):
      if((x % i == 0) and (y % i == 0)):
          hcf = i
  return hcf

#eculidian
def hcf1(x,y):
  if x > y:
      smaller = y
  elif x<y:
      smaller = x
  else:
    return x
  while(y):
         x, y = y, x % y

  return x

print(hcf(11,77))
print(hcf1(11,11))

#LCM oftwo numbers
def lcm(x, y):
  if x > y:
       greater = x
  else:
       greater = y

  while(True):
      if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
      greater += 1

  return lcm
def lcm2(x, y):
  lcm = (x*y)//hcf(x,y)
  return lcm

print(lcm(10,35))
print(lcm2(10,15))

#factors of a number
def factors(n):
  factor=[i for i in range(1, int(n**0.5) + 1) if n % i == 0]
  return factor
factors(120)

# sum of digits of a number

def sum_digits(num):
  sum=0
  while(num):
    rem=num%10
    sum+=rem
    num=num/10
  return sum

sum_digits(1234)

# factorial of a number

def cal_fact(num):
  fact=1
  if num==0 or num==1:
    return 1
  else:
    for i in range(1,num+1):
      fact*=i
  return fact

cal_fact(5)

#palindrome
def check_palindrome(num):
  sum=0
  temp=num
  while(num):
    rem=num%10
    sum=sum*10+rem
    num=num/10
  if sum==temp:
    return True 
  else:
    return False

check_palindrome(123421)

# armstrong
def check_armstrong(num):
  sum=0
  temp=num
  while(num):
    rem=num%10
    sum+=rem*rem*rem
    num=num/10
  if sum==temp:
    return True 
  else:
    return False

check_armstrong(371)

#palindrome string
s="madam"
if s==s[::-1]:
  print(True)
else:
  print(False)

#print sum of prime numbers in a given range
def print_prime(limit):
  flag=0
  for i in range(1,limit+1):
    count=0
    for j in range(1,limit+1):
      if i%j==0:
        count+=1
    if count==2:
      print(i)
print_prime(10)