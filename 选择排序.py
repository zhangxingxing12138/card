def zxx_min(arr):
    default_min = arr[0]
    default_index = 0
    for i in range(1,len(arr)):
        if arr[i] < default_min:
            default_min = arr[i]
            default_index = i
    return default_index
def selectionSort(arr):
    newarr = []
    for i in range(len(arr)):
        print(arr)
        small_index = zxx_min(arr)

        newarr.append(arr.pop(small_index))

    return newarr
arr = [5,3,6,2,10,67,45,98,45,33]
newarr = selectionSort(arr)

print(newarr)
