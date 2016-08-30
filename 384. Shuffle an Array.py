class Solution(object):
    def __init__(self, nums):
        self.nums = nums
        self.origin = nums[:]

    def reset(self):
        return self.origin

    def shuffle(self):
        import random
        for x in range(len(self.nums)):
            randomIndex = random.randrange(0, len(self.nums))
            self.nums[x], self.nums[randomIndex] = self.nums[randomIndex], self.nums[x]
        return self.nums