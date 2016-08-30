class Solution(object):
    def reverseVowels(self, s):
        vowels = "AEIOUaeiou"
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)
if __name__ == "__main__":
    s = "hello"
    ''.join(list(s).reverse())
    h = Solution()
    print h.reverseVowels(s)