def threeSum(nums):
    n = len(nums)
    if n < 3:
        return []

    nums.sort()
    res = []

    for i in range(n - 2):
        # skip duplicate anchors
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # since sorted, once nums[i] > 0, further sums can't be zero
        if nums[i] > 0:
            break

        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # skip duplicates on both sides
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
    return res


if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))   # [[-1,-1,2], [-1,0,1]]
    print(threeSum([-2,0,0,2,2]))       # [[-2,0,2]]
