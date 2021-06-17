#連続合計値が多いものを導き出す
from typing import List

def get_max_min_sequence_sum(numbers : List[int], operator=max) -> int:
    result_sequence, sum_sequence = 0, 0
    for num in numbers:
        # temp_result_sequence = sum_sequence + num
        # if num < temp_result_sequence:
        #     sum_sequence = temp_result_sequence
        # else:
        #     sum_sequence = num
        sum_sequence = operator(num, sum_sequence + num)

        # if result_sequence < sum_sequence:
        #     result_sequence = sum_sequence
        result_sequence = operator(result_sequence, sum_sequence)

    return result_sequence


def find_max_circular_seqence_sum(numbers : List[int]) -> int:
    max_seqence_sum = get_max_min_sequence_sum(numbers)
    # invert_numbers = []
    # all_sum = 0
    # for num in numbers:
    #     all_sum += num
    #     invert_numbers.append(-num)
    #
    # max_wrap_sequence = all_sum - (-get_max_sequence_sum(invert_numbers))
    max_wrap_seqence = sum(numbers) -get_max_min_sequence_sum(numbers, operator=min)

    return (max_seqence_sum,max_seqence_sum)



if __name__ == "__main__":
    print(find_max_circular_seqence_sum([1, -2, 3, 6, -1, 2, 4, -5, 2]))

