def shutdown_func(n):
    v = ''
    if n=="yes":
        print("shutdown")
        v = "valid entry"
    elif n=="no":
        print("abort shutdown")
        v = "valid entry"
    else:
        print("sorry")
        v = "invalid entry"
    return v

n = str(input("Did you click the shutdown button on your computer:"))
op = shutdown_func(n)
print(op)