class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
if __name__ == '__main__':
    h = Solution()
    print h.containsNearbyDuplicate([1, 0, 1, 1], 1)