# Problem Description: https://codeforces.com/problemset/problem/71/A

n = int(input())

for i in range(n):
    word = input()
    print(word if len(word) <= 10 else ''.join(word[0] + '' + str((len(word) - 2)) + word[len(word) - 1]))
