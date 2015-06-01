from __future__ import division
import numpy as np
import matplotlib.pyplot as pyplot
from pymongo import MongoClient
import seaborn as sns
from pylab import *
from plotly.graph_objs import *
import plotly.plotly as py
from statsmodels.nonparametric.kernel_regression import KernelReg


client=MongoClient()
db=client.twitterdb
aa=[]
aa=db.twitterdb.distinct("Created at:: ")
tweetatsec=[]
for i in aa:
    ts=db.twitterdb.find({"Created at:: ":i}).count()
    tweetatsec.append(ts)
print 'twitter:',tweetatsec

xax=[]
j=0
for i in tweetatsec:
    j+=1
    xax.append(j)

client=MongoClient()
db=client.fbdb
aa2=[]
aa2=db.fbdb.distinct("Created at:: ")
tweetatsec2=[]
for i in aa2:
    ts2=db.fbdb.find({"Created at:: ":i}).count()
    tweetatsec2.append(ts2)
print 'facebook:',tweetatsec2

xax2=[]
j=0
for i in tweetatsec2:
    j+=1
    xax2.append(j)

client=MongoClient()
db=client.instadb
aa3=[]
aa3=db.instadb.distinct("Created at:: ")
tweetatsec3=[]
for i in aa3:
    ts3=db.instadb.find({"Created at:: ":i}).count()
    tweetatsec3.append(ts3)
print 'instagram:',tweetatsec3

xax3=[]
j=0
for i in tweetatsec3:
    j+=1
    xax3.append(j)

client=MongoClient()
db=client.tumblrdb
aa4=[]
aa4=db.tumblrdb.distinct("Created at:: ")
tweetatsec4=[]
for i in aa4:
    ts4=db.tumblrdb.find({"Created at:: ":i}).count()
    tweetatsec4.append(ts4)
print 'tumblr:',tweetatsec4

xax4=[]
j=0
for i in tweetatsec4:
    j+=1
    xax4.append(j)

ax = pyplot.subplot()
x=xax
y = tweetatsec
x2=xax2
y2= tweetatsec2
x3=xax3
y3= tweetatsec3
x4=xax4
y4= tweetatsec4
pyplot.xlabel('Second')
pyplot.ylabel('Total tweet')


pyplot.scatter(x,y,color='cyan')
pyplot.scatter(x2,y2,color='red')
pyplot.scatter(x3,y3,color='blue')
pyplot.scatter(x4,y4,color='green')

kr = KernelReg(y,x,'o')
kr2 = KernelReg(y2,x2,'o')
kr3 = KernelReg(y3,x3,'o')
kr4 = KernelReg(y4,x4,'o')
pyplot.plot(x, y, '+')
pyplot.plot(x2,y2,'+')
pyplot.plot(x3,y3,'+')
pyplot.plot(x4,y4,'+')

y_pred, y_std = kr.fit(x)
y2_pred, y2_std = kr2.fit(x2)
y3_pred, y3_std = kr3.fit(x3)
y4_pred, y4_std = kr4.fit(x4)

pyplot.plot(x, y_pred,'cyan',label='twitter')
pyplot.plot(x2,y2_pred,'red',label='facebook')
pyplot.plot(x3,y3_pred,'blue',label='instagram')
pyplot.plot(x4,y4_pred,'green',label='tumblr')
pyplot.legend(loc='upper right')
pyplot.show()