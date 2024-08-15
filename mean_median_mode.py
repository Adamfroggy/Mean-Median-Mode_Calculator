"""
This folder contains my algo make up for
"mean","mode", "median"
"""

# defined function for mean


def mean(list_of_nums):
    total = 0
    for num in list_of_nums:
        total = total + num
    return total / len(list_of_nums)


# defined function for mode


def mode(list_of_nums):
    max_count = (0, 0)
    for num in list_of_nums:
        occurances = list_of_nums.count(num)
        if occurances > max_count[0]:
            max_count = (occurances, num)
    return max_count[1]

# defined function for median


def median(list_of_nums):
    list_of_nums.sort()
    if len(list_of_nums) % 2 != 0:
        middle_index = int((len(list_of_nums) - 1) / 2)
        return list_of_nums[middle_index]
    elif len(list_of_nums) % 2 == 0:
        middle_index_1 = int(len(list_of_nums) / 2)
        middle_index_2 = int(len(list_of_nums) / 2) - 1
        return mean([list_of_nums[middle_index_1],
                     list_of_nums[middle_index_2]])


print(mean([13, 13, 13, 13, 14, 14, 16, 18]))
print(mode([13, 13, 13, 13, 14, 14, 16, 18]))
print(median([13, 13, 13, 13, 14, 14, 16, 18]))
