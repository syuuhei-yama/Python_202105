#順列の表示　
# from itertools import permutations
from typing import List

def all_perms(elemerts : List[int]) -> List[List[int]]:
    result = []
    if len(elemerts) <= 1:
        return [elemerts]

    for perm in all_perms(elemerts[1:]):
        for i in range(len(elemerts)):
            result.append(perm[:i] + elemerts[0:1] + perm[i:])

    return result

if __name__ == "__main__":
    for p in all_perms([1, 2, 3]):
        print(p)
