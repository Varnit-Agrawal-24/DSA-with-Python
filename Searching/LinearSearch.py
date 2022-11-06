def linearSearch(arr,key):
    for i in arr:
        if key==i:
            return True
    return False

if __name__=="__main__":
    arr=[10,40,50,5,100,30,79,45]
    key=29
    print(linearSearch(arr,key))