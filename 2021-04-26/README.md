### 题目描述：
- 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
- ##### 示例 1：
   输入：nums = [2,7,11,15], target = 9
   输出：[0,1]
   解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
- ##### 示例 2：
  输入：nums = [3,2,4], target = 6
  输出：[1,2]
  
### 解题方法：
- 方法一：暴力枚举
   思路及算法：最容易想到的方法是枚举数组中的每一个数N ，寻找数组中是否存在 target。当我们使用遍历整个数组的方式寻找 target时，需要注意到每一个位于N之前的元素都已经和 N 匹配过，因此不需要再进行匹配。而每一个元素不能被使用两次，所以我们只需要在 N 后面的元素中寻找 target.
- 方法二：哈希表




### Title Description
- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
- ##### Example 1:
   Input: nums = [2,7,11,15], target = 9
   Output: [0,1]
   Output: Because nums[0] + nums[1] == 9, we return [0, 1].
- ##### Example 2:
   Input: nums = [3,2,4], target = 6
   Output: [1,2]

