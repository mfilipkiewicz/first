# y = True
# s = False
#
# if(y and s):
#     print("TRUE")
# else:
#     print("FALSE")

'''-----------------inny przyklad'''

def get_ful_name(name, default = "Gonzales"):
    first_name = "JUAN"
    last_name = name or default
    return f"{first_name} {last_name}"

print(get_ful_name("amigo"))