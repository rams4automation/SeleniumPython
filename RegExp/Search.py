
# The search() function searches the string for a match, and returns a Match object if there is a match.
#
# If there is more than one match, only the first occurrence of the match will be returned:

import re

str = "The rain in Spain"
x = re.search("ai", str)
print(x)
print("The first located in position:", x.start())


str = "The rain in Spain"
x = re.search("\s", str)

print(x)

print("The first white-space character is located in position:", x.start())


str = "The rain in Spain"
mat=re.search("QTP", str)
print(mat)
