n, k = map(int, input().split())
sequence = list(map(int, input().split()))
re = -float('inf')
prefixsum = [0]
t = 0
for i in sequence:
    t += i
    prefixsum.append(t)

print(prefixsum)
for i in range(k, n+1):
    re = max(re, prefixsum[i] - prefixsum[i - k])

print(re)