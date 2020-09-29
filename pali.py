def is_palindrome(s):
    if len(s)<1:
        return True
    else:
        if s[0]==s[-1]:
            return is_palindrome(s[-1:1])
        else:
            return False

s=str(input("Input string: "))
if (is_palindrome(s)==True):
    print("Is palindrome")
else:
    print("It isn't a palindrome")
