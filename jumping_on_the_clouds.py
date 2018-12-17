"""
Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus or

. She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered
if they are safe or if they must be avoided. For example, indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes and . She could follow the following two paths: or . The first path takes jumps while the second takes

.

Function Description

Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):

    c: an array of binary integers

Input Format

The first line contains an integer
, the total number of clouds. The second line contains space-separated binary integers describing clouds where

.

Output Format

Print the minimum number of jumps needed to win the game.
"""


def jumpingOnClouds(c):
    i = 0
    steps = 0
    while i < len(c)-1:
        if c[i + 1] == 0:
            i += 1
            steps += 1
            if (i < len(c) - 1) and c[i+1]==0:
                i+=1
        else:
            i += 2
            steps += 1
    return steps

if __name__ == '__main__':
    res = jumpingOnClouds([0,0,0,1,0,0])
    print(res)