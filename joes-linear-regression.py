from random import random
import sympy as sp

xData = [8,2,11,6,5,4,12,9,6,1]
yData = [3,10,3,6,8,12,1,4,9,14]

W0,W1 = sp.symbols('W0 W1')

cost = 0
# GET COST FUNCTION
iteration = 0
for Xi in xData:
    # (actual - predicted) squared
    # predicted = (y-int + slope*x)
    cost += (yData[iteration]-(W0+W1*Xi))**2
    iteration+=1
cost = cost / ((len(xData)))
lr = 0.01

# GET PARTIAL DER
W0Diff = sp.diff(cost,W0)
W1Diff = sp.diff(cost,W1)

# ADJUST WEIGHTS
W0value = random()
W1value = random()
for i in range(1000):
    # TRAIN W0
    W0slope = W0Diff.subs(W0,W0value)
    W0slope = W0slope.subs(W1,W1value)
    W0value = W0value - lr*W0slope
    # TRAIN W1
    W1slope = W1Diff.subs(W0,W0value)
    W1slope = W1slope.subs(W1,W1value)
    W1value = W1value - lr*W1slope

print('y =',W0value,'+ (x *',W1value,')')
