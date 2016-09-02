class Solution(object):
    def longestConsecutive(self, nums):
        origin = nums[:]
        origin.sort()
        count = 1; i = 0; maxLen = 1

        while i + 1 < len(origin):
            sum = abs(origin[i] - origin[i + 1])
            if sum == 1:
                count += 1
            elif sum == 0:
                None
            else:
                if count > maxLen:
                    maxLen = count
                count = 1
            i += 1
        return maxLen if count < maxLen else count

if __name__ == "__main__":
    h = Solution()
    alist = [9,1,4,7,3,-1,0,5,8,-1,6]
    print h.longestConsecutive(alist)

