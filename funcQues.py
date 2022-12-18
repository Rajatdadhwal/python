# create z func that will take two argumnt , name and age and print their values




def details(name,age):
    print(name)
    print(age)

details("Rajat","19")  


#create a func in sauch a following  conditions

#it should accept employee name and the salary and display both


#if the salary is missing in the func the assign the default value 10000 to salary 


#Ben(9000)  mike(15000)   Bob()


def google(employee , salary = 10000):
    print(employee,salary)

google("ben", "9000")
google("mike", "15000")
google("bob")


#Question


def info(name , **data): 
    print(name)

    for i,j in data .items():
        print(i,j)



info("Rajat Dadhwal", age=19, place="Repur",num=144222)


def name(x):
    return lambda a : a + x 

num = name(10)
print(num)

