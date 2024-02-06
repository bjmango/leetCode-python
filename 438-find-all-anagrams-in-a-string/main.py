# 483  https://leetcode.com/problems/find-all-anagrams-in-a-string/
# https://www.youtube.com/watch?v=G8xtZy0fDKg

def findAnagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []

    pCount, sCount = {}, {}
    for i in range(len(p)):
        pCount[p[i]] = 1 + pCount.get(p[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)

    res = [0] if sCount == pCount else []

    l = 0  # left pointer
    for r in range(len(p), len(s)):
        sCount[s[r]] = 1 + sCount.get(s[r], 0)
        sCount[s[l]] -= 1

        if sCount[s[l]] == 0:
            sCount.pop(s[l])
        l += 1

        if sCount == pCount:
            res.append(l)
    print(res)
    return res

findAnagrams("cbaebabacd", "abc")
