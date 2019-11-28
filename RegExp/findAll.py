
import re

# The findall() function returns a list containing all matches.

str="How is how are you"
mat=re.findall("How",str)
print(mat)

str="How is Python"
mat=re.findall("hi",str)
print(mat)

str = "The rain in Spain"
mat=re.findall("ai",str)
print(mat)



