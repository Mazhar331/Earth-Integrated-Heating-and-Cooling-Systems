#!/usr/bin/env python
# coding: utf-8

# In[5]:


from scipy.optimize import curve_fit as fit
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error

def func(T,a,b,c):
    return a*T**2+b*T+c

T_train=np.array([-10,0,10,20,30,40,50,60])

rho_train=np.array([1.341,
1.292,
1.246,
1.204,
1.164,
1.127,
1.093,
1.06
])

popt,pcov=fit(func,T_train,rho_train)
print('Curve fit constants:')
print(popt)
print('\n')

a=popt[0]
b=popt[1]
c=popt[2]

rho_train_pred=a*T_train**2+b*T_train+c

print('Training R2 is %f'%r2_score(rho_train,rho_train_pred))
print('Training RMSE is %f'%mean_squared_error(rho_train,rho_train_pred,squared=False))
print('\n')

T_test=np.array([5,15,25,35])

rho_test=np.array([1.268,1.225,1.184,1.146])

rho_test_pred=a*T_test**2+b*T_test+c

print('Testing R2 is %f'%r2_score(rho_test,rho_test_pred))
print('Testing RMSE is %f'%mean_squared_error(rho_test,rho_test_pred,squared=False))


# In[6]:


import matplotlib.pyplot as plt

T=np.arange(-10,61)
rho=a*T**2+b*T+c

plt.scatter(T_train,rho_train,label='Data Points')
plt.plot(T,rho,label='2nd Order Curve Fit')
plt.xlabel('Temperature (degree Celsius)')
plt.ylabel('Density (kg/m3)')
plt.title('Air Density vs Temperature')
plt.legend()
plt.show()


# In[ ]:




