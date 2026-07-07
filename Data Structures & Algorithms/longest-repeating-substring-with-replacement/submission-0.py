class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq: dict[str, int] = {}
        res = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            max_char = max(freq, key = lambda x: freq[x])
            max_freq = freq[max_char]

            window_length = r - l + 1

            if (window_length - max_freq) > k:
                freq[s[l]] -= 1
                l += 1
                continue

            res = max(res, window_length)
        return res