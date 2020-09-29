'''
# BASIC FUNCTION
def greet(name):
    print("Hello",name)
    print("What's going on")
greet("Athi")
greet("Gongotha")
greet("So this is how recursive function works")
print("We call a function outside a function()")


# RECURSIVE FUNCTION
def calc_sum(n):
    if n==1:
        return 1
    else:
        return n + calc_sum(n-1)
sum=calc_sum(3)
print(sum)
'''

# THIS IS A PALINDROME FUNCTION
def is_palindrome(s):
    if len(s)<=1:
        return True
    else:
        if s[0]!=s[len(s)-1]:
            return False
        else:
                return is_palindrome((s[1:len(s)-1]))
print(is_palindrome("level"))

'''
# BASIC ADDITION FUNCTION
def add_2_numbers(num1,num2):
    answer=num1+num2
    return answer

f_num =int(input("enter first number\n"))
s_num =int(input("enter second number\n"))

solution = add_2_numbers(f_num , s_num)
print(f_num , "+", s_num , "=", solution)
'''
