# Day 1 — LeetCode Easy Set (Questions 1–5) 02/02/2026 13:08

This document contains the problem statements for the Day 1 Python scripts:

- `001_two_sum.py`
- `002_best_time_buy_sell_stock.py`
- `003_valid_parentheses.py`
- `004_climbing_stairs.py`
- `005_merge_two_sorted_lists.py`

---

## Table of Contents
1. [1. Two Sum](#1-two-sum)
2. [121. Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock)
3. [20. Valid Parentheses](#20-valid-parentheses)
4. [70. Climbing Stairs](#70-climbing-stairs)
5. [21. Merge Two Sorted Lists](#21-merge-two-sorted-lists)

---

## 1. Two Sum

**Difficulty:** Easy  
**Topics:** Array, Hash Table  

### Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Examples

**Example 1**  
Input: `nums = [2,7,11,15], target = 9`  
Output: `[0,1]`  
Explanation: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

**Example 2**  
Input: `nums = [3,2,4], target = 6`  
Output: `[1,2]`

**Example 3**  
Input: `nums = [3,3], target = 6`  
Output: `[0,1]`

### Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

---

# Notes for Problem Above

![Freehand Drawing.svg](/day1/_resources/Freehand%20Drawing-20.svg)

## 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy  
**Topics:** Array, Dynamic Programming  

### Problem
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### Examples

**Example 1**  
Input: `prices = [7,1,5,3,6,4]`  
Output: `5`  
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = `6 - 1 = 5`.  
Note: Buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2**  
Input: `prices = [7,6,4,3,1]`  
Output: `0`  
Explanation: In this case, no transactions are done and the max profit = 0.

### Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## 20. Valid Parentheses

**Difficulty:** Easy  
**Topics:** String, Stack  

### Problem
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Examples

**Example 1**  
Input: `s = "()"`  
Output: `true`

**Example 2**  
Input: `s = "()[]{}"`  
Output: `true`

**Example 3**  
Input: `s = "(]"`  
Output: `false`

**Example 4**  
Input: `s = "([])"`  
Output: `true`

**Example 5**  
Input: `s = "([)]"`  
Output: `false`

### Constraints
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`

---

## 70. Climbing Stairs

**Difficulty:** Easy  
**Topics:** Math, Dynamic Programming, Memoization  

### Problem
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

### Examples

**Example 1**  
Input: `n = 2`  
Output: `2`  
Explanation: There are two ways to climb to the top:
1. `1 step + 1 step`
2. `2 steps`

**Example 2**  
Input: `n = 3`  
Output: `3`  
Explanation: There are three ways to climb to the top:
1. `1 step + 1 step + 1 step`
2. `1 step + 2 steps`
3. `2 steps + 1 step`

### Constraints
- `1 <= n <= 45`

---

## 21. Merge Two Sorted Lists

**Difficulty:** Easy  
**Topics:** Linked List, Recursion  

### Problem
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Examples

**Example 1**  
Input: `list1 = [1,2,4], list2 = [1,3,4]`  
Output: `[1,1,2,3,4,4]`

**Example 2**  
Input: `list1 = [], list2 = []`  
Output: `[]`

**Example 3**  
Input: `list1 = [], list2 = [0]`  
Output: `[0]`

