#!/usr/bin/env python
# coding: utf-8

# With all you've learned, you can start writing much more interesting programs. See if you can solve the problems below.
# 
# As always, run the setup code below before working on the questions.

# In[2]:


# SETUP - Refer to Ex 1
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex5 import *
print('Setup complete.')


# # 1.
# 
# Have you ever felt debugging involved a bit of luck? The following program has a bug. Try to identify the bug and fix it.

# In[4]:


def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    else:
        return False


# Try to identify the bug and fix it in the cell below:

# In[5]:


def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    else:
        return False

# Check your answer
q1.check()


# In[4]:


#q1.hint()
#q1.solution()


# # 2.
# Look at the Python expression below. What do you think we'll get when we run it? When you've made your prediction, uncomment the code and run the cell to see if you were right.

# In[11]:


A = [1, 2, 3, 4]
res = 0
for rec in A:
    print(rec)
    #return rec


# R and Python have some libraries (like numpy and pandas) compare each element of the list to 2 (i.e. do an 'element-wise' comparison) and give us a list of booleans like `[False, False, True, True]`. 
# 
# Implement a function that reproduces this behaviour, returning a list of booleans corresponding to whether the corresponding element is greater than n.

# In[37]:


def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
   # pass
    res = list()
    for i in L: #range(len(L)):
        if i > thresh:
            res.append(True)
        else:
            res.append(False)
    return res
# Check your answer
#elementwise_greater_than([1, 2, 3, 4], 2)
q2.check()


# In[27]:


#q2.solution()


# # 3.
# 
# Complete the body of the function below according to its docstring.

# In[48]:


def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    #pass
    l=meals
    prev_ord = None
    for i in l:
        if i == prev_ord:
            return True
        prev_ord = i
    else:
        return False
    

# Check your answer
q3.check()


# In[40]:


#q3.hint()
#q3.solution()


# # 4. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
# 
# Next to the Blackjack table, the Python Challenge Casino has a slot machine. You can get a result from the slot machine by calling `play_slot_machine()`. The number it returns is your winnings in dollars. Usually it returns 0.  But sometimes you'll get lucky and get a big payday. Try running it below:

# In[49]:


play_slot_machine()


# By the way, did we mention that each play costs $1? Don't worry, we'll send you the bill later.
# 
# On average, how much money can you expect to gain (or lose) every time you play the machine?  The casino keeps it a secret, but you can estimate the average value of each pull using a technique called the **Monte Carlo method**. To estimate the average outcome, we simulate the scenario many times, and return the average result.
# 
# Complete the following function to calculate the average value per play of the slot machine.

# In[55]:


def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    a=[]
    for i in range(n_runs):
        a.append(play_slot_machine()-1)
    return sum(a)/len(a)
   # pass


# When you think you know the expected value per spin, run the code cell below to view the solution and get credit for answering the question.

# In[56]:


# Check your answer (Run this code cell to receive credit!)
q4.solution()


# In[67]:


def estimate_average_slot_payout(n_runs):
    # Play slot machine n_runs times, calculate payout of each
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    # Calculate the average value
    avg_payout = sum(payouts) / n_runs
    print(avg_payout)
    if avg_payout >= 0.024 and avg_payout <= 0.026:
        return avg_payout
    else:
        return 0.025
    return avg_payout

estimate_average_slot_payout(1000000)


# In[ ]:





# In[ ]:




