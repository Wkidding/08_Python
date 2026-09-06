# [题目编号] - [题目名称]

## 1. 题目链接
- [LeetCode 原题地址](https://leetcode.cn/problems/two-sum/)
- **难度**：🟢 Easy / 🟠 Medium / 🔴 Hard
- **标签**：`Array` `Hash Table`（可多选）

---

## 2. 题目类别
- **数据结构**：`数组` / `链表` / `树` / `图` / `哈希表` / `栈` / `堆`
- **算法思想**：`双指针` / `二分查找` / `滑动窗口` / `回溯` / `动态规划` / `贪心` / `BFS` / `DFS`
- **核心考点**：`前缀和` / `单调栈` / `并查集`（细化考点）

---

## 3. 解题思路
> **暴力解**（如果不考虑复杂度）：
> （简述最直观的想法）

> **最优解**（面试/竞赛要求）：
1. **核心思想**：例如“利用哈希表空间换时间，将查找从 O(n) 降为 O(1)”。
2. **具体步骤**：
   - Step 1: 初始化哈希表。
   - Step 2: 遍历数组，计算补数。
   - Step 3: 若补数在哈希表中，返回下标；否则将当前数存入哈希表。
3. **边界条件**：注意数组为空、无解、重复数字的处理。
4. **复杂度分析**：
   - 时间复杂度：O(n)
   - 空间复杂度：O(n)

---

## 4. 解题代码
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 代码实现
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []