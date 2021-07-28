from math import sqrt



def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x :
            return i
    return -1   

def binarySearch(arr , lo , hi , x):
    if lo <= hi :
        mid = lo + (hi - lo ) // 2
        if arr[mid] == x :
            return mid
        if arr[mid] < x :
            return binarySearch(arr,mid+1,hi,x)    
        if arr[mid] > x :
            return binarySearch(arr,lo,mid-1,x)
    return -1        

def jumpSearch(arr , x):
    size = len(arr)
    step = int(sqrt(size))
    prev = 0
    while arr[min(step , size) -1 ] < x :
        prev = step 
        step += int(sqrt(size))
        if prev > size :
            return -1 
    while arr[prev] < x :
        prev+=1
        if prev == min(step , size):
            return -1
    if arr[prev] == x :
        return prev
    return -1 

def interpolationSearch(arr , lo , hi , x) :
    
    if lo <= hi and x >= arr[lo] and x <= arr[hi] :
        pos = lo + int(((x - arr[lo]) * (hi - lo)) / (arr[hi] - arr[lo]))
        if arr[pos] == x :
            return pos
        if arr[pos] < x :
            return interpolationSearch(arr , pos +1 , hi , x)
        if arr[pos] > x :
            return interpolationSearch(arr , lo , pos - 1 , x)
    return -1            




