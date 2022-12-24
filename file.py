f = open("pexels-adam-kontor-325117.jpg", "rb")

f1 = open("pexels-adam-kontor-325117_copy.jpg", "wb")

print(f.read())

for i in f:
    f1.write(i)  