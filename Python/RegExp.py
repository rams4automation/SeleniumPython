
# match -This method matches the regex pattern in the string with the optional flag. It returns true if a match is found
#        in the string otherwise it returns false.
# search	-This method returns the match object if there is a match found in the string.
# findall	-It returns a list that contains all the matches of a pattern in the string.
# split	-Returns a list in which the string has been split in each match.
# sub	-Replace one or many matches in the string.

import re

# ********************** Find All ******************************************

str = "How are you. How is everything"
matches=re.findall("How",str)

print(matches)

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

str = "The rain in Spain"
x = re.findall("Portugal", str)
print(x)


# ************************************** Search **********************************

str1 = "How are you. How is everything"

matches=re.search("How",str1)

print(matches)

str = "The rain in Spain"
x = re.search("\s", str)
print("The first white-space character is located in position:", x.start())

str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)

# ******************************************************************************

str = "How are you. How is everything"

matches = re.search("How", str)

print(matches.span())

print(matches.group())

print(matches.string)

# ********************************** Split ****************************

str="Twelve:12 Eighty nine:89."
pa="[e]"
result=re.split(pa, str)
print(result)

str = "The rain in Spain"
x = re.split("\s", str)
print(x)

str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)



