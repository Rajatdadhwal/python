
#take the input of the age of 3 people 
#determine the oldest and youngest 



age1 = int(input("enter the age of 1st person"))
age2 = int(input("enter the age of 2and person"))
age3 = int(input("enter the age of 3ard person"))



if age1 > age2  and age1 > age3:
    print("oldest is", age1)

elif age2 > age1 and age2 > age3:
    print("oldest is", age2)    
 
elif age3> age1 and age3 > age2:
    print("oldest is", age3)





