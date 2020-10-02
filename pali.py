# THIS IS A PALINDROME FUNCTION
def is_palindrome(s):
    if len(s)<=1:
        return True
    else:
        if s[0]!=s[len(s)-1]:
            return False
        else:
                return is_palindrome((s[1:len(s)-1]))
s=str(input("Enter a word: "))
if(is_palindrome(s)==True):
    print(s," is a palindrome")
else:
    print(s," is not palindrome")
