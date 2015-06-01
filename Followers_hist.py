import sys
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from pandas import *

f = open('followers.txt', 'r')
lines = f.readlines()
f.close()
i=1
j=1
facebook=[]
twitter=[]
instagram=[]
tumblr=[]
for line in lines:
	data =line.strip().split('\t')
	if j%4 == 1 :
		facebook.append(int(data[1]))
		j+=1
	elif j%4 == 2 :
		twitter.append(int(data[1]))
		j+=1
	elif j%4 == 3 :
		instagram.append(int(data[1]))
		j+=1
	else :
		tumblr.append(int(data[1]))
		j+=1
print facebook
print twitter
print instagram
print tumblr
df = DataFrame({'facebook':facebook,'Twitter':twitter,'Instagram':instagram,'Tumblr':tumblr})
df.plot(kind='bar', color='rbmcy')
plt.show()