
my_string = "Hello Academy"
str2 = "Hi!"
name = "Marlena"
age= 22
hobbies = {'0', '1'}
hobbies1 = {'python', 'volley'}
hobbies2 = {'ehe', 'aha'}
string_tamplate = "My name is {0}. Im {1} years old. My hobbies are {0}"
output = string_tamplate.format(name, age)
#print(len(hobbies))

for a,b,c in zip(hobbies, hobbies1, hobbies2):
    print(a, ', ', b, ', ', c, ', ')