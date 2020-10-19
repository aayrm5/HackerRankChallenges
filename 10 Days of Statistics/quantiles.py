n = int(input())
arr = [int(x) for x in input().split()]

arr = sorted(arr)

def median(arr):

    if len(arr)%2==0:
        return int((arr[len(arr)//2-1]+arr[(len(arr)//2)])/2)
    else:
        return int(arr[len(arr)//2])

def quantiles(arr):
    if len(arr)%2==0:
        Q1 = median(arr[:len(arr)//2])
        Q3 = median(arr[len(arr)//2:])
    else:
        Q1 = median(arr[:len(arr)//2])
        Q3 = median(arr[len(arr)//2+1:])
        
    print(Q1)
    print(median(arr))
    print(Q3)    

quantiles(arr)