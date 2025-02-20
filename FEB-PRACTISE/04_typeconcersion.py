def tc1():
    n = 10
    result = n + 2.5  # Implicit type conversion (int -> float)
    print(result)
    print(type(result))  # Output: <class 'float'>

tc1()

def tc2():
    age = 25
    message = f"I am {age} years old."  # f-string (Python 3.6+)
    print(message) # Output: I am 25 years old.
    print(type(message))

tc2()

def tc3():
    a=5
    b=float(a)
    print(b,type(b))
tc3()

def tc4():
    c=10.5
    d=int(c)
    print(d,type(d))

tc4()
