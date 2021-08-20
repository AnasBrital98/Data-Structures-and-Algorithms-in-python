# Sorting Algorithms

### Selection Sort :

```python
def selectionSort(arr):
    for i in range(len(arr) - 1):
        index = i 
        for j in range(i+1 , len(arr)):
            if arr[j] < arr[i]:
                index = j
        arr[i] , arr[index] = swap(arr[i], arr[index])
```

### Insertion Search :

```python
def insertionSort(arr):
    for i in range(1 , len(arr)):
        val = arr[i]
        j = i-1
        while j>=0 and arr[j] > val :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
```

### Bubble Sort :

```python
def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1]  = swap(arr[j], arr[j+1]) 
```

### Merge Sort :

```python
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        a = arr[:mid]
        b = arr[mid:]

        mergeSort(a)
        mergeSort(b)

        i = j = k = 0;

        while i < len(a) and j < len(b):
            if a[i] < b [j]:
                arr[k] = a[i]
                i+=1
                k+=1
            else :
                arr[k] = b[j]
                j+=1
                k+=1

        while i < len(a):
            arr[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            arr[k] = b[j]
            j += 1
            k += 1
```