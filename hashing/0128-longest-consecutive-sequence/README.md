# 0128. Longest Consecutive Sequence

**Category:** Hashing / Arrays  
**Link:** https://leetcode.com/problems/longest-consecutive-sequence/

## Problem (brief)
Given an unsorted array `nums`, return the length of the longest sequence of consecutive integers (each element is `+1` from the previous). Elements do not have to be adjacent in the original array. Target time: **O(n)**.

## Approach
- Insert all numbers into a **hash set**.
- A value `x` is a **sequence start** iff `x - 1` is **not** in the set.
- For each start, increment while `x + 1` exists; track the longest run.

## Complexity
- Time: **O(n)** average
- Space: **O(n)**
