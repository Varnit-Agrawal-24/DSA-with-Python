def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


if __name__=="__main__":
    arr=[10,40,50,5,100,30,79,45]
    bubbleSort(arr)
    print(arr)