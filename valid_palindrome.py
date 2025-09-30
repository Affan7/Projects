def isPalindrome(s):
        s.lower()
        s.strip()
        if s == s[::-1]:
            print("palindrome")
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))