# 0167. Two Sum II – Input Array Is Sorted

**Category:** Two Pointers  
**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Problem (brief)
Given a **1-indexed**, non-decreasing array `numbers` and a `target`, return two indices `[i, j]` such that `numbers[i] + numbers[j] == target` with `i < j`. Exactly one solution exists.

## Approach (Two Pointers)
- Use two pointers: `l = 0` and `r = n-1`.
- If `numbers[l] + numbers[r] > target` → move `r--`.
- If `< target` → move `l++`.
- If equal → return `[l+1, r+1]` (1-based indices).

## Correctness
Array is sorted; moving the pointer on the side that makes the sum too large/small monotonically approaches the target.

## Complexity
- **Time:** O(n)
- **Space:** O(1)
