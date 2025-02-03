# Integer data types
i = 10
j = 90

print(i)
print(j)
# Decimal data type
d = 10.4
d1 = 34.67
print(d)
print(d1)

# String data types
name = "" # empty string
name1 = "12" # it's a string of number
name2 = "A" # It's single character string
name3 = "ABC" # It's text
print(name)
print(name1)
print(name2)
print(name3)

# List data type

l = [10, 20, 30, 50, 45, 343, 45, 34, 45, 45, 56, 34, 45, 56] # size 14 last index 13
print(l[2]) # prints 10
print(l[1]) # prints 20
print(l[0]) # prints 30
print(l[7])
print(len(l)) # len() is inbuilt function which tells a list size or length

print(l[ len(l) - 1 ]) # prints 56

l.append(57)
print(len(l)) # prints size/length 15 and last index 14


#Tuples data type
tup = (10, 20, 30, 40, 50) # size 5 and index 4
print(tup[0])
