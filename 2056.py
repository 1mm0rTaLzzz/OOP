k = int(input())
mrks = list(map(int, [input() for i in range(k)])
if 3 in mrks:
    print('None')
elif sum(mrks)/k == 5:
    print('Named')
elif sum(mrks)/k >= 4.5:
    print('High')
else:
    print('Common')
