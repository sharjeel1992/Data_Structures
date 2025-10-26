def longestConsecutive(nums):
    if not nums:
        return 0

    s = set(nums)
    best = 0

    for x in s:
        if x - 1 not in s:            # start of a sequence
            cur = x
            streak = 1
            while cur + 1 in s:
                cur += 1
                streak += 1
            best = max(best, streak)   # update the global best

    return best


if __name__ == "__main__":
    print(longestConsecutive([2,20,4,10,3,4,5]))          # 4
    print(longestConsecutive([0,3,2,5,4,6,1,1]))          # 7
    print(longestConsecutive([-4,-3,-2,-1,0,5,9,8,0,1]))  # 5
