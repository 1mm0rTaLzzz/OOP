strips = int(input())
ways = list()

if strips in (1, 2):
    print('2')
else:
    ways.append(0)
    ways.append(2)
    ways.append(2)
    for i in range(3, 46):
        ways.append(ways[i - 1] + ways[i - 2])
        
    print(ways[strips])