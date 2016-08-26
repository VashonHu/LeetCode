class Solution(object):
    @staticmethod
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        length = len(nums)
        while count < length:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
            else:
                i += 1
            count += 1


class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last0 = 0
        for i in range(0,len(nums)):
            if (nums[i]!=0):
                nums[i],nums[last0] = nums[last0],nums[i]
                last0+=1


if __name__ == "__main__":
    alist = [0,1,0,3,12]
    Solution.moveZeroes(alist)
    print alist