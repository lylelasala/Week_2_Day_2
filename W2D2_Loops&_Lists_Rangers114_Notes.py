#!/usr/bin/env python
# coding: utf-8

# # Functions, Scoping, Data Collections 1 & List Comprehensions

# ## Tasks Today:
# 
# <i>Monday Additions (for loops)</i>
# 
# 1) For Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Using 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Continue Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Break Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Pass Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Double For Loops <br>
# 2) While Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Looping 'While True' <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) While and For Loops Used Together <br>
#  
# 3) Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Indexing a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .append() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .insert() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .pop() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) del() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Concatenating Two Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Lists Within Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Looping Through Lists <br>
# 4) Working With Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) min() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) max() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) sum() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) sort() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Copying a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) 'not in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Checking an Empty List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Removing Instances with a Loop <br> 
# 5) List Comprehensions <br>
# 6) Tuples <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) sorted() <br>
# 

# ### For Loops

# In[6]:


# for keyword, counter/iterator, in keyword, object

# for i in range(10):
#     print(i)
    
name = "Lyle"
# for letter in name:
#     print(letter)

# print(len(name))
# for i in range(len(name)):
#     print(name[i])

print(name[4])

    


# ##### Using 'in' keyword

# In[2]:


#in is what accesses the items in an iterable
for i in range(15):
    print(i**2)


# ##### Continue Statement

# In[1]:


for i in range(20):
    print(i)
    
#will continue to the next iteration
for i in range(20):
    if i == 5 or i == 6:
        continue
    print(i)



# ##### Break Statement

# In[1]:


#stops the Loop from iterating if a certain condition is met
for i in range(20):
    if i -- 6:
        break
    print(1)
    


# ##### Pass Statement

# In[ ]:


#mostly used as a placeholder

for i in range(20)
    pass

word = "midi keyboard"



# ##### Double For Loops

# In[3]:





# In[26]:


for i in range(5):
    for j in range(5):
        print("1 = ", i, "j = ", j)


# In[ ]:





# In[ ]:





# In[ ]:





# ### While Loops

# In[3]:


#while keyword, condition
#while loop will run based on the codition statement

counter = 0

while counter < 11:
    counter += 1
    print(counter)


# In[2]:


print("\n")

num = 0
while num < 15:
    print(num**2)
    num+=1


# In[1]:


#breaks with while loop
num1 = 0

while num1 < 15:
    
    num +-1
    if num -- 7:
        break
    print(num1)


# In[ ]:





# ##### looping 'While True'

# In[1]:


# true as a condition for a while loop to run
game_over = False
while True:
    print("Infinite Loop")
    if game_over == False:
        break


# In[1]:


game_running = True
num = 7
while game_running:
    print("checking num")
    if num == 7:
        game_running = False


# In[ ]:


while True:
    name = input ('what is your name?')
    if name == '':
        print ('thats empty please enter a name')
    else:
        print(name)
        break


# ##### While & For Loops Used Together

# In[1]:


j = 0

while j < 10:
    print("\nWhile Loop Iteration: " + str(j))
    
    for i in range(4):
        print("For loop iteration: " + str(i))
        
    j += 1


# ##### The Range Function

# In[5]:


#range(start, stop, step) - stop is the only required parameter and is not inclusive
# start will default to 0 if not provided
# step will dafault to 1 if not provided

#stop
for i in range(5):
    print(i)
print("\n")    
#restart, stop
for i in range(1, 10):
    print(i)


# ### String Manipulation Exercise

# In[3]:


# loop through the list below and strip all white space and title case each string
# print each corrected name
names = ['    coNNor', 'max', ' EVan ', 'JORDAN']

for name in names:
    print(name.strip().title())


# In[15]:





# In[16]:





# In[17]:





# ## Lists

# ##### Declaring Lists

# In[5]:


#declaring an empty list
our_list = [] #<-- empty list

names = ["alex", "lyle", "chuck", "manja", "desiree"]

numbers = [1, 2, 3, 4, 5, 6, 7]

