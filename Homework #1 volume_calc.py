#장육예-20222034-오픈소스SW-03분반
express_fee = 0      # initialize the express_fee

print ("Input the weight of your packet. (kg)")         #weight
weight = int(input("Weight: "))


print ("\nInput the length of your packet. (cm)")         #length
length = int(input("Length: "))
width = int(input("Width: "))
height = int(input("height: "))
total_length = length + width + height


print ("\nIs your destination JEJU?")                     #jeju
destination = str(input("(Y/N)"))
if (destination == "Y" or destination == "y"):
    print ("\nIf you insist on NEXT-DAY DELIVERY, you will pay an extra 2,500 KRW, otherwise it will be delivered IN TWO DAYS. Do you want to pay it?")   #next-day
    next_day_delivery = str(input("(Y/N)"))
    if (next_day_delivery == "Y" or next_day_delivery == "y"):
        express_fee += 2500
    else: pass
else: pass


if ((weight < 0) & (total_length < 0)):
    print("\nSorry, please check your input and try it again.")
elif ((0 < weight <= 5) & (0 < total_length <= 80)):        # the box's total length shoud greater than 0
    express_fee += 5000
elif ((weight <= 10) & (total_length <= 100)):
    express_fee += 8000
elif ((weight <= 20) & (total_length <= 120)):
    express_fee += 10000
elif ((weight <= 30) & (total_length <= 160)):
    express_fee += 13000
else:
    print("\nSorry, please ask the staff for the details of express fee.")
    

if ((0 < total_length <= 160) & (0 < weight <= 30)):       # 'total_length' should be within the range
    print("\nYour express fee's %s KRW." %str(express_fee))
else: pass

    
    
    
#  - the original answer's below -

# #장육예-20222034-오픈소스SW-03분반

# print ("Input the length of your box. (cm)")
# length = int(input("Length: "))
# width = int(input("Width: "))
# height = int(input("height: "))

# express_fee = 0      # initialize the variable in advance for easier code changing

# total_length = length + width + height
# if (0 < total_length <= 80):        # the box's total length shoud greater than 0
#     express_fee = 5000
# elif (total_length <= 100):
#     express_fee = 8000
# elif (total_length <= 120):
#     express_fee = 10000
# elif (total_length <= 160):
#     express_fee = 13000
# else:
#     print("Sorry, please ask the staff for the details of express fee.")
    

# if (0 < total_length <= 160):       # 'total_length' should be within the range
#     print("Your express fee's %s KRW." %str(express_fee))
