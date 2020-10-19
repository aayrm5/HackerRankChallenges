n = int(input())
X = [int(i) for i in input().split()]
F = [int(i) for i in input().split()]

import statistics as st

N = sum(F)

l = []

for i in range(n):
    l += [X[i]] * F[i]

l.sort()

Q1 = st.median(l[:N//2])

if n%2 == 0:    
    Q3 = st.median(l[N//2:])
else:
    Q3 = st.median(l[N//2+1:])

print(round(float(Q3-Q1),1))