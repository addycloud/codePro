#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, hashmap = 0, {}
        start = 0
        longest_substring = ""
        for end in range(len(s)):
            hashmap[s[end]] = hashmap.get(s[end], 0)+1
            if len(hashmap) == end - start + 1:
                if end - start + 1 > max_len:
                    max_len = end - start + 1
                    longest_substring = s[start:end + 1]
            while end - start + 1 > len(hashmap):
                head = s[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                start += 1
        return max_len, longest_substring

if __name__ == '__main__':
    s_str = 'asfgdjisaofjdisajfijdijeriuqtoprtiuijka;jgz./fdlsaj'
    print(Solution().lengthOfLongestSubstring(s_str))