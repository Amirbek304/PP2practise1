def myfunc():
    x = 100
    def innerrfunc():
        print(x)
    innerrfunc()

myfunc()