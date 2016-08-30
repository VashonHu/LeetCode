class Solution(object):
    def minSubArrayLen(self, s, nums):
        import sys
        i = 0; start = 0; minLen = sys.maxsize; sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            while (sum >= s):
                minLen = min(minLen, i - start + 1)
                sum -= nums[start]
                start += 1
        return 0 if minLen == sys.maxsize else minLen

if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    h = Solution()
    print h.minSubArrayLen(s, nums)

