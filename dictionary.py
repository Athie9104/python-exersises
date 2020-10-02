this_dict={"brand": "Ford",
"model": "Mustang",
"year":"1964"}
#print(this_dict) # printing all the items of a dictionary

'''for x in this_dict:
    print(x)''' # printing all the key names

'''for x in this_dict:
    print(this_dict[x])'''# print values one by one without keys

'''for x in this_dict.values():
    print(x)'''# to return all the all the values

'''for x, y in this_dict.items():
    print(x, y)'''# to print key and its value

'''if "odel" in this_dict:
    print("Yes, 'model' is one of the keys in this_dict Dictionary")
'''# to check if the value exists in the dictionary

'''this_dict["color"]="red"
print(this_dict)'''# adding items to a dictionary

'''this_dict.pop("model")
print(this_dict)'''# removing items from a dictionary

'''this_dict.popitem()
print(this_dict)'''# removing the last item from a dictionary

'''del this_dict["model"]
print(this_dict)'''# REMOVES ITEM WITH SPECIFIED KEY NAME

'''this_dict.clear()
print(this_dict)'''# this will make dictionary to be empty

'''mydict=this_dict.copy()
print(mydict)'''# to copy or make a duplicate of the dictionary

