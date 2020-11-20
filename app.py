from typing import List


def swap(array: List[int], first_index: int, second_index: int):
    array[first_index], array[second_index] = array[second_index], array[first_index]


def swap_if_not_ordered(array: List[int], first_index: int, second_index: int, ascending: bool):
    if array[first_index] < array[second_index] and not ascending:
        swap(array, first_index, second_index)
    elif array[first_index] > array[second_index] and ascending:
        # 'elif' can be replaced with 'or' in previous 'if' statement. Which way is better?
        swap(array, first_index, second_index)


def sort_by_zigzag(input_list: List[int]) -> List[int]:
    ascending_order = True
    for index in range(len(input_list) - 1):
        swap_if_not_ordered(input_list, index, index + 1, ascending_order)
        ascending_order = not ascending_order
    return input_list


if __name__ == '__main__':
    input_numbers = [1, 5, -9, 12, 500, -50, -49, 11]
    result_zigzag = sort_by_zigzag(input_numbers)
    print(result_zigzag)
