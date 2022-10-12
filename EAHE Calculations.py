#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

Tw=np.array([23,20.5,20,21,22,23,25,27.5,28.5,27.5,26.5,25]) # deg C
Tin_min=np.array([8,11,16,23,27,28,28,27,25,21,14,9]) # deg C
Tin_max=np.array([20,24,30,37,40,39,35,34,34,33,28,22]) # deg C

air_flow=0.02643 # m^3/s
Cp=1005 # J kg^-1 K^-1

blower_power=28 # W

pipe_ID=0.15 # m
pipe_length=30.48 # m
area=14.363 # m^2

v=air_flow/(math.pi*pipe_ID**2/4) # m/s
h=2.8+3*v # W m^-2 K^-1

m_dot_min=air_flow*(1.38690477e-05*Tin_min**2-4.69226191e-03*Tin_min+1.29223214e+00)
m_dot_max=air_flow*(1.38690477e-05*Tin_max**2-4.69226191e-03*Tin_max+1.29223214e+00)

Tout_min=Tw+(Tin_min-Tw)*np.exp(-math.pi*pipe_ID*h*pipe_length/(m_dot_min*Cp))
print('Minimum outlet temperatures:')
print(Tout_min)
print('\n')

Tout_max=Tw+(Tin_max-Tw)*np.exp(-math.pi*pipe_ID*h*pipe_length/(m_dot_max*Cp))
print('Maximum outlet temperatures:')
print(Tout_max)
print('\n')

heat_duty_min=m_dot_min*Cp*np.abs(Tout_min-Tin_min)
print('Heat duty for minimum inlet temperatures:')
print(heat_duty_min)
print('\n')

heat_duty_max=m_dot_max*Cp*np.abs(Tout_max-Tin_max)
print('Heat duty for maximum inlet temperatures:')
print(heat_duty_max)
print('\n')

LMTD_min=np.abs(((Tw-Tout_min)-(Tw-Tin_min))/np.log((Tw-Tout_min)/(Tw-Tin_min)))
print('LMTD for minimum inlet temperatures:')
print(LMTD_min)
print('\n')

LMTD_max=np.abs(((Tw-Tout_max)-(Tw-Tin_max))/np.log((Tw-Tout_max)/(Tw-Tin_max)))
print('LMTD for maximum inlet temperatures:')
print(LMTD_max)
print('\n')

h_calc_min=heat_duty_min/(area*LMTD_min)
print('Calculated h for minimum inlet temperatures:')
print(h_calc_min)
print('\n')

h_percent_error_min=np.abs(h_calc_min-h)*100/h
print('Percent error in h for minimum inlet temperatures:')
print(h_percent_error_min)
print('\n')

h_calc_max=heat_duty_max/(area*LMTD_max)
print('Calculated h for maximum inlet temperatures:')
print(h_calc_max)
print('\n')

h_percent_error_max=np.abs(h_calc_max-h)*100/h
print('Percent error in h for maximum inlet temperatures:')
print(h_percent_error_max)
print('\n')

COP_min=heat_duty_min/blower_power
print('COP for minimum inlet temperatures:')
print(COP_min)
print('\n')

COP_max=heat_duty_max/blower_power
print('COP for maximum inlet temperatures:')
print(COP_max)
print('\n')

effectiveness_min=np.abs((Tout_min-Tin_min)/(Tw-Tin_min))
print('Effectiveness for minimum inlet temperatures:')
print(effectiveness_min)
print('\n')

effectiveness_max=np.abs((Tout_max-Tin_max)/(Tw-Tin_max))
print('Effectiveness for maximum inlet temperatures:')
print(effectiveness_max)
print('\n')

COP_avg=(np.sum(COP_min)+np.sum(COP_max))/24
print('Average COP: %f'%COP_avg)
print('\n')

effectiveness_avg=(np.sum(effectiveness_min)+np.sum(effectiveness_max))/24
print('Average effectiveness: %f'%effectiveness_avg)
print('\n')

monthly_Tout_range=np.abs(Tout_max-Tout_min)
print('Monthly outlet temperature range:')
print(monthly_Tout_range)
print('\n')

plt.figure(figsize=(8,5))
plt.plot([0,1,2,3,4,5,6,7,8,9,10,11],Tout_min,label='Minimum Outlet Temperatures',color='blue')
plt.plot([0,1,2,3,4,5,6,7,8,9,10,11],Tout_max,label='Maximum Outlet Temperatures',color='red')
plt.title('Tempearture Band Plot')
plt.xlabel('Months')
plt.ylabel('Temperature (deg C)')
plt.gca().xaxis.set_major_locator(mticker.FixedLocator(np.arange(len([0,1,2,3,4,5,6,7,8,9,10,11]))))
plt.gca().xaxis.set_major_formatter(mticker.FixedFormatter(np.array(['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])))
ax=plt.gca()
ax.set_ylim(15,30)
plt.legend(loc=2)
plt.show()

month_avg_COP=(COP_min+COP_max)/2

plt.figure(figsize=(8,5))
plt.plot([0,1,2,3,4,5,6,7,8,9,10,11],month_avg_COP)
plt.title('Monthly Average COP Plot')
plt.xlabel('Months')
plt.ylabel('COP')
plt.gca().xaxis.set_major_locator(mticker.FixedLocator(np.arange(len([0,1,2,3,4,5,6,7,8,9,10,11]))))
plt.gca().xaxis.set_major_formatter(mticker.FixedFormatter(np.array(['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'])))
plt.show()

data={'Month':['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'],'Ground Temp':Tw,'Min Temp':Tin_min,'Max Temp':Tin_max,'Outlet Temp for Min Inlet Temp':Tout_min,'Outlet Temp for Max Inlet Temp':Tout_max,'Heat Duty for Min Inlet Temp':heat_duty_min,'Heat Duty for Max Inlet Temp':heat_duty_max,'COP for Min Inlet Temp':COP_min,'COP for Max Inlet Temp':COP_max,'Average Monthly COP':month_avg_COP,'Effectiveness for Min Inlet Temp':effectiveness_min,'Effectiveness for Max Inlet Temp':effectiveness_max}
df=pd.DataFrame(data)
df.to_excel('EAHE Month-Wise Data.xlsx')


# In[ ]:




