class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        best_sub = ("", float('inf'))

        target_mp = {}
        s_mp = {}

        for i in range(len(t)):
            target_mp[t[i]] = target_mp.get(t[i], 0) + 1

        matches = 0
        l = 0
        valid_matches = len(target_mp.keys())

        for r in range(len(s)):
            c = s[r]
            s_mp[c] = s_mp.get(c, 0) + 1
            if s_mp[c] == target_mp.get(c, 0):
                matches += 1

            while matches == valid_matches:
                if r - l + 1 < best_sub[1]:
                    best_sub = (s[l:r+1], r -l + 1)
                c = s[l]
                s_mp[c] -= 1
                l += 1
                if s_mp[s[l - 1]] < target_mp.get(s[l - 1], 0):
                    matches -= 1

        return best_sub[0]


            

                