import numpy as np
import math as mp
import pandas as pd

g=9.8

def yf(t,v_0,theta):
    yaxis = np.add(np.multiply(t,v_0*mp.sin(theta)),np.multiply(np.power(t,2),-g*0.5))
    return yaxis
def xf(t,v_0,theta):
    xaxis = np.multiply(t,v_0*mp.cos(theta))
    return xaxis
def time(v_0,theta):
    t = np.arange(0,2*v_0*mp.sin(theta)/g,0.01)
    return t
theta= mp.pi/4
v = 10
t = list(time(v,theta))
v_i = [v]*len(time(v,theta))
sintheta = [mp.sin(theta)]*len(time(v,theta))
costheta = [mp.cos(theta)]*len(time(v,theta))
x = list(xf(time(v,theta),v,theta))
y = list(yf(time(v,theta),v,theta))
data_dict = {
    'Time':t,
    'Initial Velocity':v_i,
    'Sine of Theta':sintheta,
    'Cosine of Theta':costheta,
    'X Position':x,
    'Y Position':y
}
data = pd.DataFrame.from_dict(data_dict)
data.to_csv(r'C:\Users\satar\OneDrive\Desktop\Projectile Machine Learning\Projectile_test.csv',index=0)