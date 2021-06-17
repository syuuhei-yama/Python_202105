#スネーク表示
from typing import List

def snake_string_v1(chears :str) -> List[List[str]]:
    result = [[],[],[]]
    result_indexs = {0, 1, 2}
    insert_index = 1
    for i, s in enumerate(chears):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)
        for rest_index in result_indexs - {insert_index}:
            result[rest_index].append(' ')
    return result

def snake_string_v2(chears :str, depth: int) -> List[List[str]]:
    result = [[] for _ in  range(depth)]
    result_indexs = {i for i in range(depth)}
    insert_index = int(depth / 2)

    def pos(i):
        return i + 1
    def neg(i):
        return i - 1

    op = neg

    for s in chears:
        result[insert_index].append(s)
        for rest_indexs in result_indexs - {insert_index}:
            result[rest_indexs].append(' ')
        if insert_index <= 0:
            op = pos
        if insert_index >= depth -1:
            op = neg
        insert_index = op(insert_index)

    return result




if __name__ == "__main__":
    # numbers = [str(i) for j in range(5) for i in range(10)]
    # string = ''.join(numbers)
    # for line in snake_string_v1(string):
    #     print(''.join(line))

    import string
    alphabet = [s for _ in range(2) for s in string.ascii_lowercase]
    strings = ''.join(alphabet)
    for line in snake_string_v2(strings, 10):
        print(''.join(line))

