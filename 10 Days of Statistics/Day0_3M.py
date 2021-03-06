N = int(input().strip())

arr = [int(i) for i in input().strip().split(' ')]
arr.sort()
arr
#Mean
print("{0:.1f}".format(sum(arr)/N))

#Median
if N%2 == 0:
    print("{0:.1f}".format(0.5*(arr[int(N/2)-1]
                           +arr[int(N/2)])))
else:
    print("{0:.1f}".format(arr[int(N/2)]))

#Mode
counts = []
for i in arr:
    counts.append(arr.count(i))
    
if max(counts) > 1:
    print(arr[counts.index(max(counts))])
else:
    print(min(arr))
    
#____________________________________________
#Alternatively you could simply use Python's bult-in libraries to calc it
import numpy as np
from scipy import stats 

N = int(input().strip())
arr = list(map(int,input().strip().split()))   

print("{0:.1f}".format(np.mean(arr)))
print("{0:.1f}".format(np.median(arr)))
print(int(stats.mode(arr)[0]))