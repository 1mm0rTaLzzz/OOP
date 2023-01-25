from math import ceil
from dataclasses import dataclass


@dataclass
class ActivStrs(object):
    strs: str
    activ: bool = True

    def deactivate(self):
        self.activ = False


h, w, n = map(int, input().split())
strs = [ActivStrs(input()) for _ in range(n)]

for index, item in enumerate(strs):
    if strs[index].activ:
        temp = []
        for i in range(index, len(strs)):
            if strs[i].activ:
                if len(' '.join(map(str, temp + [strs[i].strs]))) <= w:
                    temp.append(strs[i].strs)
                    continue
            break

        [strs[i].deactivate() for i in range(index, index + len(temp))]
        strs[index].strs, strs[index].activ = ' '.join(map(str, temp)), True

print(ceil(len([_ for _ in strs if _.activ]) / h))