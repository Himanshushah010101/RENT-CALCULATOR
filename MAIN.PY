# Take a input to how much  rent of your flat/hotel
# Take a input to which food items did you ordered within a month
# Take a input to how many units to spend in a month
# Take a input that how much bill per_unit 
# Take a input to how many person stay with you 

#Then code will count total bill of per_unit and divide by how much did you spend a month...
#Then you will have to create new variable and store with addition food,rent,total_bill and divide by persons. 

Rent = int(input("Enter Your Hostel/Flat : "))
Food = int(input("Enter The Amount Of Food Ordered : "))
Electricity_Spend = int(input("Enter The Total Of Electricity Spend : "))
Charge_per_Unit = int(input("Enter The Charge Per Unit : "))
Persons = int(input("Enter The Number Of Persons : "))

Total_bill = Electricity_Spend * Charge_per_Unit

Output = (Food + Rent + Total_bill) // Persons

print("The Total Amount To Be Paid By Each Person Is : ", Output)
