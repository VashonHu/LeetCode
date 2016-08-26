class Solution(object):
    def intersect(self, nums1, nums2):
        dict1 = {}
        for x in nums1:
            if x not in dict1:
                dict1[x] = 1
            else:
                dict1[x] += 1

        dict2 = {}
        for x in nums2:
            if x not in dict2:
                dict2[x] = 1
            else:
                dict2[x] += 1

        result = []
        for x in dict1:
            if x in dict2:
                n = min(dict1[x], dict2[x])
                for i in range(n):
                  result.append(x)

        return result

class Solution2(object):
    def intersection(self, nums1, nums2):
        return set(nums1) & set(nums2)

if __name__ == "__main__":
    alist1 =  [1, 2, 2, 1]
    alist2 = [2, 2]
    h = Solution()
    print h.intersect(alist1, alist2)