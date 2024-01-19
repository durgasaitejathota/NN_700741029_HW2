#Define a list
heightList = []

#take input from user for number of customers
noOfCustomers = int(input("Enter number of customers : "))

#for loop to take input and append to list
for i in range(0, noOfCustomers):
    h = float(input())
    heightList.append(h)

#converting inches to cms and appending to a list
newlist = [x*2.54 for x in heightList] 

print(newlist)
