class Solution(object):
    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0:0}
        for line in input.splitlines():
            name = line.strip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1#depth + 1 是因为要利用这一行就把递加的路径长度算出来，
                # 于是就要利用之前的值， 要利用当pathlen[0]的时候，所以depth 要加1，
                #等号后面的加一是因为要加上分隔文件夹名之间的斜线
        return maxlen

if __name__ == "__main__":
    h = Solution()
    s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print h.lengthLongestPath('')