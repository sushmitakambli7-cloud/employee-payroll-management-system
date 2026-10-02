import xml.etree.ElementTree as ET

# Read XML file
tree = ET.parse('employees.xml')
root = tree.getroot()

# Display all employee records
print("All Employee Records:")

for employee in root.findall('employee'):

    emp_id = employee.get('emp_id')
    name = employee.find('name').text
    department = employee.find('department').text
    designation = employee.find('designation').text

    print("Employee ID :", emp_id)
    print("Name :", name)
    print("Department :", department)
    print("Designation :", designation)
    print()


# Search for an employee using ID
search_id = input("Enter Employee ID: ")

for employee in root.findall('employee'):

    if employee.get('emp_id') == search_id:

        print("Employee Found:")
        print("Name :", employee.find('name').text)
        print("Department :", employee.find('department').text)
        print("Designation :", employee.find('designation').text)
        break

else:
    print("Employee Not Found")


# Calculate gross salary
print("\nGross Salary:")

for employee in root.findall('employee'):

    name = employee.find('name').text

    basic_salary = int(employee.find('earnings/basic_salary').text)
    allowance = int(employee.find('earnings/allowance').text)
    bonus = int(employee.find('earnings/bonus').text)

    gross_salary = basic_salary + allowance + bonus

    print("Name :", name, ", Gross Salary :", gross_salary)


# Calculate total deductions
print("\nTotal Deductions:")

for employee in root.findall('employee'):

    name = employee.find('name').text

    tax = int(employee.find('deductions/tax').text)
    provident_fund = int(
        employee.find('deductions/provident_fund_deduction').text
    )

    total_deductions = tax + provident_fund

    print("Name :", name, ", Total Deductions :", total_deductions)


# Calculate net salary
print("\nNet Salary:")

for employee in root.findall('employee'):

    name = employee.find('name').text

    basic_salary = int(employee.find('earnings/basic_salary').text)
    allowance = int(employee.find('earnings/allowance').text)
    bonus = int(employee.find('earnings/bonus').text)

    tax = int(employee.find('deductions/tax').text)
    provident_fund = int(
        employee.find('deductions/provident_fund_deduction').text
    )

    gross_salary = basic_salary + allowance + bonus
    total_deductions = tax + provident_fund

    net_salary = gross_salary - total_deductions

    print("Name :", name, ", Net Salary :", net_salary)


# Display employees whose net salary is above Rs. 40,000
print("\nEmployees with Net Salary above Rs. 40,000:")

for employee in root.findall('employee'):

    name = employee.find('name').text

    basic_salary = int(employee.find('earnings/basic_salary').text)
    allowance = int(employee.find('earnings/allowance').text)
    bonus = int(employee.find('earnings/bonus').text)

    tax = int(employee.find('deductions/tax').text)
    provident_fund = int(
        employee.find('deductions/provident_fund_deduction').text
    )

    gross_salary = basic_salary + allowance + bonus
    total_deductions = tax + provident_fund
    net_salary = gross_salary - total_deductions

    if net_salary > 40000:
        print("Name :", name, ", Net Salary :", net_salary)


# Find employee with highest net salary
highest_salary = 0
highest_employee = ""

for employee in root.findall('employee'):

    name = employee.find('name').text

    basic_salary = int(employee.find('earnings/basic_salary').text)
    allowance = int(employee.find('earnings/allowance').text)
    bonus = int(employee.find('earnings/bonus').text)

    tax = int(employee.find('deductions/tax').text)
    provident_fund = int(
        employee.find('deductions/provident_fund_deduction').text
    )

    gross_salary = basic_salary + allowance + bonus
    total_deductions = tax + provident_fund
    net_salary = gross_salary - total_deductions

    if net_salary > highest_salary:
        highest_salary = net_salary
        highest_employee = name

print("\nHighest Net Salary :", highest_employee)
print("Salary :", highest_salary)
