class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, len(nums)):
            res.append(res[i - 1] * nums[i - 1])
        right = 1
        #先用阶乘的方法，求出一个数列，再反着求一边，这一遍补上第一次乘时其所缺乏的
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

if __name__ == "__main__":
    alist = [1, 2, 3, 4]
    hu = Solution()
    print hu.productExceptSelf(alist)