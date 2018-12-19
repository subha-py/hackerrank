"""
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if and  bribes , the queue will look like this: .

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

Function Description

Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.

minimumBribes has the following parameter(s):

q: an array of integers
Input Format

The first line contains an integer , the number of test cases.

Each of the next  pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has  space-separated integers describing the final state of the queue.

Constraints

Subtasks

For  score
For  score

Output Format

Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people.

Sample Input

2
5
2 1 5 3 4
5
2 5 1 3 4
Sample Output

3
Too chaotic
"""
import operator
from collections import defaultdict


def minimumBribes(alist):
    def mergeSort(q, compare=operator.lt, bribe_dict=None):
        def merge(left, right, compare, bribe_dict):

            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if compare(left[i], right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                    # bribe happened
                    # everyone remaining in left have bribed him
                    for turn in left[i:]:
                        bribe_dict[turn] += 1
                        if bribe_dict[turn] > 2:
                            return False

            if i < len(left):
                result += left[i:]
            else:
                result += right[j:]
            return result

        if len(q) <= 1:
            return q[:]
        else:
            mid = int(len(q) / 2)
            left = mergeSort(q[:mid], compare, bribe_dict)
            right = mergeSort(q[mid:], compare, bribe_dict)
            if left == False or right == False:
                return False
            return merge(left, right, compare, bribe_dict)


    bribe_dict = defaultdict(lambda: 0)
    res = mergeSort(alist, bribe_dict=bribe_dict)
    if res != False:
        print(sum(bribe_dict.values()))
    else:
        print('Too chaotic')

if __name__ == '__main__':
   alist = [2, 1, 5, 3, 4]
   minimumBribes(alist)