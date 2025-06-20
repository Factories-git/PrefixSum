import sys, copy

input = sys.stdin.readline

k = input().strip()
prefix = [{i : 0 for i in 'abcdefghijklmnopqrstuvwxyz'}]
for i in range(len(k)):
    string = copy.deepcopy(prefix[-1])
    string[k[i]] += 1
    prefix.append(string)
n = int(input())
for i in range(n):
    a, l, r = map(str, input().split())
    print(prefix[int(r)+1][a] - prefix[int(l)][a])