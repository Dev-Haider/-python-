Python String Methods – Quick Reference

This document provides a simple reference for commonly used Python string methods, with examples and expected outputs.

🔠 Case Conversion

capitalize()

"hello world".capitalize()   # "Hello world"


Converts first character to uppercase, rest to lowercase.

casefold()

"HELLO WORLD".casefold()     # "hello world"


Converts entire string into lowercase (stronger than lower()).

lower()

"HELLO".lower()              # "hello"


Converts all characters to lowercase.

upper()

"hello".upper()              # "HELLO"


Converts all characters to uppercase.

swapcase()

"Hello World".swapcase()     # "hELLO wORLD"


Swaps uppercase ↔ lowercase.

title()

"hello world".title()        # "Hello World"


Converts each word to Title Case.

📐 Alignment & Formatting

center(width, char)

"hello".center(10, "-")      # "--hello---"


Centers string with padding.

ljust(width, char)

"Hello".ljust(10, "-")       # "Hello-----"


Left-justifies string.

rjust(width, char)

"Hello".rjust(10, "-")       # "-----Hello"


Right-justifies string.

zfill(width)

"42".zfill(5)                # "00042"


Pads string with zeros.

🔍 Searching & Checking

count(sub)

"banana".count("a")          # 3


Counts occurrences.

find(sub)

"hello world".find("world")  # 6


Returns first position, -1 if not found.

rfind(sub)

"banana".rfind("a")          # 5


Finds last occurrence.

index(sub)

"hello world".index("world") # 6


Like find() but error if not found.

rindex(sub)

"banana".rindex("a")         # 5


Like rfind() but error if not found.

startswith(prefix)

"python.py".startswith("py") # True


Checks start.

endswith(suffix)

"python.py".endswith(".py")  # True


Checks end.

🔑 String Tests (Boolean)
isalnum() → Alphanumeric only.
isalpha() → Alphabets only.
isdecimal() / isdigit() / isnumeric() → Numbers only.
isidentifier() → Valid Python identifier?
islower() / isupper() / istitle() → Checks letter case.
isspace() → Whitespace only.
isprintable() → No non-printable chars (like \n).
✂️ Stripping & Splitting

strip()

"   hello   ".strip()        # "hello"


Removes leading/trailing spaces.

lstrip() / rstrip()

"   hello   ".lstrip()       # "hello   "
"   hello   ".rstrip()       # "   hello"


split()

"apple banana cherry".split() # ['apple', 'banana', 'cherry']


rsplit(sep, maxsplit)

"apple,banana,cherry".rsplit(",", 1) 
# ['apple,banana', 'cherry']


splitlines()

"Hello\nWorld".splitlines()   # ['Hello', 'World']


partition(sep)

"hello-world".partition("-")  # ('hello', '-', 'world')


rpartition(sep)

"hello-world-python".rpartition("-") 
# ('hello-world', '-', 'python')

🔧 Transformation

replace(old, new)

"I like Java".replace("Java", "Python") 
# "I like Python"


expandtabs(tabsize)

"H\te\tl\tl\to".expandtabs(4)
# "H   e   l   l   o"


join(iterable)

" ".join(["Hello", "World"])  # "Hello World"


maketrans() + translate()

table = str.maketrans("aeiou", "12345")
"hello".translate(table)      # "h2ll4"

📌 Formatting

format()

"My name is {} and I am {} years old".format("Haider", 17)
# "My name is Haider and I am 17 years old"


format_map()

data = {"name": "haider", "age": 17}
"My name is {name} and I am {age}".format_map(data)
# "My name is haider and I am 17"

🔒 Encoding
encode()
"hello".encode()
# b'hello'

Returns bytes version of string.