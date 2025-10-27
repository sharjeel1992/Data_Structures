def maxArea(heights):
    """
    Two-pointer solution.
    Move the pointer at the shorter line inward each step; that is the only way
    to potentially find a taller line and increase area.
    Time: O(n), Space: O(1)
    """
    l, r = 0, len(heights) - 1
    best = 0

    while l < r:
        h = min(heights[l], heights[r])
        area = (r - l) * h
        if area > best:
            best = area

        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1

    return best


if __name__ == "__main__":
    height = [1,7,2,5,4,7,3,6]
    print(maxArea(height))  # Expected: 36 (between heights[1]=7 and heights[7]=6 → width=6, min=6 → 36)
