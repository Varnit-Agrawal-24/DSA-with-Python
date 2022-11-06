def partition(arr,l,h):
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    i+=1
    arr[i],arr[h]=arr[h],arr[i]
    return i

def quickSort(arr,l,h):
    if(l<h):
        pivot=partition(arr,l,h)
        quickSort(arr,l,pivot-1)
        quickSort(arr,pivot+1,h)

if __name__=="__main__":
    arr=[10,40,50,5,100,30,79,45]
    quickSort(arr,0,len(arr)-1)
    print(arr)