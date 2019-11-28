
# The split() function returns a list where the string has been split at each match:

import re

str="The rain in Spain"
temp=re.split("\s", str)
print(temp)

str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)