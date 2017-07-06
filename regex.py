import re

message = "ojcslkibdx,as_ty@wp.pl"

pattern = r'\w+@\w+.\w+'

m = re.search(pattern, message)
print(message)
if m: # would be None if no match is found
    print(m.group())