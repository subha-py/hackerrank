"""
Lilah has a string,

, of lowercase English letters that she repeated infinitely many times.

Given an integer,
, find and print the number of letter a's in the first

letters of Lilah's infinite string.

For example, if the string
and , the substring we consider is , the first characters of her infinite string. There are

occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length

in the infinitely repeating string.

repeatedString has the following parameter(s):

    s: a string to repeat
    n: the number of characters to consider

Input Format

The first line contains a single string,
.
The second line contains an integer,

.

Constraints

For of the test cases,

    .

Output Format

Print a single integer denoting the number of letter a's in the first
letters of the infinite string created by repeating infinitely many times.
"""



def repeatedString(s, n, char='a'):
    def number_of_letters_from_string(astring,char):

        number = 0
        for turn in astring:
            if turn==char:
                number+=1
        return number
    number_of_a = number_of_letters_from_string(s,char)
    q = int(n/len(s))
    number_of_a *= q
    rem = n % len(s)
    if rem != 0:
        number_of_a += number_of_letters_from_string(s[:rem],char=char)
    return number_of_a

if __name__ == '__main__':
    res = repeatedString('bab',725261545450)
    print(res)
