#where net salary = gross salary + allowance – deduction.
#Allowances are 10% while deductions are 3% of gross salary

Gross = int(input("Enter the gross salary: "))
Allowance = 0.1*Gross
Deduction = 0.03*Gross
print("The net salary is: ",Gross+Allowance-Deduction)
