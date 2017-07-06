l = [1,2,3]
a,b,c=l
print('\n', a, ' ', b,' ', c, '\n')

def func(a,b,c):
    print(f"pierwszy arg = {a}")
    print(f"drugi arg = {b}")
    print(f"trzeci arg = {c}")

func(*l)