print(names)


# ##### Indexing a List

# In[11]:


#[start:stop:step] -->[-1]
#our_list[2]
names = ["alex", "lyle", "chuck", "manja", "desiree"]

#single index
print(names[2])

#print starting at index 1 and going to the end of the list
print(names[1:])
new_list = names [1:]
print(new_list)

#print starting at the beginning of the list and going up to the specified index
print(names[:2])

#print starting at index 1 and stepping by 2
print(names[1::2])
copy_list = names [1::2]
print(copy_list)

#reversing a list (starting at the back and printing every item going to the front)
print(names[::-1])


# ### List Methods

# ##### .append()

# In[12]:


#append add to the back of a list
names = ["alex", "lyle", "chuck", "manja", "desiree"]

names.append('Ben')
print(names)


# In[15]:


print(names[:2:-1])


# In[16]:


names.append('Fabian')
print(names)


# In[17]:


print(names[:4:-1])


# In[18]:


numbers = [1,2,3,4,5,6]

numbers.append(12)
numbers.append(16)
numbers.append(28)

print(numbers)


# In[3]:


names = ['    coNNor', 'max', ' EVan ', 'JORDAN']

title_list = []
for name in names:
    title_list.append(name.title().strip())
    
print(title_list)


# ##### .insert()

# In[4]:


#takes in an index, and an element
names = ["alex", "lyle", "chuck", "manja", "desiree"]

names.insert(3, "Ryan")
print(names)


# In[6]:


new_data = [5, 6, 1, 10, 11, 334, 12, 123]
new_data.insert(2,56)

print(new_data)


# In[7]:


print(len(new_data))
print(range(len(new_data)))


# In[1]:


for i in range(len(new_data)):
    if i == 3:
        new_data.insert(i, names[i])
        
print(new_data)


# ##### .pop()

# In[5]:


# pop will be default remove the last item in a list
# otherwise it takes an index and will pop out the value at that index from the list
names = ["alex", "lyle", "chuck", "manja", "desiree"]
bye_bye_name = names.pop(3)
print(bye_bye_name)

other_list = []
other_list.append(names.pop())
print(other_list)


# In[4]:


print(names.pop())


# ##### .remove()

# In[6]:


names = ['bob', 'bob', 'billy', 'berry', 'bertha', 'bob', 'bert']



print(names)


# In[8]:


names.remove('bob')

print(names)


# In[10]:


names = ['bob', 'billy', 'bob', 'bon', 'berry', 'bertha', 'bob', 'bert']
for name in names:
    if name == 'bob':
        names.remove('bob')

print(names)


# for i in range(len(names)):
# if names[i] == "Bob":
# names.remove(names[i])
#print(names)


# In[13]:


names = ['bob', 'billy', 'bob', 'bob', 'berry', 'bertha', 'bob', 'bert']
print(names)
while 'bob' in names:
        names.remove('bob')

print(names)


# for i in range(len(names)):
# if names[i] == "Bob":
# names.remove(names[i])
#print(names)


# ### Working With Lists

# ##### del()

# In[1]:


# index to be removed, not valued
# this can cause indexing errors
names = ['bob', 'billy', 'bob', 'bob', 'berry', 'bertha', 'bob', 'bert']
del(names[0])


# ##### min()

# In[4]:


#returns the smallest item in a list
numbers = [1,2,3,4,56]
print(min(numbers))

names = ['jack', 'jill', 'chad', 'huckleberry', 'beyonce' ]
print(min(names))


# In[5]:


#returns the smallest item in a list
numbers = [1,2,3,4,56]
print(min(numbers))

names = ['alfonso', 'gilbert', 'chad', 'zorph', 'aname' ]
print(min(names))


# ##### max()

# In[6]:


##returns the largest item in a list
numbers = [23, 45, 63, 12, 43, 100000001]
print(max(numbers))

names = ['alfonso', 'gilbert', 'chad', 'zorph', 'aname' ]
print(max(names))


# In[ ]:





