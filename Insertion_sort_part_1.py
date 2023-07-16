

def insertionSort1(n, arr):
    for i in range(1,len(arr)):
        key = arr[i]

        j = i-1

        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            print(" ".join(str(x) for x in arr))
            
        arr[j + 1] = key
        
    print(" ".join(str(x) for x in arr))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
