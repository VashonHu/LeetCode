class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for i, j in enumerate(nums):
            if j in d :
                return True
            d[j] = i
        return False