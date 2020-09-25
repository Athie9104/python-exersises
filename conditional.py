'''x=10
if x<=15:
    if(x==10):
        print("Play Cricket")
    else:
        print("Play kabadi")
else:
    print("Don't play game")

stud_mark = int(input('Enter Sudent Mark\n'))

if stud_mark>=80 and stud_mark <=100:
    print("Grade A")
elif stud_mark>=70 and stud_mark <=79:
    print("Grade B")
elif stud_mark>=50 and stud_mark <=69:
    print("Grade C")
elif stud_mark>=40 and stud_mark<=49:
    print("Grade D")
elif stud_mark >=0 and stud_mark<=39:
    print("Grade E")
else:
    print("Enter mark within range")

if 4 < 4:
    print("A")
elif 3 < 4:
    print("B")
else:
    print("C")
    print("D")



Salary=float(input("Enter Monthly Salary Before Deductions\n"))

def permanent_fun():
    inc_tax: float = 29.5/100
    tax_payable = Salary * inc_tax
    net_pay = Salary - tax_payable

def casual_emp():

'''
try:
    drive_speed=int(input("What was your speed in\n"))
    allowed_speed=int(input("What was the allowed speed limit\n"))

    if drive_speed > 60:
        points = (drive_speed - allowed_speed) // 5
        print("You have earned: ", points, "points")
        if points > 12:
            print("See in jail")
    else:
        print("Speed was ok")

except ValueError:
    print("Invalid speed")
