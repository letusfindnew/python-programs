#List
print("List Demo")
lst = [10, 20, 30, 30]
lst.append(40)
lst.remove(10)
print(lst)

print("Tuple Demo")
#Tuple
tup = (50, 60,70, 89, 89)
print(tup)

print("Set Demo")
#Set
st = {123, 456, 456,67, 78}
st.add(432)
st.remove(456)
print(st)

print("Dictionary Demo")
#Dictionary
d = {"A": 10, "B": 20, "C": 30}
d.pop("C")
print(d.get("A"))
print(d)
