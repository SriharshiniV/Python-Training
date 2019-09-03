def fun(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


fun(5.0, 3.0)
fun(5.0, 5.0) 