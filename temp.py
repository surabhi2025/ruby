def f_to_c(s):
    """
    Docstring for f_to_c
    :param s: the temp you put in fernheight
    """
    c = (s-32) * 5/9
    return(c)


def c_to_f(v):
    """
    Docstring for c_to_f
    
    :param v: the temputure in celuisis to convert to farenhirght
    """
    d = (v * 9/5) + 32
    return(d)

print("a = f to c")
print("b = c to f")
n = str(input("Chose either a or b: "))

#aprint(n=="a")

if n == "a":
    s =input("Enter your farenhieght temp: ")
    s = float(s)
elif n == "b":
    v = input("enter you celecius temp: ")
    v = float(v)
else:
    print("You entered the wrong thing")

if n == "a":
    temp = f_to_c(s)
    print(temp)
elif n == "b":
    change = c_to_f(v)
    print(change)

