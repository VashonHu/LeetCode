class Solution(object):
    def summaryRanges(self, nums):
        res = []
        if nums is None:
            res.append(str(nums))
            return res
        elif len(nums) < 2:
            return res.append(str(nums))

        begin = end = nums[0]
        for x in range(1, len(nums)):
            if nums[x] - end != 1:
                if begin == end:
                    res.append(str(end))
                else:
                    string = str(begin) + "->" + str(end)
                    res.append(string)
                begin = end = nums[x]
            else:
                end = nums[x]

        if begin == end:
            res.append(str(end))
        else:
            string = str(begin) + "->" + str(end)
            res.append(string)

        return res

if __name__ == "__main__":
    # alist = [0, 1, 2, 4, 5, 7]
    alist = []
    hu = Solution()
    print hu.summaryRanges(alist)

    print []
