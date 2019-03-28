from pprint import pprint

def seggregate_odd_even(arr):
    i = -1
    j = 0
    while j!=len(arr):
        if arr[j]%2==0:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
        j+=1



if __name__ == '__main__':
    arr = [12,34,45,9,8,90,3]
    seggregate_odd_even(arr)
    pprint(arr)