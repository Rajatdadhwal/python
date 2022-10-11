firstnumber=input("enter your digit : ")
operater= input("choose your operater (-,+,*,/,%)")
secondnumber=input("enter your digit : ")


firstnumber=int(firstnumber)
secondnumber=int(secondnumber)

if ("operater == +"):
    print(firstnumber+secondnumber)

elif("operater == -"):
    print(firstnumber-secondnumber)


elif("operater == *"):
    print(firstnumber*secondnumber)     


elif("operater == /"):
    print(firstnumber/secondnumber)    


elif("operater == %"):
    print(firstnumber%secondnumber)


else :
    print("error")

