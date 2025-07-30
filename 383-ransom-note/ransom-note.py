class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = {}

        for c in magazine:
            magazine_counter[c] = 1 + magazine_counter.get(c,0)

        for c in ransomNote:
            if magazine_counter.get(c,0) > 0:
                magazine_counter[c] -= 1
            else:
                return False
        return True



        