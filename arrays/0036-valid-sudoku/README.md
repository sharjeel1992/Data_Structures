# 0036. Valid Sudoku

**Category:** Arrays / Matrix  
**Link:** https://leetcode.com/problems/valid-sudoku/

## Problem (brief)
Validate a partially filled 9×9 Sudoku board. Each row, column, and 3×3 box must have no duplicate digits '1'–'9'. '.' are blanks.

## Approach
- Track digits with three structures: rows[r], cols[c], boxes[(r/3)*3 + (c/3)] (sets or bit masks).
- For each digit cell, if it already exists in any of the three → invalid; else insert and continue.

## Complexity
- Time: O(81)
- Space: O(81) (or O(1) with bit masks)
