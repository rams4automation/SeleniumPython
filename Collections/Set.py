

thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
    print(x)

# ***************** Access Items

if "banana" in thisset:
    print("banana" in thisset)


# ************** Add Items

adset= {"apple", "banana", "cherry"}
adset.add("Test")
print(adset)

# ***************** Update Items

upset= {"apple", "banana", "cherry"}

upset.update(["orange", "mango", "grapes"])

print(upset)

print(len(upset))