# ##### sum()

# In[8]:


# returns the sum of all numbers in a list

numbers = [1,2,3,4,56]

print(sum(numbers))


# ##### sorted()

# In[9]:


numbers = [5,1,17,12,9,6,20,3]

sorted_nums = sorted(numbers)
print(sorted_nums)


# ##### .sort() <br>
# <p>Difference between sort and sorted, is that sorted doesn't change original list it returns a copy, while .sort changes the original list</p>

# In[10]:


numbers.sort()
print(numbers)


# ##### Copying a List

# In[11]:


# [:] copy a list, doesnt alter the original list
numbers = [3,6,1,5,10,-12]
print(numbers)
new_list = numbers [:]
print(new_list)



# In[13]:


another_list = []

for num in numbers:
    another_list.append(num)
    
print(numbers)
print(another_list)

num1 = 15

num1 = num2


# In[1]:


my_ string = 'cool beans'

new_string = my_string[:]

print(new_string)


# ##### Looping Through Lists

# In[3]:


#Looping by value
names = ['han solo', 'leia organa', 'luke skywalker', 'lando calrissian', 'mace windu']
for name in names:
    print(name)
print("\n")
for name in names:
    if name == "han solo":
        print(name)
print("\n")
#looping by index
for i in range (len(names)):
    print(names[i])
    
print("\n")

for i in range(len(names)):
    if names[i] == "leia organa":
        print(names[i])
        
#enumerate
for i, v in enumerate(names):
    print(i,v)
    
print("\n")

for i, v in enumerate(names):
    if v == "mace windu"


# ##### 'in' keyword

# In[5]:


#specifying list that we are iterating through
names = ["Alex", "Abdel", "Swan", "Ethan", "Hyun-Tae]" ]
if "Ethan" in names:
    print("Ranger")
else:
    print("not a ranger")


# In[87]:





# In[91]:





# In[ ]:





# ##### 'not in' keyword

# In[6]:


names = ["Alex", "Abdel", "Swan", "Ethan", "Hyun-Tae]" ]
if "Frederick" not in names:
    print("boooo not a Ranger")
else:
    print("great job being a ranger, frederick")


# ##### Checking an Empty List

# In[7]:


our_list = []

if our_list == []:
    print("welp thats empty")
else:
    print("there is stuff in there")


# ##### Removing Instances with a Loop

# In[8]:


names = ["Alex", "Abdel", "Swan", "Ethan", "Hyun-Tae]" ]

while "Alex" in names:
    names.remove('Alex')
    
print(names)


# ### List Exercise <br>
# <p>Remove all duplicates<br><b>Extra: Create a program that will remove any duplicates from a given list</b></p>

# In[11]:


names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

cleaned_list = []

for name in names:
    if name not in cleaned_list:
        cleaned_list.append(name)
        
print(cleaned_list)


# ### List Comprehensions <br>
# <p>Creating a quickly generated list to work with<br>*result*  = [*transform*    *iteration*         *filter*     ]</p>

# ##### In a list comprehension we have a few pieces:
# 1. The first is the counter/ variable - IN this the variable is x
# 2. then we have a transform for the variable
# 3. The finale part of a list comp is called the condition
# 
# ```python
#     [transform, iteration/variable, condition]
# ```

# In[12]:


nums = [2,4,6,8,10]
nums_squared = []

#for loop way
for num in nums:
    nums_squared.append(num**2)
print(nums_squared)

#list comprehension way
num_squared = [num**2 for num in nums]
print(num_squared)


# In[14]:


nums = [2,4,6,8,10,3,5,7,9,11]
nums_squared = []

#for loop way
for num in nums:
    nums_squared.append(num**2)
print(nums_squared)

#list comprehension way
num_squared = [num**2 for num in nums]
print(num_squared)

#list comprehension with conditional
more_squared = [num**2 for num in nums if num%2 ==0]
print(more_squared)


