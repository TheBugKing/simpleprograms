
# coding: utf-8

# ## given an array implement a function to return the position of sorted elements

# # Solution 1

# In[2]:


arr=[]
for i in range(int(input("enter the size of arry"))):
    arr.append(int(input(f"enter array element {i}:\t")))
def funIndex(arr):
# getting index of arr elements
    arr_index=[arr.index(i) for i in arr]
    
    # mapping of elements and indexes in list of tuples and sorting them
    arr2=sorted([i for i in zip(arr,arr_index)])
    print("sorted tuple in the form of (value, index)",arr2)

    # printing the index value only
    res=[ arr2[i][1] for i in range(len(arr2))]
    print(f"\n the index of sorted elements the original arrar is {res}")


# In[3]:


funIndex(arr)
             


# ## given an array implement a function to return the sorted elements of an array , with changing the elements of old array and print both sorted and the old arrays

# # solution 2

# In[4]:


initial_arr=[]
arr=[]
for i in range(int(input("enter the size of arry"))):
    initial_arr.append(int(input(f"enter array element {i}:\t")))
def sorting1(arr):
    new_arr=sorted(initial_arr)
    print(" new array",new_arr)
    
sorting1(initial_arr)    
print(" initial array",initial_arr)

or
# In[5]:


import copy
def sorting2(arr):
    new=copy.deepcopy(arr)
    for i in range(len(new)):
        for j in range(i+1,len(new)):
            if new[i] > new[j]:
                temp=new[j]
                new[j]=new[i]
                new[i]=temp
    print(f"the new array is {new}")


# In[6]:


sorting2(initial_arr)
print(f" value old  array is : {initial_arr}")

