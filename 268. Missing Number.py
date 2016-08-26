class Solution(object):
    @staticmethod
    def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0] + 1

        previous = nums[0]
        for x in nums:
            if (x - previous) == 2:
                return previous + 1
            previous = x

def missingNumber(nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)

if __name__ == "__main__":
    alist = [0, 1, 2, 4]
    n = len(alist)
    print n * (n + 1) / 2
    print  missingNumber(alist)

    [0, 1, 2, 3, 4]
