def check(x):
    if x %2==0:
        print("{} - this number is even ".format(x))
    elif x%2==1:
        print("{} - this number is odd ".format(x))
    else:
        print("{} - Wrong input ".format(x))

def greet(name):
    print("Hello",name)

def square(x):
    return x**2
