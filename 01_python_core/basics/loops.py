#For Loop

for i in range (1,5):
    print(i)
    

#List Comparison

squares=[x**2 for x in range (1,6)]
print(squares)

#For Loop through List

fruits=["BAnana","Aple","Mango"]
for fruit in fruits:
    print(fruit)    

#While Loop

count=1

while count<=10:
    print(count)
    count=count+2



#Loop Control

for i in range(1,6):
    if i==3:
        continue
    if i==5:
        break
    print(i)
