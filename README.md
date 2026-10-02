# Employee Payroll Management System

An Employee Payroll Management System developed using **XML, DTD, JSON, and Python**.

## Project Objective

The project stores and processes employee payroll information such as Employee ID, Name, Department, Designation, Earnings, and Deductions.

Python programs are used to parse XML and JSON files and perform payroll calculations and employee searches.

## Features

* Display employee records
* Search employee by Employee ID
* Calculate Gross Salary
* Calculate Total Deductions
* Calculate Net Salary
* Display employees with Net Salary above ₹40,000
* Find the employee with the highest Net Salary
* XML validation using DTD
* JSON data processing using Python

## Technologies Used

* XML
* DTD
* JSON
* Python

## Project Structure

```text
Employee-Payroll-Management-System/
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
```

## XML Structure

The XML document uses `<employees>` as the root element. Each employee is stored inside an `<employee>` element with `emp_id` as an attribute.

Employee information includes:

* Name
* Department
* Designation
* Earnings

  * Basic Salary
  * Allowance
  * Bonus
* Deductions

  * Tax
  * Provident Fund Deduction

## DTD Validation

The XML file is validated using `employees.dtd`.

The final XML document is well-formed and valid according to the DTD.

## JSON Structure

The JSON file stores employee records inside an `employees` array.

The project contains records for **5 employees**.

## Salary Calculations

**Gross Salary**

`Gross Salary = Basic Salary + Allowance + Bonus`

**Total Deductions**

`Total Deductions = Tax + Provident Fund Deduction`

**Net Salary**

`Net Salary = Gross Salary - Total Deductions`

## Python Parsing

### XML Parser

`xml_parser.py` uses Python's `xml.etree.ElementTree` module to read and process the XML file.

### JSON Parser

`json_parser.py` uses Python's `json` module to read and process the JSON file.

Both programs perform employee search and payroll calculations.

## Validation and Error Handling

The project includes XML validation using DTD and demonstrates correction of an XML closing-tag error.

Example:

```xml
Incorrect:
<name>Rahul Sharma</nme>

Correct:
<name>Rahul Sharma</name>
```

## Author

**Sushmita Kambli**

B.Sc. Information Technology
