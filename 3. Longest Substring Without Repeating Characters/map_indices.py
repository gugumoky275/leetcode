class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_of_last_idx = {}
        start_pos, max_len = 0, 0
        for idx, char in enumerate(s):
            prev_pos = map_of_last_idx.get(char, -1) 
            if prev_pos >= start_pos:
                start_pos = prev_pos + 1
            map_of_last_idx[char] = idx

            dif = idx - start_pos + 1
            if dif > max_len:
                max_len = dif

        return max_len
