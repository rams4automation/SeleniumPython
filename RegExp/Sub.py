
# The sub() function replaces the matches with the text of your choice

import re

str = "The rain in Spain"
x = re.sub("rain", "cold", str)
print(x)

str = "The rain in Spain"
x = re.sub("\s", "9", str,2)
print(x)


