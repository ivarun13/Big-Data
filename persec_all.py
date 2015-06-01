from __future__ import division
import numpy as np
import matplotlib.pyplot as pyplot
from pymongo import MongoClient
import seaborn as sns
from pylab import *
from statsmodels.nonparametric.kernel_regression import KernelReg


client=MongoClient()
db=client.twitterdb
aa=[]
aa=db.twitterdb.distinct("Created at:: ")
tweetatsec=[]
for i in aa:
    ts=db.twitterdb.find({"Created at:: ":i}).count()
    tweetatsec.append(ts)
print tweetatsec

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
print tweetatsec2

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
print tweetatsec3

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
print tweetatsec4

xax4=[]
j=0
for i in tweetatsec4:
    j+=1
    xax4.append(j)

x=xax
y = tweetatsec
x2=xax2
y2= tweetatsec2
x3 = xax3
y3 = tweetatsec3
x4=xax4
y4 = tweetatsec4
pyplot.xlabel('Second')
pyplot.ylabel('Total tweet')
pyplot.scatter(x,y,color='red')






pyplot.title('Twitter', bbox={'facecolor':'1.0', 'pad':5})
pyplot.show()

pyplot.scatter(x2,y2,color='blue')
pyplot.title('facebook', bbox={'facecolor':'1.0', 'pad':5})
pyplot.show()
pyplot.scatter(x3,y3,color='cyan')
pyplot.title('instagram', bbox={'facecolor':'1.0', 'pad':5})
pyplot.show()
pyplot.scatter(x4,y4,color='green')
pyplot.title('Tumblr', bbox={'facecolor':'1.0', 'pad':5})
pyplot.show()

