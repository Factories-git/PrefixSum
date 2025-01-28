import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
sum_ = [0]
t = 0
for i in arr:
    t += i
    sum_.append(t)
for i in range(m):
    s,e = map(int , input().split())
    print(sum_[e] - sum_[s-1])