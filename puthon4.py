
#areaof triangle

a = float(input("enter first side of triangle"))
b = float(input("enter first side of triangle"))
c = float(input("enter first side of triangle"))



s = (a + b  +  c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5

print("area of triangle : " ,area)