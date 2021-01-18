#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[13]:


x = np.linspace(0, 10, 31)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(0.5*x))


# In[ ]:




