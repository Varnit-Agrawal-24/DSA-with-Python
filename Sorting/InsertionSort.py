def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

if __name__=="__main__":
    arr=[10,40,50,5,100,30,79,45]
    insertionSort(arr)
    print(arr)