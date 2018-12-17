def hourglassSum(arr):
    hourglass_sum = -9999999
    for row in range(4):
        for col in range(4):
            sum = arr[row][col] + arr[row][col + 1] + arr[row][col + 2] + arr[row + 1][col + 1] + arr[row + 2][col] + \
                  arr[row + 2][col + 1] + arr[row + 2][col + 2]
            if sum > hourglass_sum:
                hourglass_sum = sum
    return hourglass_sum


if __name__ == '__main__':
    array = [
        [1,1,1,0,0,0],
        [0,1,0,0,0,0],
        [1,1,1,0,0,0],
        [0,0,2,4,4,0],
        [0,0,0,2,0,0],
        [0,0,1,2,4,0]
    ]
    res = hourglassSum(array)
    print(res)