__author__ = 'fhca'

import matplotlib
from numpy.random import rand
from numpy import zeros
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
from matplotlib.ticker import FuncFormatter
import math


def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'

def limite_central():
    N=5000
    epsilon = 5e-2
    x1 = zeros(N)
    mu = 0.5
    for i in range(N):
        x1[i] = sum(rand(i+1)) / (i+1)

    plt.hist(x1, bins=100, range=(mu - epsilon, mu + epsilon), normed=True)
    formatter = FuncFormatter(to_percent)
    plt.gca().yaxis.set_major_formatter(formatter)

#limite_central()

k=1.75

def f(x, k):
    return 1 - k * x**2

# for k in np.arange(0, 2, .1):
#     plt.plot(f(np.arange(-1, 1.1, .1), k))

def evalua(k, N):
    x = zeros(N)
    x[0] = 0
    for i in range(N//10):
        x[0] = f(x[0], k)
    for i in range(1,N):
        x[i] = f(x[i-1], k)
        if x[i] in x[:i]:
            x=x[:i]
            break
    return x

N=500
for k in np.linspace(0, 2, num=10*N):
    r=evalua(k, N)
    plt.plot([k]*len(r), r, 'k,')

plt.show()
