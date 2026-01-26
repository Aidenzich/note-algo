## Leetcode 17. Letter Combinations of a Phone Number
![alt text](imgs/algorithm-17.drawio.png)

#### Solution
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        results = []
        
        def backtrack(index, curr):
            if index == len(digits):
                results.append(curr)
                return 

            bag = mapping[digits[index]]

            for letter in bag:
                backtrack(index + 1, curr + letter)


        backtrack(0, "")
        return results
```