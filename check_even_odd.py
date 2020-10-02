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
