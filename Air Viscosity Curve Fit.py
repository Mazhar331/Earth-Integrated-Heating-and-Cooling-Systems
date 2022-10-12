#!/usr/bin/env python
# coding: utf-8

# In[3]:


from scipy.optimize import curve_fit as fit
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error

def func(T,a,b):
    return a*T+b

T_train=np.array([-10,0,10,20,30,40,50,60])

viscosity_train=np.array([1.665E-05,
1.715E-05,
1.764E-05,
1.813E-05,
1.860E-05,
1.907E-05,
1.953E-05,
1.999E-05
])

popt,pcov=fit(func,T_train,viscosity_train)
print('Curve fit constants:')
print(popt)
print('\n')

a=popt[0]
b=popt[1]

viscosity_train_pred=a*T_train+b

print('Training R2 is %f'%r2_score(viscosity_train,viscosity_train_pred))
print('Training RMSE is %0.16f'%mean_squared_error(viscosity_train,viscosity_train_pred,squared=False))
print('\n')

T_test=np.array([5,15,25,35])

viscosity_test=np.array([17.4e-6,17.89e-6,18.37e-6,18.84e-6])

viscosity_test_pred=a*T_test+b

print('Testing R2 is %f'%r2_score(viscosity_test,viscosity_test_pred))
print('Testing RMSE is %0.16f'%mean_squared_error(viscosity_test,viscosity_test_pred,squared=False))


# In[4]:


import matplotlib.pyplot as plt

T=np.arange(-10,61)
viscosity=a*T+b

plt.scatter(T_train,viscosity_train,label='Data Points')
plt.plot(T,viscosity,label='Linear Fit')
plt.xlabel('Temperature (degree Celsius)')
plt.ylabel('Viscosity (Pa.s)')
plt.title('Air Viscosity vs Temperature')
plt.legend()
plt.show()


# In[ ]:




