#Calculating the weighted mean of X with respect to W; 
# N is the number of observations;

N = int(input().strip())

X = list(map(int,input().strip().split()))
W = list(map(int,input().strip().split()))

NUM = 0
for i in range(N):
    NUM = NUM + (X[i]*W[i])

print("{0:.1f}".format(NUM/sum(W)))

#list comprehensions method
print(round(sum([X[i]*W[i] for i in range(N)])/sum(W),1))

#______________________________________
#Using Numpy
import numpy as np

print(np.dot(X,W)/sum(W))

#Another way to do this:
np.average(X,None,W)