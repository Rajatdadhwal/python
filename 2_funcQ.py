#  print(i)



def count(listofnumber):
    even = 0
    odd = 0

    for i in listofnumber:
      if i % 2 ==0:
        even += 1

    else:
        odd =+ 1

    return even , odd                

listofnumber = [32,21,64,100,13]

even,odd = count(listofnumber)
print(even)
print(odd) 

 #question 2 


def fact(n):
    if n ==0:
        return 1
    return n * fact(n-1)

num = fact(5)

print(num)
