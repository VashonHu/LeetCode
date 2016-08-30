class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for x in ransomNote:
            if x in magazine:
                magazine.remove(x)
            else:
                return False
        return True

if __name__ == "__main__":
    r = "aa"
    m = "ab"
    h = Solution()
    print h.canConstruct(r, m)