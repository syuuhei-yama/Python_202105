# def validate_format(chars: str) -> bool:
#     lookup = {'{': '}','{': '}','(': ')'}
#     stack = []
#     for char in chars:
#         if char in lookup.keys():
#             stack.append(lookup[char])
#         if char in lookup.values():
#             if not stack:
#                 return False
#
#             if char != stack.pop():
#                 return False
#
#
#     if stack:
#         return False
#
#     return True
#
# if __name__ == "__main__":
#     j = "{'key1':'value1','key2':[1,2,3], 'key3':(1,2,3)}"
#     print(validate_format(j))

#コーディングはアイデアが出るかどうか


#キュー
from collections import deque
from typing import Any

def reverse(queue):
    new_queue =deque()
    while queue:
        new_queue.append((q.pop()))
    return new_queue


# class Queue(object):
#
#     def __init__(self) -> None:
#         self.queue = []
#
#     def enqueue(self, data: Any) -> None:
#         self.queue.append(data)
#
#     def dequeue(self) -> Any:
#         if self.queue:
#             return self.queue.pop(0)

if __name__ == "__main__":
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    # q.reverse()
    # print(q)
    q = reverse(q)
    print(q)
    # print(q.pop())
    # print(q.pop())
    # print(q.pop())
    # print(q.pop())


