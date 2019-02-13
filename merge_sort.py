import operator

def merge(right,left,compare):
    """
    :param right: right list
    :param left: left list
    :param compare: could be lt or gt depends on ascending or descending
    :return:
    """
    result = []
    i,j = 0,0
    while (i<len(left)) and (j<len(right)):
        if compare(left[i],right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    if i >= len(left):
        result += right[j:]
    else:
        result += left[i:]

    return result

def mergeSort(alist,compare = operator.lt):
    if len(alist) <= 1:
        return alist[:]
    else:
        mid = int(len(alist)/2)
        left = mergeSort(alist[:mid], compare)
        right = mergeSort(alist[mid:], compare)
        return merge(left,right,compare)

print(mergeSort([54,26,93,17,77,31,44,55,20]))

