N = int(input().strip())

X = list(map(int,input().strip().split()))
W = list(map(int,input().strip().split()))

NUM = 0
for i in range(N):
    NUM = NUM + (X[i]*W[i])

print("{0:.1f}".format(NUM/sum(W)))
#______________________________________
#Using Numpy
import numpy as np

print(np.dot(X,W)/sum(W))