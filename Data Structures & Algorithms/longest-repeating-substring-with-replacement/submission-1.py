class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq: dict[str, int] = {}
        res = 0
        max_freq = -1

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])

            window_length = r - l + 1

            if (window_length - max_freq) > k:
                freq[s[l]] -= 1
                l += 1
                continue

            res = max(res, window_length)
        return res