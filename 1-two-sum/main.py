def two_sum(arr: list[int], target: int) -> list[int]:
    hash_map = {}  # value, index
    for i, n in enumerate(arr):
        diff = target - n
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[n] = i
    return


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
