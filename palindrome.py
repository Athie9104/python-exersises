
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


'''
def palindrome_1(str1):
    word1=''
    for x in range(len(str1)):
        for y in range(len(str1), x -1):
            if len(word1)>=y-x:
                break
            elif str1[x:y]==str1[x:y][::-1]:
                word1=str1[x:y]
                break
    return word1
word1=input("enter a word\n")
palindrome_1(word1)
print(palindrome_1)
'''
'''
#CHECK IF ODD OR EVEN NUMBER
def check_num(n):
    if n<2:
        return n%2==0
    return (check_num(n-2))
n=int(input("enter number\n"))
if (check_num(n)==True):
    print("It is even")
else:
    print("It's an odd")
'''