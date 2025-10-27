# 0015. 3Sum

**Category:** Two Pointers  
**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/3sum/

## Problem (brief)
Given an integer array `nums`, return all unique triplets `[a, b, c]` such that `a + b + c = 0`. Triplets must be unique, and order inside `nums` doesn’t matter.

## Approach (Sort + Two Pointers)
1. Sort `nums`.
2. For each index `i`, treat `nums[i]` as the anchor and run a two-pointer scan on `(i+1 .. n-1)`:
   - If sum `< 0` → move `l++`
   - If sum `> 0` → move `r--`
   - If sum `== 0` → record triplet, then skip duplicates on both sides.
3. Skip duplicate anchors (`nums[i] == nums[i-1]`) and early-break when `nums[i] > 0`.

## Complexity
- **Time:** O(n²)  
- **Space:** O(1) extra (ignoring output)

## Edge Cases
- Fewer than 3 elements → `[]`
- Many duplicates → ensure skipping duplicates at `i`, `l`, and `r`
- All positive or all negative → early exit after sort
