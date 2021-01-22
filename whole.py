max_num = int(input("Enter the maximum whole number you want:"))
mul1 = int(input("Enter 1st multiple you want to be found: "))
mul2 = int(input("Enter 2nd multiple you want to be found: "))
final_num = 0
for i in range(1,max_num+1):
    if(i % mul1 == 0 or i % mul2 == 0):
        final_num = final_num + i
        #print(i)
print("Sum of all the multiples of ",mul1," and ", mul2, "from 1 to", max_num,"is: ",final_num)
    