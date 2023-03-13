class StringMethods:
    # https://leetcode.com/problems/longest-common-prefix/
    def longestCommonPrefix_14(self, strs) -> str:
        shortest = min(strs, key=len)
        if len(shortest) <= 0:
            return strs[0]
        ans = []
        pivot = ""
        for x in range(len(shortest)):
            pivot = strs[0][x]
            for y in range(len(strs)):
                #print(strs[y][x], "  piv:",pivot)
                if strs[y][x] != pivot:
                    return "".join(ans)
            ans.append(pivot)
        return "".join(ans)