#!/usr/bin/env python
# coding: utf-8

# # programe that print the prime number using a function 

# In[10]:


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
print("Prime numbers between 1 and 19:")
for num in range(1, 20):
    if is_prime(num):
        print(num)


# In[ ]:




