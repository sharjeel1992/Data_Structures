# 0011. Container With Most Water

**Category:** Two Pointers  
**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/container-with-most-water/

## Problem (brief)
Given an array `height` where each element is the height of a line on the x-axis,
choose two lines that, together with the x-axis, form a container holding the most water. Return the maximal area.

## Approach (Two Pointers)
- Start with `l = 0` and `r = n-1`.
- Area at each step is `(r - l) * min(height[l], height[r])`.
- Move the pointer at the **shorter line** inward; moving the taller one can’t increase area while width shrinks.

## Complexity
- **Time:** O(n)  
- **Space:** O(1)

## Example
height = [1,7,2,5,4,7,3,6] → 36
