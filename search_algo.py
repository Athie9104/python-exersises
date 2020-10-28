def selection_sort_algo(items):
    for step in range(len(items)):
        #print(step)
        #min = step====same as the line below
        location_of_smallest = step
        for location in range(step, len(items)):
            if(items[location] < items[step]):
                items[location] = items[step]
                items[step] = items[location]
        if(location_of_smallest != step):
            items[step]

    return items
x=[3,2,1,7,8,9]
print(selection_sort_algo(x))
