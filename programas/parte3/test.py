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


def evalua(k, N):

    def f(x):
        return 1 - k * x**2

    # for k in np.arange(0, 2, .1):
    #     plt.plot(f(np.arange(-1, 1.1, .1), k))
    x = zeros(N)
    x[0] = 0
    for i in range(N//10):
        x[0] = f(x[0])
    for i in range(1,N):
        x[i] = f(x[i-1])
        #if x[i] in x[:i]:
        #    x=x[:i]
        #    break
    return x

def diagrama_de_orbitas():
    N=500
    for k in np.linspace(1,2, num=N):
        r=evalua(k, N)
        plt.plot([k]*len(r), r, 'k,')


#diagrama_de_orbitas()

def limite_central2():
    N=5000
    k = 1.99999999
    r=evalua(k, N)
    np.random.shuffle(r)

    epsilon = .1
    x1 = zeros(N)
    mu = 0
    for i in range(N):
        np.random.shuffle(r)
        x1[i] = sum(r[:i]) / (i+1)

    plt.hist(x1, bins=1000, range=(mu - epsilon, mu + epsilon), normed=True)
    formatter = FuncFormatter(to_percent)
    plt.gca().yaxis.set_major_formatter(formatter)

limite_central2()

plt.show()
