class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_pos, max_len = 0, 0
        char_to_index = {}
        for idx, char in enumerate(s):
            if char in char_to_index:
                old_start_pos = start_pos
                start_pos = char_to_index[char] + 1
                for remove_idx in range(old_start_pos, char_to_index[char] + 1):
                    del char_to_index[s[remove_idx]]

            char_to_index[char] = idx
            if idx - start_pos + 1 > max_len:
                max_len = idx - start_pos + 1

        return max_len
