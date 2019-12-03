
li = ["apple", "banana", "cherry"]
print(li)

print(li[0])

# Negative Indexing
print(li[-1])

# Range of Indexes
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1[2:5])

list2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list2[:4])

list3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list3[2:])

list4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list4[-4:-1])


#  Change Item Value

Clist = ["apple", "banana", "cherry"]
Clist[1] = "blackcurrant"
print(Clist)

# Loop Through a List


llist = ["apple", "banana", "cherry"]
for x in llist:
  print(x)


# Check if Item Exists

checklist = ["apple", "banana", "cherry"]
if "apple" in checklist:
    print("Yes, 'apple' is in the fruits list")

# List Length

lenlist = ["apple", "banana", "cherry"]
print(len(lenlist))

# Add Items

Addlist = ["apple", "banana", "cherry"]
Addlist.append("orange")
print(Addlist)

inlist=["test","qtp","seleniumwebdriver"]
inlist.insert(1,"Python")
print(inlist)

# *********** Remove ***********

inlist.remove("qtp")
print(inlist)

# ************** del
dellist = ["apple", "banana", "cherry"]
del dellist[0]
print(dellist)

# ************** clear

cllist = ["apple", "banana", "cherry"]
print(cllist)
cllist.clear()
print(cllist)


# *********** Join two list

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# ************** Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)









