mytuples =("Apple","banana","cherry")
#Tuples are indexed so tuples can have duplicates
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#Tuple DataTypes
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
# tuples Can have multiple datatypes
# Check if Item Exists
if "Apple" in mytuples:
    print("Yes it is there")
else:
    print("Nope")
#update tuples
m1 = list(mytuples)
m1[0] = "straw-berry"
mytuples = tuple(m1)
print("Includes new fruit")
print(mytuples)

