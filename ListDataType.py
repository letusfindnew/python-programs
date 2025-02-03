lst = [10,20,30] # list is mutable

print("Size: ", len(lst)) # prints length/size 3 and last index 2

lst.append(40) # lst = [10, 20, 30, 40]

print("Latest Size: ", len(lst)) # prints length/size 4 and last index 3
lst.remove(40) # removing a value at 2nd index
# lst = [10, 20, 40]

print(lst)
lst.clear() # clearing the list
print(lst) # EMPTY