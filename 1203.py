k = int(input())
time = []
out, end = 0, 0

for _ in range(k):
    time.append(list(map(int, input().split())))
    
time.sort(key=lambda x: x[1])

for conf in time:
    if end < conf[0]:
        end = conf[1]
        out += 1
        
print(out)