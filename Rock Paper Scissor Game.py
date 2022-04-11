#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


def play():
  User = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
  Computer = random.choice(['r','p','s'])

  if User == Computer:
      return 'It\'s a tie.'
  # r > s, s > p, p>r
  if is_win(User, Computer):
      return 'You won!'

  return 'You Lost!'


#  choice(seq)- Choose a random element from a non-empty sequence.
#  
#  random -  integers
# pick random element pick random sample pick weighted random sample generate random permutation

# In[3]:


def is_win(player, opponent):
    # return true if player wins
    # r>s, s>p, p>r
    if (player =='r' and opponent == 's') or (player =='s' and opponent == 'p') or (player =='p' and opponent == 'r'):
      return True


# In[5]:


print(play())

