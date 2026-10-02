import json

# Read JSON file
with open('employees.json', 'r') as file:
    data = json.load(file)

# Display all employee records
print("All Employee Records:")

for employee in data['employees']:

    print("Employee ID :", employee['emp_id'])
    print("Name :", employee['name'])
    print("Department :", employee['department'])
    print("Designation :", employee['designation'])
    print()

# Search for an employee using ID
search_id = int(input("Enter Employee ID: "))

for employee in data['employees']:

    if employee['emp_id'] == search_id:

        print("Employee Found:")
        print("Name :", employee['name'])
        print("Department :", employee['department'])
        print("Designation :", employee['designation'])
        break

else:
    print("Employee Not Found")


# Calculate gross salary
print("\nGross Salary:")

for employee in data['employees']:

    basic_salary = employee['earnings']['basic_salary']
    allowance = employee['earnings']['allowance']
    bonus = employee['earnings']['bonus']

    gross_salary = basic_salary + allowance + bonus

    print("Name :", employee['name'], ", Gross Salary :", gross_salary)


# Calculate total deductions
print("\nTotal Deductions:")

for employee in data['employees']:

    tax = employee['deductions']['tax']
    provident_fund = employee['deductions']['provident_fund_deduction']

    total_deductions = tax + provident_fund

    print("Name :", employee['name'], ", Total Deductions :", total_deductions)


# Calculate net salary
print("\nNet Salary:")

for employee in data['employees']:

    basic_salary = employee['earnings']['basic_salary']
    allowance = employee['earnings']['allowance']
    bonus = employee['earnings']['bonus']

    tax = employee['deductions']['tax']
    provident_fund = employee['deductions']['provident_fund_deduction']

    gross_salary = basic_salary + allowance + bonus
    total_deductions = tax + provident_fund

    net_salary = gross_salary - total_deductions

    print("Name :", employee['name'], ", Net Salary :", net_salary)


# Display employees whose net salary is above Rs. 40,000
print("\nEmployees with Net Salary above Rs. 40,000:")

for employee in data['employees']:

    basic_salary = employee['earnings']['basic_salary']
    allowance = employee['earnings']['allowance']
    bonus = employee['earnings']['bonus']

    tax = employee['deductions']['tax']
    provident_fund = employee['deductions']['provident_fund_deduction']

    gross_salary = basic_salary + allowance + bonus
    total_deductions = tax + provident_fund
    net_salary = gross_salary - total_deductions

    if net_salary > 40000:
        print("Name :", employee['name'], ", Net Salary :", net_salary)


# Find employee with highest net salary
highest_salary = 0
highest_employee = ""

for employee in data['employees']:

    basic_salary = employee['earnings']['basic_salary']
    allowance = employee['earnings']['allowance']
    bonus = employee['earnings']['bonus']

    tax = employee['deductions']['tax']
    provident_fund = employee['deductions']['provident_fund_deduction']

    gross_salary = basic_salary + allowance + bonus
    total_deductions = tax + provident_fund
    net_salary = gross_salary - total_deductions

    if net_salary > highest_salary:
        highest_salary = net_salary
        highest_employee = employee['name']

print("\nHighest Net Salary :", highest_employee)
print("Salary :", highest_salary)
