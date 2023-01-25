s = int(input())
if s >= 1 and s <= 4:
    print('few')
if s >= 5 and s <= 9:
    print('several')
if s >= 10 and s <= 19:
    print('pack')
if s >= 20 and s <= 49:
    print('lots')
if s >= 50 and s <= 99:
    print('horde')
if s >= 100 and s <= 249:
    print('throng')
if s >= 250 and s <= 499:
    print('swarm')
if s >= 500 and s <= 999:
    print('zounds')
if s >= 1000:
    print('legion')