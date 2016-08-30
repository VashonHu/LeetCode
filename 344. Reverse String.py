class Solution(object):
    def reverseString(self, s):
        s = list(s)
        s.reverse()
        return ''.join(s)
if __name__ == "__main__":
    h = Solution()
    s = "hello"
    print h.reverseString(s)

