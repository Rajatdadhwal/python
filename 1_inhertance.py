class A:
    def method1(self):
        print("this is the method 1")

class B():
    def method2(self):
        print("This is method 2")
class C(B,A):
    def method3(self):
        print("This is method 3")

objB = A()
objA = B()
objC = C()

objC.method3()