class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        target_mp = {}
        s_mp = {}
        for ch in t:
            target_mp[ch] = target_mp.get(ch, 0) + 1

        matches = 0
        valid_matches = len(target_mp)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            s_mp[c] = s_mp.get(c, 0) + 1
            if s_mp[c] == target_mp.get(c, 0):
                matches += 1

            while matches == valid_matches:
                if r - l + 1 < res_len:
                    res, res_len = [l, r], r - l + 1
                c = s[l]
                s_mp[c] -= 1
                if s_mp[c] < target_mp.get(c, 0):
                    matches -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""