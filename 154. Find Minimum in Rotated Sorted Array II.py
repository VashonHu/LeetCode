from sys import maxsize
class Solution(object):
    def findMin(self, nums):
        before = -maxsize
        for x in nums:
            if x < before:
                return x
            before = x
        return nums[0]# if len(nums) > 0 else None

class Solution3(object):
    def findMin(self, nums):
        return min(nums)

class Solution2(object):#it is valid , as the nums's besed on increasing order
    def findMin(self, nums):
        start = 0; end = len(nums) - 1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start + end) / 2
            if nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid
        return nums[start]

if __name__ == "__main__":
    h = Solution2()
    print h.findMin([3, 1])