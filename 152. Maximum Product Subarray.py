class Solution(object):
    def maxProduct(self, nums):
        thisProd = 1; maxProd = 0
        if len(nums) == 1:
            return nums[0]

        for x in nums:
            thisProd *= x
            if thisProd < 0:
                thisProd = 1
            if thisProd > maxProd:
                maxProd = thisProd
        return maxProd

if __name__ == "__main__":
    h = Solution()
    alist = [2,3,-2,4]
    print h.maxProduct(alist)