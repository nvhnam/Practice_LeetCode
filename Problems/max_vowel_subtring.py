class MaxVowelInSubString:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = ['a', 'e', 'i', 'o','u']
        left = 0
        new_count = 0
        for right in range(len(s)):
            if s[right] in vowels:
                new_count += 1
            if right - left == k - 1:
                count = max(count, new_count)
                if s[left] in vowels:
                    new_count -= 1
                left += 1
        return count