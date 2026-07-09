class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        # build both counts for the first window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # how many of the 26 positions currently agree
        matches = sum(1 for i in range(26) if s1_count[i] == s2_count[i])

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # --- add the incoming char s2[r] ---
            i = ord(s2[r]) - ord('a')
            s2_count[i] += 1
            if s1_count[i] == s2_count[i]:      # just became equal
                matches += 1
            elif s1_count[i] + 1 == s2_count[i]:  # was equal, just broke it
                matches -= 1

            # --- remove the outgoing char s2[l] ---
            i = ord(s2[l]) - ord('a')
            s2_count[i] -= 1
            if s1_count[i] == s2_count[i]:      # just became equal
                matches += 1
            elif s1_count[i] - 1 == s2_count[i]:  # was equal, just broke it
                matches -= 1
            l += 1

        return matches == 26