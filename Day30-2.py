#指定されたIndex通りにリストの並ひ替え
from typing import List

def order_change_by_v1(chars:[str], indexs :List[int]) -> str:
    tmp = [None] * len(chars)
    for i, indexs in enumerate(indexs):
        tmp[indexs] = chars[i]
    return ' '.join(tmp)


def order_change_by_v2(chars:[str], indexs :List[int]) -> str:
    i, len_indexs = 0, len(indexs) -1
    while i < len_indexs:
        while i != indexs[i]:
            index = indexs[i]
            chars[index],chars[i] = chars[i], chars[index]
            indexs[index],indexs[i] = indexs[i],indexs[index]
        i += 1
    return ''.join(chars)



if __name__ == "__main__":
    w = ['h','y','n','p','t','o']
    i = [3, 1, 5, 0, 2, 4]
    print(order_change_by_v2(w, i))
