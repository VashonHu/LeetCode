class Solution(object):
    def findPeakElement(self, nums):
        low = 0; high = len(nums) - 1

        while (low < high):
            mid1 = (low + high) / 2
            mid2 = mid1 + 1
            if (nums[mid1] < nums[mid2]):
                low = mid2
            else:
                high = mid1

        return low


# class Solution(object):
#     def findPeakElement(self, nums):
#         import random
#         listLen = len(nums)
#         if listLen == 2:
#             return 0 if nums[0] > nums[1] else 1
#         elif listLen <= 1:
#             return 0
#
#         result =[]
#         i = 0
#         while i + 1 <= listLen - 1:
#             if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
#                 result.append(i)
#             i += 1
#
#         if result:
#             return random.choice(result)

if __name__ == "__main__":
    h = Solution()
    n = [1,2,3,1, 8, 2]
    print h.findPeakElement(n)