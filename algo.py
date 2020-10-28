def select_sort(items):
    for step in range(len(items)):
        print(items)

        for location in range(len(items)):
            if items[location]  > items[step]:
                #items[location] = items[step]
                items[step],items[location] =items[location],items[step]
x=[3,2,1,7,5,8,4,9,6]
select_sort(x)
print(x)
