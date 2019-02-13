"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other
string. Given a string, find the number of pairs of substrings of the string which are anagrams of each
other.
For example , the list of all anagrammatic pairs is at positions
respectively.
Function Description
Complete the function sherlockAndAnagrams in the editor below. It must return an integer representing
the number of anagrammatic pairs of substrings in .
sherlockAndAnagrams has the following parameter(s):
s: a string .
Input Format
The first line contains an integer , the number of queries.
Each of the next lines contains a string to analyze.
Constraints
String contains only lowercase letters ascii[a-z].
Output Format
For each query, return the number of unordered anagrammatic pairs.
Sample Input 0
2
abba
abcd
Sample Output 0
4
0
Explanation 0
The list of all anagrammatic pairs is and at positions
and respectively.
No anagrammatic pairs exist in the second query as no character repeats.
Sample Input 1
2
ifailuhkqq
kkkk
Sample Output 1
3
10
Explanation 1
For the first query, we have anagram pairs and at positions and
respectively.
For the second query:
There are 6 anagrams of the form at positions and
.
There are 3 anagrams of the form at positions and .
There is 1 anagram of the form at position .
Sample Input 2
1
cdcd
Sample Output 2
5
Explanation 2
There are two anagrammatic pairs of length : and .
There are three anagrammatic pairs of length : at positions
respectively
"""


def sherlockAndAnagrams(s):
    def is_anagram(string_1, string_2):
        def build_string_dict(string):
            adict = dict()
            for char in string:
                if char in adict.keys():
                    adict[char] += 1
                else:
                    adict[char] = 1
            return adict.copy()

        if len(string_1)!=len(string_2):
            return False
        string_1_dict = build_string_dict(string_1)
        string_2_dict = build_string_dict(string_2)
        for key in string_1_dict:
            if string_2_dict.get(key) is None:
                return False
            if string_2_dict.get(key) != string_1_dict.get(key):
                return False
        return True
    i, j = 0, 1
    result_dict = {}
    count = 0
    while i < len(s):
        while j <= len(s):
            substring = s[i:j]
            if len(substring) in result_dict.keys():
                collection = result_dict[len(substring)]
                for match in collection:
                    if is_anagram(substring,match):
                        count += 1
                collection.append(substring)
            else:
                result_dict[len(substring)] = []
                result_dict[len(substring)].append(substring)

            j += 1
        i += 1
        j = i + 1
        
    return count


if __name__ == '__main__':
    res = sherlockAndAnagrams('bcbabbaccacbacaacbbaccbcbccbaaaabbbcaccaacaccbabcbabccacbaabbaaaabbbcbbbbbaababacacbcaabbcbcbcabbaba')
    print(res)
