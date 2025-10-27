def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        curr_sum = numbers[l] + numbers[r]
        if curr_sum == target:
            # 1-based indices
            return [l + 1, r + 1]
        if curr_sum > target:
            r -= 1
        else:
            l += 1

    # Problem guarantees a solution; return [] for completeness
    return []


if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 10, 11]
    target = 9
    print(twoSum(numbers, target))  # [2, 4]
