def compare(ages,ages1):
    #return =False
    for x in ages:
        for y in ages1:
            if x == y:
                result=True
                return result
ages=[2,12,12,14,15,16,16, 17,18, 14, 20, 20]
ages1=[2,4,12,14,15,16,16, 17,18, 14, 20, 20]
print(compare(ages, ages1))