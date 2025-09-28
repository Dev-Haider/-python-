# capitalize()
text = "hello world"
print(text.capitalize())  
# Converts the first character to uppercase and the rest to lowercase → "Hello world"

# casefold()
text = "HELLO WORLD"
print(text.casefold())  
# Converts the string into lowercase → "hello world"

# center()
text = "hello"
print(text.center(10, "-"))  
# Returns a centered string with padding 

# count()
text = "banana"
print(text.count("a"))  
# Returns the number of times "a" occurs 

# encode()
text = "hello"
print(text.encode())  
# Returns the encoded version (bytes) 

# endswith()
text = "python.py"
print(text.endswith(".py"))  
# Returns True if the string ends with ".py" 

# expandtabs()
text = "H\te\tl\tl\to"
print(text.expandtabs(4))  
# Sets tab size (replaces \t with spaces) 

# find()
text = "hello world"
print(text.find("world"))  
# Searches and returns the position of "world" 

# format()
print("My name is {} and I am {} years old".format("Haider", 17))  
# Formats values into string 

# format_map()
data = {"name": "haider", "age": 17}
print("My name is {name} and I am {age}".format_map(data))  
# Formats values using dictionary 

# index()
text = "hello world"
print(text.index("world"))  
# Returns position of "world" (like find but error if not found) 

# isalnum()
text = "Python123"
print(text.isalnum())  
# Returns True if all characters are alphanumeric 

# isalpha()
text = "Python"
print(text.isalpha())  
# Returns True if all characters are alphabetic 

# isdecimal()
text = "12345"
print(text.isdecimal())  
# Returns True if all characters are decimals 

# isdigit()
text = "12345"
print(text.isdigit())  
# Returns True if all characters are digits 

# isidentifier()
text = "variable1"
print(text.isidentifier())  
# Returns True if valid identifier name 

# islower()
text = "python"
print(text.islower())  
# Returns True if all characters are lowercase 

# isnumeric()
text = "12345"
print(text.isnumeric())  
# Returns True if all characters are numeric 

# isprintable()
text = "Hello\nWorld"
print(text.isprintable())  
# Returns False if it contains non-printable chars (like \n) 

# isspace()
text = "   "
print(text.isspace())  
# Returns True if all characters are whitespace 

# istitle()
text = "Hello World"
print(text.istitle())  
# Returns True if follows title rules 

# isupper()
text = "HELLO"
print(text.isupper())  
# Returns True if all characters are uppercase 
                            
# join()
words = ["Hello", "World"]
print(" ".join(words))  
# Joins iterable into string with separator 

# ljust()
text = "Hello"
print(text.ljust(10, "-"))  
# Returns left-justified string 

# lower()
text = "HELLO"
print(text.lower())  
# Converts string into lowercase 

# lstrip()
text = "   hello   "
print(text.lstrip())  
# Removes leading spaces 

# maketrans() + translate()
table = str.maketrans("aeiou", "12345")
print("hello".translate(table))  
# Translates characters 

# partition()
text = "hello-world"
print(text.partition("-"))  
# Splits into 3 parts (before, separator, after) 

# replace()
text = "I like Java"
print(text.replace("Java", "Python"))  
# Replaces substring 

# rfind()
text = "banana"
print(text.rfind("a"))  
# Returns last position of "a" 

# rindex()
text = "banana"
print(text.rindex("a"))  
# Returns last position of "a" 

# rjust()
text = "Hello"
print(text.rjust(10, "-"))  
# Right-justifies string 

# rpartition()
text = "hello-world-python"
print(text.rpartition("-"))  
# Splits from right into 3 parts 

# rsplit()
text = "apple,banana,cherry"
print(text.rsplit(",", 1))  
# Splits from right 

# rstrip()
text = "   hello   "
print(text.rstrip())  
# Removes trailing spaces 

# split()
text = "apple banana cherry"
print(text.split())  
# Splits into list 

# splitlines()
text = "Hello\nWorld\nPython"
print(text.splitlines())  
# Splits at line breaks  

# startswith()
text = "python.py"
print(text.startswith("py"))  
# Returns True if starts with "py"  

# strip()
text = "   hello   "
print(text.strip())  
# Removes leading and trailing spaces  

# swapcase()
text = "Hello World"
print(text.swapcase())  
# Swaps upper  lower alphabat

# title()
text = "hello world"
print(text.title())  
# Converts to title case  

# upper()
text = "hello"
print(text.upper())  
# Converts string into uppercase 

# zfill()
text = "42"
print(text.zfill(5))  
# Pads string with zeros  "00042"
