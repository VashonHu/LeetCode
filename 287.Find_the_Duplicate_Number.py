class Solution(object):
    def findDuplicate(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            count = 0
            # mid = low + (high - low) / 2
            mid = (low + high) / 2
            for x in nums:
                if x <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low