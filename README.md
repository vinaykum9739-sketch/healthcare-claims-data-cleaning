# Healthcare Claims Data Cleaning Project

This Python project demonstrates how healthcare claims data can be validated and processed using business rules.

## Project Objective
Clean and validate claims data before performing healthcare analytics.

## Business Rules Implemented

- Skip invalid claim amounts
- Handle missing values
- Detect negative claim amounts
- Identify unrealistic claim values (>10000)
- Calculate total approved claim amount

## Technologies Used

- Python
- File Handling
- Exception Handling
- Data Validation

## Dataset Example

C001,John,5000,Approved  
C002,Ram,abc,Pending  
C003,Anitha,7000,Approved  

## GitHub Files

- Python Code.py → main processing logic  
- claims_data.txt → dataset  
- README.md → project documentation  

## Output Example

Total Approved Claim Amount: 22000  
Invalid Values: 1  
Missing Values: 1  
Negative Claims: 1  
Large Claims: 1  

This project simulates real-world healthcare data validation used in analytics workflows.
