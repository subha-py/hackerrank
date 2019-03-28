def search(arr,item):
    def binary_search(arr,item,low,high):
        if low == high:
            return arr[low] == item
        mid = low+int((high-low)/2)
        if arr[mid] > item:
            return binary_search(arr,item,low,mid -1)
        elif arr[mid] < item:
            return binary_search(arr,item,mid +1 , high)
        else:
            return True
    if len(arr) == 0:
        return False
    else:
        return binary_search(arr,item,0,len(arr)-1)

if __name__ == '__main__':
    arr = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    found =search(arr,17)
    print(found)