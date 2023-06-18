
# coding: utf-8

# In[35]:


import matplotlib.pyplot as plt
import math


# In[2]:


mu = 50
theta = 0.5  
eta = 1


#coefficients
g=0.5 
hsr=0.5
hrd= 0.5
h = 0.5
# constants
A=1
B=1


# In[29]:



ps = 0.02                          # variables
lambda_2 = 10

lambda_2_low = 0    
lambda_2_up = 160


ib = ps*(abs(h)*abs(h))
a = mu * (1-theta) / 2
row=
C = 2*row*hsr*hsr/(1-theta)((row*sigma1*sigma1)+(sigma2*sigma2))


Es = eta*theta*T*pb*g*g
pt = ((2*theta)/1-theta)*pb*g*g
pb = (lambda1*g*g-B)/A


# In[30]:


lambda_2_opt = []
ith = 0
ith_list = []
while ith<=0.5:
    ith_list.append(ith)
    count = lambda_2_low
    while count<=lambda_2_up:
        pb = 65
        u_b2 = lambda_2*(1-theta)*ps*(abs(h)*abs(h))
        if ib*lambda_2*count <= ith:
            u_b2 = lambda_2*count*(1-theta)*ps*(abs(h)*abs(h))
        else:
            u_b2 = lambda_2*count*(1-theta)*ith
        count += eta
    lambda_2_opt.append(lambda_2*u_b2)
    print(u_b2)
    ith += 0.05


# In[31]:


lambda_2_opt


# In[37]:


plt.plot(ith_list,lambda_2_opt)


# In[33]:


ith_list

