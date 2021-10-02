#!/usr/bin/env python
# coding: utf-8

# Notebooks are composed of blocks (called "cells") of text and code. Each of these is editable, though you'll mainly be editing the code cells to answer some questions.
# 
# To get started, try running the code cell below (by pressing the ► button, or clicking on the cell and pressing ctrl+enter on your keyboard).

# In[ ]:


print("You've successfully run some Python code")
print("Congratulations!")


# # Setup for running exercise
# 
# 1. Download learntools-master by clicking [here](https://drive.google.com/file/d/1aZx9Lk1nvSwqqxyPEYnaiHhbJ40FMkew/view?usp=sharing)
# 2. Extract the zip in the same folder you are running this notebook
# 3. Right Click the zip and select 7-zip --> Extract Here
# 4. Copy the "learntools" folder to C:\ProgramData\Anaconda3\Lib\site-packages (*tip: ProgramData folder is hidden)

# Try adding another line of code in the cell above and re-running it. 
# 
# Now let's get a little fancier:  Add a new code cell by clicking on an existing code cell, hitting the escape key, and then hitting the `a` or `b` key.  The `a` key will add a cell above the current cell, and `b` adds a cell below.
# 
# Great! Now you know how to use Notebooks.
# 
# Each hands-on exercise starts by setting up our feedback and code checking mechanism. Run the code cell below to do that. Then you'll be ready to move on to question 0.

# In[ ]:


from learntools.core import binder; binder.bind(globals())
from learntools.python.ex1 import *
print("Setup complete! You're ready to start question 0.")


# # 0.
# 
# *This is a silly question intended as an introduction to the format we use for hands-on exercises throughout this course.*
# 
# **What is your favorite color? **
# 
# To complete this question, create a variable called `color` in the cell below with an appropriate value. The function call `q0.check()` (which we've already provided in the cell below) will check your answer.

# In[ ]:


# create a variable called color with an appropriate value on the line below
# (Remember, strings in Python must be enclosed in 'single' or "double" quotes)

# *Write you answer here*

# Check your answer
q0.check()


# Didn't get the right answer? How do you not even know your own favorite color?!
# 
# Delete the `#` in the line below to make one of the lines run. You can choose between getting a hint or the full answer by choosing which line to remove the `#` from. 
# 
# Removing the `#` is called uncommenting, because it changes that line from a "comment" which Python doesn't run to code, which Python does run.

# In[ ]:


#q0.hint()
#q0.solution()


# The upcoming questions work the same way. The only thing that will change are the question numbers. For the next question, you'll call `q1.check()`, `q1.hint()`, `q1.solution()`, for question 2, you'll call `q2.check()`, and so on.

# <hr/>
# 
# # 1.
# 
# Complete the code below. In case it's helpful, here is the table of available arithmetic operations:
# 
# 
# 
# | Operator     | Name           | Description                                            |
# |--------------|----------------|--------------------------------------------------------|
# | ``a + b``    | Addition       | Sum of ``a`` and ``b``                                 |
# | ``a - b``    | Subtraction    | Difference of ``a`` and ``b``                          |
# | ``a * b``    | Multiplication | Product of ``a`` and ``b``                             |
# | ``a / b``    | True division  | Quotient of ``a`` and ``b``                            |
# | ``a // b``   | Floor division | Quotient of ``a`` and ``b``, removing fractional parts |
# | ``a % b``    | Modulus        | Integer remainder after division of ``a`` by ``b``     |
# | ``a ** b``   | Exponentiation | ``a`` raised to the power of ``b``                     |
# | ``-a``       | Negation       | The negative of ``a``                                  |
# 
# <span style="display:none"></span>
# 

# In[ ]:


pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter


# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared


# Check your answer
q1.check()


# In[ ]:


# Uncomment and run the lines below if you need help.
# q1.hint()
# q1.solution()


# <hr/>
# 
# # 2.
# 
# Add code to the following cell to swap variables `a` and `b` (so that `a` refers to the object previously referred to by `b` and vice versa).

# In[ ]:


########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
q2.store_original_ids()
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.


######################################################################

# Check your answer
q2.check()


# In[ ]:


#q2.hint()


# In[ ]:


#q2.solution()


# <hr/>
# 
# # 3a.
# 
# Add parentheses to the following expression so that it evaluates to 1.

# In[ ]:


5 - 3 // 2


# In[ ]:


#q3.a.hint()


# In[ ]:


# Check your answer (Run this code cell to receive credit!)
#q3.a.solution()


# # 3b.  <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
# 
# <small>Questions, like this one, marked a spicy pepper are a bit harder.</small>
# 
# Add parentheses to the following expression so that it evaluates to 0.

# In[ ]:


8 - 3 * 2 - 1 + 1


# In[ ]:


#q3.b.hint()


# In[ ]:


# Check your answer (Run this code cell to receive credit!)
#q3.b.solution()


# <hr/>
# 
# # 4. 
# Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves.
# For the sake of their friendship, any candies left over will be smashed. For example, if they collectively
# bring home 91 candies, they'll take 30 each and smash 1.
# 
# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.

# In[ ]:


# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = -1

# Check your answer
q4.check()


# In[ ]:


#q4.hint()
#q4.solution()

