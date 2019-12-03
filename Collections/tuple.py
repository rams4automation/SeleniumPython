

thistuple=("apple", "banana", "cherry")

print(thistuple)

print(thistuple[1])



#  ************** Range of Indexes

ratuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(ratuple[2:5])

# ************  Loop Through a Tuple

Rangetuple = ("apple", "banana", "cherry")
for x in Rangetuple:
  print(x)

# **************** Check if Item Exists

checktuple = ("apple", "banana", "cherry")
if "apple" in checktuple:
  print("Yes, 'apple' is in the fruits tuple")

# *************** Tuple Length

lentuple = ("apple", "banana", "cherry")
print(len(lentuple))

# ***************** Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

# ****************** Join Two Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)