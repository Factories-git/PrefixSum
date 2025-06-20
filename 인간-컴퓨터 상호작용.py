import sys

input = sys.stdin.readline

k = input().strip()
n = int(input())
prefix = [[0] * (len(k) + 1) for _ in range(26)]

for i in range(1, len(k) + 1):
    ch = ord(k[i-1]) - ord('a')
    for j in range(26):
        prefix[j][i] = prefix[j][i-1]
    prefix[ch][i] += 1

for i in range(n):
    a, l, r = map(str, input().split())
    idx = ord(a) - ord('a')
    print(prefix[idx][int(r)+1] - prefix[idx][int(l)])