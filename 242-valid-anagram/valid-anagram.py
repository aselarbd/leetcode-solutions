class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter, t_counter = {}, {}

        for c in s:
            s_counter[c] = s_counter.get(c, 0) + 1

        for c in t:
            t_counter[c] = t_counter.get(c, 0) + 1

        return s_counter == t_counter
        