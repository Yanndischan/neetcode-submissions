class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text =""
        reversed_text =""
        for char in s:
            if char.isalnum():
                clean_text += char.lower()
        for char in clean_text:
            reversed_text= char + reversed_text
        
        if clean_text==reversed_text:
            return True
        return False
