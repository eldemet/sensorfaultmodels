# Sensor fault models based on Reppa et al. 2016
# Matlab code: https://github.com/eldemet/sensorfaultmodels/blob/main/sensorfaultmodels.m

import matplotlib.pyplot as plt
import numpy as np


class struct():
    t1 = {}
    t2 = {}
    a1 = {}
    a2 = {}
    functiontype = {}
    functionpar = {}

n = 100
y0 = 10 * np.ones(n) #+ 0.5* sin(1:100);

plt.plot(y0, 'b')

events = struct()
events.t1[0] = 2             # time step start
events.t2[0] = 10            # time step end
events.a1[0] = 0.5           # parameter in occurance evolution profile function
events.a2[0] = 0.7           # parameter in dissapearance evolution profile function
events.functiontype[0] = 'constant'
events.functionpar[0] = 3    # constant difference

events.t1[1] = 20            # time step start
events.t2[1] = 30            # time step end
events.a1[1] = 999999        # parameter in occurance evolution profile function
events.a2[1] = 1             # parameter in dissapearance evolution profile function
events.functiontype[1] = 'drift'
events.functionpar[1] = 1    # constant difference

events.t1[2] = 40            # time step start
events.t2[2] = 50            # time step end
events.a1[2] = 100           # parameter in occurance evolution profile function
events.a2[2] = 100           # parameter in dissapearance evolution profile function
events.functiontype[2] = 'normal'
events.functionpar[2] = 2    # constant difference

events.t1[3] = 70            # time step start
events.t2[3] = np.inf        # time step end
events.a1[3] = 999999        # parameter in occurance evolution profile function
events.a2[3] = 0.7           # parameter in dissapearance evolution profile function
events.functiontype[3] = 'percentage'
events.functionpar[3] = .1   # constant difference

events.t1[4] = 80            # time step start
events.t2[4] = np.inf        # time step end
events.a1[4] = 999999        # parameter in occurance evolution profile function
events.a2[4] = 0.7           # parameter in dissapearance evolution profile function
events.functiontype[4] = 'stuckzero'
events.functionpar[4] = 0    # constant difference

n = len(events.t1)

df = np.zeros(len(y0))
beta = np.zeros(len(y0))
f = np.zeros(len(y0))
y = []

for k in range(0, len(y0)):
    y0k = y0[k]
    for i in range(0, n):
        T1 = events.t1[i]
        T2 = events.t2[i]
        a1 = events.a1[i]
        a2 = events.a2[i]
        ftype = events.functiontype[i]
        fpar = events.functionpar[i]
        b1 = 0
        b2 = 0
        if k >= T1:
            b1 = 1 - np.exp(- a1 * (k-T1))

        if k >= T2:
            b2 = 1 - np.exp(- a2 * (k-T2))

        b = b1 - b2
        phi = 0

        if b > 0:
            if ftype == 'constant':
                phi = fpar
            if ftype == 'drift':
                phi = fpar * (k - T1)
            if ftype == 'normal':
                phi = np.random.normal(0, fpar)
            if ftype == 'percentage':
                phi = fpar*y0k
            if ftype == 'stuckzero':
                phi = -y0k

        df = b * phi

        y0k = y0k + df

    y.append(y0k)

plt.plot(y, 'r')
plt.show()