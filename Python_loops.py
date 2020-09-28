gas = 45
'''while gas>0:
 print("Vroom")
 gas = gas-1
 if gas == 10:
     print("Fill up")
     break
     #continue
''''''gas = 45

while gas>0:
 print("Vroom")
 gas = gas-1
 if gas == 10:
     print("Fill up")
     #break
     continue


ages = [18, 21, 16, 12]
for age in ages:
    if age>=18:
        print("Come on in let's PARTTY")
    elif age>=16:
        print("Not quite yet wait another 2 years")
    else:
        ("Go plays with dolls")
    '

x=1
while x<=100:
    if x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    elif x%3==0 and x%5==0:
        print("FizzBuzz")
    else:
        print(x)
    x=x+1


def is_palindrome(s):
    if len(s)<=1:
        return True
    else:
        if s[0]!=s[len(s)-1]:
            return False    
        else:
                return is_palindrome((s[1:len(s)-1]))
print(is_palindrome("MAN"))


for x in range(10):
    if x<=4:
        for y in range(x+1):
            print("*", end="")
    else:
        for y in range(10 - x-1):
            print("*", end="")
    print()

'''

import random
guess_taken=0

num = random.randint(0, 10)
while guess_taken<=5:     
    _guess =int(input("Take a guess.\n"))
    guess_taken+=1
    if int(_guess)<int(num):
        print("Your guess is too low. ")
    if int(_guess)>int(num):
        print("Your guess is too high.")
    if int(_guess)==int(num):
        break

    if int(_guess)==int(num):
        guess_taken=str(guess_taken)
        print("Good job",num)

    if int(_guess)!=int(num):
        guess_taken=str(guess_taken)
        print("No the number is. ",num)


