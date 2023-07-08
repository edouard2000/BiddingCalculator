#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

def clear_screen():
    os.system("clear")

bids = {}

def bidders():
    name = input("What is your name: ")
    price = int(input("What is your bid: "))
    bids[name] = price

is_True = True
while is_True:
    answer = input("Want to bid? 'yes' or 'no': ").lower()
    if answer == "yes":
        bidders()
    elif answer == "no":
        is_True = False
high_bid = 0
winner = ""

for name, bid in bids.items():
    if bid > high_bid:
        high_bid = bid
        winner = name

print(f"The highest bid is: {high_bid} and was donated by {winner}.")

       
    
        
        
    




    

        
     
            
        
   







# In[ ]:




