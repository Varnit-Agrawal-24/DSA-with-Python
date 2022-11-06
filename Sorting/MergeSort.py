def merge(arr,l,m,h):
    n1=m-l+1
    n2=h-m
    L=arr[l:m+1]
    R=arr[m+1:h+1]
    i=j=0
    k=l
    while(i<n1 and j<n2):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while(i<n1):
        arr[k]=L[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=R[j]
        j+=1
        k+=1

def mergeSort(arr,l,h):
    if l<h:
        m=l+(h-l)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,h)
        merge(arr,l,m,h)

if __name__=="__main__":
    arr=[10,40,50,5,100,30,79,45]
    mergeSort(arr,0,len(arr)-1)
    print(arr)