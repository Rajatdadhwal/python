def div(a,b):
    print(a/b)


def new_div(func):


    def innerFunc(a,b):

        if a < b :

            a,b = b,a

        return func(a,b)
    return innerFunc
new_div(div)
              