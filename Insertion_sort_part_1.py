def insertionSort1( arr):
    for i in range(1,len(arr)):
        key = arr[i]

        j = i-1

        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            print(" ".join(str(x) for x in arr))
            
        arr[j + 1] = key
        
    print(" ".join(str(x) for x in arr))

arr = [2, 4 ,6, 8 ,3]
insertionSort1(arr)


# 2 4 6 8 8 
# 2 4 6 6 8 
# 2 4 4 6 8 
# 2 3 4 6 8 