Employee Payroll Management System 
1. Project Title 
Employee Payroll Management System 
 
2. Objective 
The objective of this project is to develop an Employee Payroll Management System using 
XML and JSON. The system stores employee details such as Employee ID, Name, 
Department, Designation, Earnings, and Deductions. 
Python programs are used to read and process the XML and JSON files. The system can 
display employee records, search for an employee by ID, calculate gross salary, total 
deductions and net salary, display employees whose net salary is above ₹40,000, and find the 
employee with the highest net salary. 
 
3. XML Structure 
The XML file used in this project is employees.xml. 
The XML document has <employees> as the root element. Each employee is stored inside an 
<employee> element. 
The Employee ID is stored as an attribute called emp_id. 
Each employee contains: 
• Name  
• Department  
• Designation  
• Earnings  
o Basic Salary  
o Allowance  
o Bonus  
• Deductions  
o Tax  
o Provident Fund Deduction  
XML Structure 
<employees> 
    <employee emp_id="1"> 
        <name>Rahul Sharma</name> 
        <department>IT</department> 
        <designation>Software Developer</designation> 
 
        <earnings> 
            <basic_salary>45000</basic_salary> 
            <allowance>5000</allowance> 
            <bonus>3000</bonus> 
        </earnings> 
 
        <deductions> 
            <tax>4500</tax> 
            <provident_fund_deduction>3600</provident_fund_deduction> 
        </deductions> 
    </employee> 
</employees> 
 
4. DTD Validation 
The XML structure is validated using employees.dtd. 
DTD Code 
<!ELEMENT employees (employee+)> 
 
<!ELEMENT employee (name, department, designation, earnings, deductions)> 
 
<!ATTLIST employee emp_id CDATA #REQUIRED> 
 
<!ELEMENT name (#PCDATA)> 
<!ELEMENT department (#PCDATA)> 
<!ELEMENT designation (#PCDATA)> 
 
<!ELEMENT earnings (basic_salary, allowance, bonus)> 
 
<!ELEMENT basic_salary (#PCDATA)> 
<!ELEMENT allowance (#PCDATA)> 
<!ELEMENT bonus (#PCDATA)> 
 
<!ELEMENT deductions (tax, provident_fund_deduction)> 
 
<!ELEMENT tax (#PCDATA)> 
<!ELEMENT provident_fund_deduction (#PCDATA)> 
Validation Result 
The employees.xml file was successfully validated against employees.dtd. 
Result: The XML document is well-formed and valid according to the DTD. 
 
5. JSON Structure 
The JSON file used in this project is employees.json . 
The employee records are stored inside an employees array. 
Each employee contains Employee ID, Name, Department, Designation, Earnings and 
Deductions. 
JSON Structure 
{ 
    "employees": [ 
        { 
            "emp_id": 1, 
            "name": "Rahul Sharma", 
            "department": "IT", 
            "designation": "Software Developer", 
            "earnings": { 
                "basic_salary": 45000, 
                "allowance": 5000, 
                "bonus": 3000 
            }, 
            "deductions": { 
                "tax": 4500, 
                "provident_fund_deduction": 3600 
            } 
        } 
    ] 
} 
The JSON file contains records for 5 employees. 
 
6. Parsing Code 
6.1 XML Parser – xml_parser.py 
The XML parser uses Python's xml.etree.ElementTree module to read and process the XML 
file. 
The program performs the following operations: 
1. Displays all employee records.  
2. Searches employee by Employee ID.  
3. Calculates gross salary.  
4. Calculates total deductions.  
5. Calculates net salary.  
6. Displays employees with net salary above ₹40,000.  
7. Finds the employee with the highest net salary.  
Salary Calculations 
Gross Salary 
Gross Salary = Basic Salary + Allowance + Bonus 
Total Deductions 
Total Deductions = Tax + Provident Fund Deduction 
Net Salary 
Net Salary = Gross Salary - Total Deductions 
6.2 JSON Parser – json_parser.py 
The JSON parser uses Python's json module to read and process the employees.json file. 
The program performs the same payroll operations: 
1. Displays all employee records.  
2. Searches employee by Employee ID.  
3. Calculates gross salary.  
4. Calculates total deductions.  
5. Calculates net salary.  
6. Displays employees with net salary above ₹40,000.  
7. Finds the employee with the highest net salary.  
 
7. Program Output 
The project contains 5 employee records. 
Employee Salary Details 
Employee 
Gross Salary 
₹53,000 
Total Deductions 
Rahul Sharma 
Net Salary 
₹8,100 
Priya Patil 
₹44,900 
₹47,000 
₹7,200 
Amit Joshi 
₹39,800 
₹49,000 
₹7,560 
Sneha Desai 
₹41,440 
₹44,500 
₹6,840 
Rohan Mehta 
₹37,660 
₹60,000 
₹9,000 
Employees with Net Salary Above ₹40,000 
₹51,000 
• Rahul Sharma – ₹44,900  
• Amit Joshi – ₹41,440  
• Rohan Mehta – ₹51,000  
Highest Net Salary 
Employee: Rohan Mehta 
Net Salary: ₹51,000 
Employee Search 
The program allows the user to enter an Employee ID. 
For example: 
Enter Employee ID: 4 
The program displays the details of: 
Employee Name: Sneha Desai 
Department: Marketing 
Designation: Marketing Executive 
8. Syntax Errors and Corrections 
During XML validation, an incorrect closing tag was temporarily used to test error handling. 
Incorrect XML 
<name>Rahul Sharma</nme> 
The opening tag was <name> but the closing tag was incorrectly written as </nme>. 
This caused an XML validation error because the opening and closing tags must match. 
Correct XML 
<name>Rahul Sharma</name> 
After correcting the closing tag, the XML file was successfully validated against the DTD. 
The final employees.xml file contains the correct version. 
9. Conclusion 
The Employee Payroll Management System was successfully developed using XML, DTD, 
JSON, and Python. 
The XML file stores employee information in a structured format and is validated using 
DTD. The JSON file stores the same employee records in JSON format. Python programs are 
used to parse the data, search employees, calculate salaries and deductions, identify 
employees with net salary above ₹40,000, and find the highest net salary. 
This project demonstrates the practical use of XML, DTD, JSON, and Python parsing for 
managing employee payroll data. 
Figure 1: employees.xml File 
Figure 2: employees.json File 
Figure 3: XML Parser Code 
Figure 4: XML Parser Output 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 5: JSON Parser Code 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 6: JSON Parser Output 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 7: DTD Validation Result 
Figure 8: XML Validation Error 
Figure 9: Corrected XML Validation Result 
Final project folder 
project/ 
│ 
├── employees.xml 
├── employees.dtd 
├── employees.xsd 
├── employees.json 
├── xml_parser.py 
├── json_parser.py 
│ 
└── output-screenshots/ 
├── dtd-validation.png 
├── xml-parser-output.png 
├── json-parser-output.png 
├── xml-error.png 
├── xml-correction.png 
├── json-parser-code.png 
├── xml-file.png 
├── json-file.png 
└── xml-parser-code.png 
