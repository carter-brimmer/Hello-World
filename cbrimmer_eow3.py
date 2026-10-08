#Carter Brimmer
#9/10/26
# “end of week assignment – week 3”.




#1.
print("Exercise 1")


weight_kgs = float(input("please enter the weight of the package in kg: "))
weight_lbs = weight_kgs * 2.21

shipping_cost_light = 5
shipping_cost_medium = 10
shipping_cost_heavy = 20

if weight_lbs < 5:
    print("the weight of the package", round(weight_lbs, 2), "lbs")
    print("the shipping cost of the package", shipping_cost_light, " $")
    
elif weight_lbs >= 5 and weight_lbs <= 15:
    print("the weight of the package", round(weight_lbs, 2), "lbs")
    print("the shipping cost of the package", shipping_cost_medium, " $")
    
else:
    print("the weight of the package", round(weight_lbs, 2), "lbs")
    print("the shipping cost of the package", shipping_cost_heavy, " $")
    
    

    
 #2.
print("exercise 2")   

employee_hours = float(input("enter the number of hours worked by the employee: "))
full_time = input("please enter employee status for full time (T/F): ")

if employee_hours > 40 and full_time == "T":
    print("employee is eligible for overtime pay")
else: 
    print("employee is not eligible for overtime pay")
    

    

#3.
print("exercise 3")
defect_rate = float(input("Enter defect rate: "))
units = int(input("Enter number of units produced: "))

if defect_rate > 5 or units < 1000:
    print("Quality alert!")
else:
    print("Production normal.")
    
 


#4.

print("excercise 4")
distance = int(input("Enter distance traveled: "))
contractor = input("Is the employee a contractor? (True or False): ") == "True"

if (distance > 100 and not contractor) or (distance < 100 and (contractor or not contractor)):
    print("Reimbursement approved")
else:
    print("Not approved")
    
 
    
    
#5.
print("exercise 5")

manager = input("is the employee a manager? (True/False): ") == "True"
probation = input("is the employee on probation? (True/False): ") == "True"
days_employed = int(input("enter the number of days employed: "))

if manager or (not probation and days_employed > 90):
    print("Access granted")
else:
    print("Access denied")
    
    
    