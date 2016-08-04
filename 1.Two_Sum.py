class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        h = {}
        for i, num in enumerate(nums):
            if (target - num) in h:
                return [i, h[target - num]]
            h[num] = i #这条语句不能放在if之前，不然会引发错误

    @staticmethod
    def combinationSum4(nums, target):
        temp = nums[:]
        temp.sort()
        i = 0
        j = len(temp) - 1
        sum = 0
        while i < j:
            sum = temp[i] + temp[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                if temp[i] == temp[j]:
                    index = nums.index(temp[i])
                    index += 1
                    return(nums.index(temp[i]), nums[index:].index(temp[j]) + index)
                return (nums.index(temp[i]), nums.index(temp[j]))


    @staticmethod
    def twoSum2(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        for i in range(len(nums)):
            hashTable[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] in hashTable and i != hashTable[target - nums[i]]:
                return [i, hashTable[target - nums[i]]]#这里必须是i，而不能是hashTable[nums[i]]，那样的话当target为同一数值的元素相加而成的话，其结果是错的

        return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print  Solution.combinationSum4(nums, target)

    nums = [0, 2, 4, 0]
    target =  0
    print Solution.twoSum(nums, target)

    h = {}
    h['h'] = 8
    h['h'] = 10
    print h