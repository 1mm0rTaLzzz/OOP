n, a, b = map(int, input().split())

a_, b_ = (n + 1) * [0], (n + 1) * [0]
a_[0], b_[0], a_[1], b_[1] = 1, 1, 1, 1
m = 1e9 + 7

for i in range(2, n + 1):
    if i - a > 0:
        a_[i] = int((sum(b_[i - 1:i - a:-1]) + b_[i - a]) % m)
    else:
        a_[i] = int(sum(b_[i - 1:0:-1]) + b_[0] % m)
        
    if i - b > 0:
        b_[i] = int((sum(a_[i - 1:i - b:-1]) + a_[(i - b)]) % m)
    else:
        b_[i] = int((sum(a_[i - 1:0:-1]) + a_[0]) % m)
        
print(int((a_[n] + b_[n]) % m))