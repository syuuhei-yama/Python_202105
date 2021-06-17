#リストを使った足し算
from typing import List

def remove_zero(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)

def list_in_int(numbers: List[int]) -> int:
    sum_numbers = 0
    for i, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10**i)
    return sum_numbers



def List_to_int_plus_one(numbers : List[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < 1:
        if numbers[i] != 10:
            remove_zero(numbers)

            break
        # 7, 8, 9 -> 7, 8, 10
        numbers[i] = 0
        numbers[i-1] += 1
        i -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    return numbers

if __name__ == "__main__":
    print(List_to_int_plus_one([1, 2, 3]))