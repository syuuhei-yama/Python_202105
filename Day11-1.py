# from typing import List, Tuple, Optional
#
# def ger_pair(numbers:List[int], target: int) -> Optional[Tuple[int,int]]:
#     cache = set()
#     for num in numbers:
#         val = target - num
#         if val in cache:
#             return  val, num
#         cache.add(num)
#
# def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
#     sum_numbers = sum(numbers)
#     # if sum_numbers % 2 != 0:
#     #     return
#     # half_sum = int(sum_numbers / 2)
#     half_sum, remainder = divmod(sum_numbers, 2)
#     if remainder != 0:
#         return
#
#     cache = set()
#     for num in numbers:
#         cache.add(num)
#         val = half_sum - num
#         if val in cache:
#             return val, num
#
#
#
#
# if __name__ == "__main__":
#     l = [11, 2, 5, 9, 10, 3]
#     t = 12
#     print(ger_pair(l, t))
#
#     l = [11, 2, 5, 9, 10, 3]
#     print(get_pair_half_sum(l))


#Stack

from typing import Any

class Stack(object):

    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        self.stack.append(data)

    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop()

if __name__ == "__main__":
    stack = Stack()
    print(stack.stack)
    stack.push(1)
    print(stack.stack)
    stack.push(2)
    print(stack.stack)