# There are a few benefits to using List comprehensions. The most obvious would be that we now have shorter code to work with instead of using 3+ lines of code in the for loop variant.
# 
# Another is an added benefit to memory usage. Since the list's memory is allocated first before adding elements to it, we don't have to resize the list once we add elements to it.
# 
# Lastly, list comprehensions are considered the "pythonic" way to write code by the PEP8 standards (Python Style Guide)

# In[15]:


pets = [ 'elliot', 'eyo', 'henri', 'luci', 'eyeball', 'astro', 'jimmy', 'kino', 'pi', 'penny']

letter_names = [name [0] for name in pets if name[0] != '0']

print(letter_names)


# In[ ]:


import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


# ### Tuples <br>
# <p><b>Defined as an immutable list</b></p><br>Seperated by commas using parenthesis

# In[21]:


#declaring tuples
tup_1 = (1,2,3)
tup_2 = 4,5,6

print(tup_1)
print(tup_2)

print(type(tup_1))

#indexing into a tuple
print(tup_1[0])
print(tup_2[1])

#length of a tuple
print("tuple length", len(tup_2))

#iterating through a tuple
for num in tup_1:
    print(num)
    
for i in range(len(tup_2)):
    print(tup_2[i])


# ##### sorted()

# In[26]:


tup = (20,5,1,10,95,123)
print(sorted(tup))

print(tuple(sorted(tup)))

some_list = [5,12,654,234,65,12]

#combine_list = some_list + tup

new_tup = tuple(some_list)
print(new_tup)

new_new_tup = tup + new_tup
print(new_new_tup)


# In[142]:


tup = (20, 5, 1, 10, 95, 123)

print(sorted(tup))

some_list = [5, 12, 654, 234, 7643, 34]

# combine_list = some_list + tup

new_tup = tuple(some_list)

new_new_tup = new_tup + tup
print(new_new_tup)




# In[149]:


# List Concatenation

my_list = [1, 2, 3, 4, 5]
my_list2 = [2, 3, 4, 5, 13, 12, 16, 1234]

my_list3 = my_list + my_list2

print(my_list3)


# ##### Adding values to a Tuple

# In[23]:


tup = (20, 54, 60, 23, 11)
print(tup)
my_tup = tuple()
print(my_tup)
#help(tuple)

tup = tup + (6,)

print(tup)


# # Exercises

# ## Exercise 1 <br>
# <p>Using the given list, print out a filtered version of the list with only the numbers that are less than ten</b></i></p><br>
# 

# In[28]:


#Given that list of #s < 10


alist = [1,11,14,5,8,9]
#------------------------------
numbers = [1,11,14,5,8,9]

filtered_numbers = [num for num in numbers if num < 10]

print(filtered_numbers)




# ## Exercise 2 <br>
# <p>Merge and sort the two lists below<br>
# <b><i>Hint: You can use the .sort() method</i></b></p>

# In[29]:


#Given that #s listed are between 1-10
#merge two lists given
#sort merged list
#Sort Method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

merged_list = l_1 + l_2 
merged_list.sort()  

print(merged_list)



# ## Exercise 3 <br>
# <p>Square every number from 1 to 15<br>
# 

# In[31]:


#Given that total numbers square does not ** '16', 15

squares = [num**2 for num in range(1, 16)]

print(squares)


# ## Exercise 4<br>
# <p>Using List Comprehension and the given list, print out a filtered list with 
# only the names that start with the letter 'a'. 
# The names in the outputted list should be title cased and have no whitespace.<br>
# 

# In[33]:


#Given that the given names are title cased and end with no whitespaces in outcome
names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
#expected output = ['Amy', 'Alex']
#------------------------------------------------------------------

names = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']

names_filtered = [name.strip().title() for name in names if name.strip().lower().startswith('a')]

print(names_filtered)


# ## Exercise 5 <br>
# <p>Print all Prime numbers from 1 to 100<br>
# 

# In[36]:


# Given that range does not include 1 and 101 
# prime number def - a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11    
# only 1 to 100 is counted
 
for i in range(2,101): 
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")

