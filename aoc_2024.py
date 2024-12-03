from typing import List

DAY_ONE = 1
DAY_TWO = 2


def open_and_read_input(num_of_day: int) -> [List[int], List[int]]:
    with open(f'./input_files_aoc_2024/day_{num_of_day}_input', "r") as file:
        list1: List[int] = []
        list2: List[int] = []
        for line in file:
            [val_a, val_b] = line.split()
            list1.append(int(val_a))
            list2.append(int(val_b))
        file.close()
    return list1, list2


def calculate_list_difference():
    l1, l2 = open_and_read_input(DAY_ONE)
    l1.sort()
    l2.sort()
    sum = 0
    for elem_a, elem_b in zip(l1, l2):
        sum = sum + abs(elem_b - elem_a)
    print(sum)


def calculate_similarity_score():
    l1, l2 = open_and_read_input(DAY_ONE)
    l1.sort()
    l2.sort()
    similarity_score = 0
    for elem_l1 in l1:
        for elem_l2 in l2:
            if elem_l1 == elem_l2:
                similarity_score += elem_l1
    print(similarity_score)


def is_line_safe(line: str) -> int:
    num_list = [int(item) for item in line.split()]

    for slice in range(len(num_list)):
        prev_diff = 0
        error_count = 0
        next_list = num_list[:slice] + num_list[slice+1:]
        prev_item = next_list[0]
        for item in next_list[1:]:
            #print(f'slice: {slice} {num_list[:slice]} + {num_list[slice + 1:]}')
            #print(f'{next_list}')
            diff = item - prev_item
            #print(f'diff: {diff}, item: {item}, prev_item: {prev_item}')
            if (abs(diff) > 3 or abs(diff) < 1) or (prev_diff < 0 and diff > 0) or (prev_diff > 0 and diff < 0):
                #print(f'error')
                error_count += 1
            prev_item = item
            prev_diff = diff
        if error_count == 0:
            return 1
    return 0


def calculate_number_of_safe_reports():
    safe_reports = 0
    with open(f'./input_files_aoc_2024/test_day_2_input', "r") as file:
        for line in file:
            safe_reports += is_line_safe(line)
    print(safe_reports)


def main():
    calculate_list_difference()
    calculate_similarity_score()
    calculate_number_of_safe_reports()


if __name__ == "__main__":
    main()
