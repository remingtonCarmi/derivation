#!/usr/local/bin/python
from math import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import os
import errno

## derivation.py
## Remi Carmigniani
## Simple calculation of cos''[x] as a test


##################################################################################################################
############################			Useful functions		      ############################
##################################################################################################################
def f(x):
#test function can be modified
	return cos(x**2)
def fp(x):
#first derivative of the test function (to calculate by hand)
	return -2*x*sin(x**2)
def foward(x,h):
#Calculate the derivative using the forward scheme : f'[x] = (f[x+h]-f[x])/h
	result = (f(x+h)-f(x))/h
	return result

def backward(x,h):
#TO COMPLETE
        result=(f(x)-f(x-h))/h
	return result 


def center(x,h):
#TO COMPLETE
        result=(f(x+h)-f(x-h))/(2*h)
	return result

def error(app,ex):
#Calculate the error
#app is the approximate result
#ex is the exact result 
#Comment : actually order does not matter
	return sqrt((app-ex)**2)
#you could have used also abs(diff)

##################################################################################################################
############################				Main			      ############################
##################################################################################################################
n = 5
h = [pi/10**i for i in range(1,n+1)]
errf=[0 for i in range(n)]
errb=[0 for i in range(n)]
errc=[0 for i in range(n)]

N=200
dx = 2*pi/(N-1)
u = [dx*i for i in range(N)]
fu = [f(u[i]) for i in range(N)]
fpu = [fp(u[i]) for i in range(N)]

plt.plot(u,fu,label='x->f(x)')
plt.plot(u,fpu,label='x->fp(x)')
plt.legend()
plt.xlabel('x')
plt.savefig('fplot.png')
plt.close()

x=pi/4


for i in range(n):
	errf[i] = error(foward(x,h[i]),fp(x))
        errb[i] = error(backward(x,h[i]),fp(x))
        errc[i] = error(center(x,h[i]),fp(x))

	


#plot a log log graph
plt.loglog(h,errf,label='foward')
plt.loglog(h,errb,label='backward')
plt.loglog(h,errc,label='center')
plt.legend()
plt.title('Error')
plt.savefig('Error.png')
plt.xlabel('h')
plt.ylabel('||L[f]-df/dx||_2')
plt.show()



print 'Simulation Completed without error'


       
	
	


