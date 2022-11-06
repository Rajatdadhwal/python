#defing a func

def hello():
    print("hello world")
    print("hello rajat")

#calling

hello()

#defing

def rajat():
    print("heyy")
    print("how are you")

#calling

rajat()


def add(num1 , num2):
    sum = (num1 + num2)
    print(sum)

#calling

add(10,10) 


 #substract

def substarction(x,y):  #x,y are parameter
    minus = (x-y)
    print(minus)


substarction(10,5)      #10,5 are argument

#return

def multiply(c,d):
    multi = (c*d)
    return multi

 #calling

x = multiply(10,10)
print(x)


#arguments

def address(*args):
    print(args)

#calling

address("rajat","dadhwal","vill","name","repur")


