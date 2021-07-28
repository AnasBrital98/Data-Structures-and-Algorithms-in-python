from sorting import selectionSort , bubbleSort , insertionSort , mergeSort 

arr = [9,8,7,6,5,4,3,2,1]

def display(arr):
    for i in range(len(arr)):
        print(arr[i],end='\t')
    print("\n")


print("Before Sorting The List : ")
display(arr)
print("After Sorting The List : ")
#selectionSort(arr)
#bubbleSort(arr)
#insertionSort(arr)
mergeSort(arr)
display(arr)
