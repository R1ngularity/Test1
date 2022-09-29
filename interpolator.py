import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import linalg
import scipy.interpolate as interpolate





def interpol():
    """
    opens schroedinger.inp and interpolates the given Potential
    saves the calculated xy points in potential.dat
    -------


    """
    f = open("schroedinger.inp", "r")

    pot = []
    for x in f:
        pot.append(x.split())
    f.close() 

    xpot = []
    ypot = []
    for i in range(int(pot[4][0])):
        xpot.append(float(pot[i+5][0]))
        ypot.append(float(pot[i+5][1]))



    x = np.linspace(float(pot[1][0]), float(pot[1][1]), int(pot[1][2]))
    potpoints = []
    potxpoints = []


    if str(pot[3][0]) == 'linear':
        z = interpolate.interp1d(xpot, ypot, kind = "linear")
        
    elif pot[3][0] == "polynomial":
        z = interpolate.lagrange(xpot, ypot)
        
    elif pot[3][0] == "cspline":
        z = interpolate.interp1d(xpot, ypot, kind = "cubic")
        
    else:
        return False
        pass
        

    f2 = open("potential.dat", "w")
    for i in x:
        potpoints.append(z(i))
    
    for i in x:
        potxpoints.append(i)
    
    
    for i in range(len(potpoints)):
        f2.write(str(potxpoints[i]))
        f2.write(" ")
        f2.write(str(potpoints[i]))        
        f2.write('\n')
        
    f2.close()    
    
    
    
    plt.plot(potxpoints, potpoints, '-')
    plt.show()

