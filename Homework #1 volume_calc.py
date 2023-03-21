#장육예-20222034-오픈소스SW-03분반

print ("Input the length of your box. (cm)")
length = int(input("Length: "))
width = int(input("Width: "))
height = int(input("height: "))

express_fee = 0      # initialize the variable in advance for easier code changing

total_length = length + width + height
if (0 < total_length <= 80):        # the box's total length shoud greater than 0
    express_fee = 5000
elif (80 < total_length <= 100):
    express_fee = 8000
elif (100 < total_length <= 120):
    express_fee = 10000
elif (120 < total_length <= 160):
    express_fee = 13000
else:
    print("Sorry, please ask the staff for the details of express fee.")
    

if (0 < total_length <= 160):       # 'total_length' should be within the range
    print("Your express fee's %s KRW." %str(express_fee))
