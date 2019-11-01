import re

tekst = "To be, or not to be, that is a question"
vowels = re.findall('(a|e|i|o|u|y|A|E|I|O|U|Y)',tekst)
print("Samogłosek jest: ",len(vowels))