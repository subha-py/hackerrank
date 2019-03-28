import operator

def mergeSort(arr,compare = operator.lt):

    def merge(left,right,compare):
        result = []
        i,j = 0,0
        while i < len(left) and j < len(right):
            if compare(left[i],right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        if i < len(left):
            result += left[i:]
        else:
            result += right[j:]
        return result

    if len(arr) <=1:
        return arr
    mid = int(len(arr)/2)
    left = mergeSort(arr[:mid],compare)
    right = mergeSort(arr[mid:],compare)
    return merge(left,right,compare)

print(mergeSort([54,26,93,17,77,31,44,55,20]))

