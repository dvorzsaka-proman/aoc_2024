from typing import List


def open_and_read_input() -> [List[int], List[int]]:
    with open("./input_files_aoc_2024/day_1_input", "r") as file:
        list1: List[int] = []
        list2: List[int] = []
        for line in file:
            [val_a, val_b] = line.split()
            list1.append(int(val_a))
            list2.append(int(val_b))
        file.close()
    return list1, list2


def calculate_list_difference():
    l1, l2 = open_and_read_input()
    l1.sort()
    l2.sort()
    sum = 0
    for elem_a, elem_b in zip(l1, l2):
        sum = sum + abs(elem_b - elem_a)
    print(sum)


def calculate_similarity_score():
    l1, l2 = open_and_read_input()
    l1.sort()
    l2.sort()
    similarity_score = 0
    for elem_l1 in l1:
        for elem_l2 in l2:
            if elem_l1 == elem_l2:
                similarity_score += elem_l1
    print(similarity_score)

def main():
    calculate_list_difference()
    calculate_similarity_score()


if __name__ == "__main__":
    main()
