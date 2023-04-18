def insertionsort(arr):
    for i in range(len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key
data=[5,2,4,3,98,23]
insertionsort(data)
print("sorted array ")
print(data)            