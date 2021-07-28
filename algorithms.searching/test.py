from searching import linearSearch , binarySearch , jumpSearch , interpolationSearch

arr = [1,2,3,4,5,6,7,8,9]


print(linearSearch(arr,3))

print(binarySearch(arr,0,len(arr) - 1,3))

print(jumpSearch(arr,3))

print(interpolationSearch(arr , 0 , len(arr) -1, 3))