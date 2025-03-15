class ReverseVowels:
    def reverse_vowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        results = []
        return_result = []
        for letter in s:
            normalized_letter = letter.lower()
            if normalized_letter in vowels:
                results.append(letter)
        
        results.reverse()
        idx = 0
        for letter in s:
            normalized_letter = letter.lower()
            if normalized_letter not in vowels:
                return_result.append(letter)
            else:
                return_result.append(results[idx])
                idx += 1

        return "".join(return_result)