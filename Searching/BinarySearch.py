def binarySearch(arr,key):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid= low + (high-low)//2
        if arr[mid]==key:
            return True
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return False

if __name__=="__main__":
    arr=[10,40,50,5,100,30,79,45]
    arr.sort()
    key=100
    print(binarySearch(arr,key))