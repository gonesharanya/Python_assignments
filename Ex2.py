#!/usr/bin/env python
# coding: utf-8

# Functions are powerful. Try writing some yourself.
# 
# As before, don't forget to run the setup code below before jumping into question 1.

# In[2]:


# SETUP - Refer to Ex 1
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex2 import *
print('Setup complete.')


# # 1.
# 
# Complete the body of the following function according to its docstring.
# 
# HINT: Python has a built-in function `round`.

# In[22]:


def round_to_two_places(num):
    """Return the given number rounded to two decimal places. """
    abc = round(num, 2)
    #print(abc)
    return abc
    
    res = round_to_two_places(3.14159)
    
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    #pass"""
              

# Check your answer
q1.check()


# In[21]:


print(round_to_two_places(3.14159))


# In[24]:


# Uncomment the following for a hint
q1.hint()
# Or uncomment the following to peek at the solution
q1.solution()


# # 2.
# The help for `round` says that `ndigits` (the second argument) may be negative.
# What do you think will happen when it is? Try some examples in the following cell.

# In[25]:


round(32241.3412,-1)


# Can you think of a case where this would be useful?  Once you're ready, run the code cell below to see the answer and to receive credit for completing the problem.

# In[70]:


#A student scored 71.5 marks out of 75 in a subject, so while projecting the final marks it will be rounded off to either of the values 71 or 72.

import math
print(math.ceil(71.5))
print(math.floor(71.5))


# In[26]:



q2.solution()


# # 3.
# 
# In the previous exercise, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
# 
# Below is a simple function that will calculate the number of candies to smash for *any* number of total candies.
# 
# Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.
# 
# Update the docstring to reflect this new behaviour.

# In[59]:


def to_smash(total_candies, friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    default friends to 3
    
     to_smash(91)
     1   
    """
    to_smash = total_candies % friends
    
    return to_smash

    tobesmashed = to_smash(11, 4)
    print(tobesmashed)

# Check your answer
q3.check()


# In[46]:


9%3


# In[61]:


tobesmashed = to_smash(1, 4)
print(tobesmashed)


# In[43]:


q3.hint()


# In[52]:


q3.solution()


# # 4. (Optional)
# 
# It may not be fun, but reading and understanding error messages will be an important part of your Python career.
# 
# Each code cell below contains some commented buggy code. For each cell...
# 
# 1. Read the code and predict what you think will happen when it's run.
# 2. Then uncomment the code and run it to see what happens. (**Tip**: In the kernel editor, you can highlight several lines and press `ctrl`+`/` to toggle commenting.)
# 3. Fix the code (so that it accomplishes its intended purpose without throwing an exception)
# 
# <!-- TODO: should this be autochecked? Delta is probably pretty small. -->

# In[73]:


round(9.9999, 2)


# In[97]:


#abs() function is throwing exception so instead i used my own way of dealing with it

import math
x = -10
y = 5
# # Which of the two variables above has the smallest absolute value?
a = x * x
b = y * y
if a < b:
    smallest = a
else:
    smallest = b

    smallest_abs = math.sqrt(smallest) 
print(smallest_abs)
 #smallest_abs = min(abs(x, y))


# In[106]:


def f(x):
   y = x * x
   y = math.sqrt(y)
   return y 

print(f(-5))


# In[ ]:




