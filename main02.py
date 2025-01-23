def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n- i - 1):
             if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr= [4, 87, 90 ,21 , 34 , 2]
arr2 = buble_sort(arr)
print(arr2)
