#!/usr/bin/env python
# coding: utf-8

# # Try It Yourself
# 
# There are only three problems in this last set of exercises, but they're all pretty tricky, so be on guard! 
# 
# Run the setup code below before working on the questions.

# In[2]:


# SETUP - Refer to Ex 1
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex7 import *
print('Setup complete.')


# # 1.
# 
# After completing the exercises on lists and tuples, Jimmy noticed that, according to his `estimate_average_slot_payout` function, the slot machines at the Learn Python Casino are actually rigged *against* the house, and are profitable to play in the long run.
# 
# Starting with $200 in his pocket, Jimmy has played the slots 500 times, recording his new balance in a list after each spin. He used Python's `matplotlib` library to make a graph of his balance over time:

# In[4]:


# Import the jimmy_slots submodule
from learntools.python import jimmy_slots
# Call the get_graph() function to get Jimmy's graph
graph = jimmy_slots.get_graph()
graph


# In[15]:


#print(jimmy_slots.methods)
from inspect import getmembers, isfunction
print(getmembers(jimmy_slots, isfunction))


# As you can see, he's hit a bit of bad luck recently. He wants to tweet this along with some choice emojis, but, as it looks right now, his followers will probably find it confusing. He's asked if you can help him make the following changes:
# 
# 1. Add the title "Results of 500 slot machine pulls"
# 2. Make the y-axis start at 0. 
# 3. Add the label "Balance" to the y-axis
# 
# After calling `type(graph)` you see that Jimmy's graph is of type `matplotlib.axes._subplots.AxesSubplot`. Hm, that's a new one. By calling `dir(graph)`, you find three methods that seem like they'll be useful: `.set_title()`, `.set_ylim()`, and `.set_ylabel()`. 
# 
# Use these methods to complete the function `prettify_graph` according to Jimmy's requests. We've already checked off the first request for you (setting a title).
# 
# (Remember: if you don't know what these methods do, use the `help()` function!)

# In[16]:


def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(0)
    #graph.format('${x:1.2f}')
    graph.set_ylabel("Balance")
    #graph.set_format('${x:1.2f')
    # Complete steps 2 and 3 here
    # Use automatic StrMethodFormatter
#     graph.set_major_formatter('${x:1.2f}')

#     graph.set_tick_params(which='major', labelcolor='green',
#                          labelleft=True, labelright=False)
    #new_labels = ['${}'.format(int(amt)) for amt in graph]

graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph


# **Bonus:** Can you format the numbers on the y-axis so they look like dollar amounts? e.g. $200 instead of just 200.
# 
# (We're not going to tell you what method(s) to use here. You'll need to go digging yourself with `dir(graph)` and/or `help(graph)`.)

# In[11]:


# Check your answer (Run this code cell to receive credit!)
q1.solution()


# # 2. <span title="Spicy" style="color: coral">🌶️🌶️</span>
# 
# This is a very challenging problem.  Don't forget that you can receive a hint!
# 
# Luigi is trying to perform an analysis to determine the best items for winning races on the Mario Kart circuit. He has some data in the form of lists of dictionaries that look like...
# 
#     [
#         {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
#         {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
#         # Sometimes the racer's name wasn't recorded
#         {'name': None, 'items': ['mushroom',], 'finish': 2},
#         {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
#     ]
# 
# `'items'` is a list of all the power-up items the racer picked up in that race, and `'finish'` was their placement in the race (1 for first place, 3 for third, etc.).
# 
# He wrote the function below to take a list like this and return a dictionary mapping each item to how many times it was picked up by first-place finishers.

# In[17]:


def best_items(racers):
    """Given a list of racer dictionaries, return a dictionary mapping items to the number
    of times those items were picked up by racers who finished in first place.
    """
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts


# He tried it on a small example list above and it seemed to work correctly:

# In[18]:


sample = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]
best_items(sample)


# However, when he tried running it on his full dataset, the program crashed with a `TypeError`.
# 
# Can you guess why? Try running the code cell below to see the error message Luigi is getting. Once you've identified the bug, fix it in the cell below (so that it runs without any errors).

# In[22]:


# Import luigi's full dataset of race data
from learntools.python.luigi_analysis import full_dataset

# Fix me!
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                str(i)+str(1), str(len(racers)), racer['name'])
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
best_items(full_dataset)


# In[ ]:


#q2.hint()


# In[ ]:


# Check your answer (Run this code cell to receive credit!)
q2.solution()


# # 3. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
# 
# Suppose we wanted to create a new type to represent hands in blackjack. One thing we might want to do with this type is overload the comparison operators like `>` and `<=` so that we could use them to check whether one hand beats another. e.g. it'd be cool if we could do this:
# 
# ```python
# >>> hand1 = BlackjackHand(['K', 'A'])
# >>> hand2 = BlackjackHand(['7', '10', 'A'])
# >>> hand1 > hand2
# True
# ```
# 
# Well, we're not going to do all that in this question (defining custom classes is a bit beyond the scope of these lessons), but the code we're asking you to write in the function below is very similar to what we'd have to write if we were defining our own `BlackjackHand` class. (We'd put it in the `__gt__` magic method to define our custom behaviour for `>`.)
# 
# Fill in the body of the `blackjack_hand_greater_than` function according to the docstring.

# In[28]:


def blackjack_hand_greater_than(hand_1, hand_2):
    res = 0
    a_used = 0
    val = 0
    for i in hand_1:
        if i in ('J', 'Q', 'K'):
            val = 10
        elif i == 'A':
            #val1 = 1
            val = 11
            a_used = a_used + 1
            
        res = res + val
    if a_used > 0 and res >= 20:
        res = res - 10   
    
    res1 = 0
    b_used = 0
    val = 0
    for i in hand_2:
        if i in ('J', 'Q', 'K'):
            val = 10
        elif i == 'A':
            #val1 = 1
            val = 11
            b_used = b_used + 1
        print(val)
            
        res1 = res1 + val
    if b_used > 0 and res1 >= 20:
        res1 = res1 - 10  
    print(res1)
    print(res)
    if res > res1:
        return True
    else:
        return False
    
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    pass

# Check your answer
q3.check()


# In[ ]:


#q3.hint()
#q3.solution()


# # The End
# 
# You've finished the Python course. Congrats!
# 
# Happy Pythoning!
