#list1 = [10,20,30,40,50]
#triple all the elements in the list:::::


list1 = [10,20,30,40,50]
output = list(map(lambda i : i * 3 , list1))
print(output)


#list2 = [34,88,30,22,10,15,18] 
# print out all the multiple of 5 using filter and lamda:::::

list2 = [34,88,30,22,10,15,18]
output = list(filter(lambda i : i % 5 == 0 , list2))
print(output) 