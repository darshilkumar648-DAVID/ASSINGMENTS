CREATE DATABASE ASSINGMENT;
USE ASSINGMENT;
CREATE TABLE Company (
    CompanyID INT PRIMARY KEY,
    CompanyName VARCHAR(65),
    Street VARCHAR(55),
    City VARCHAR(45),
    State VARCHAR(40),
    Zip VARCHAR(50)
);

INSERT INTO Company (CompanyID, CompanyName, Street, City, State, Zip) 
VALUES
(1, 'Urban Outfitters, Inc.', '123 Main St', 'Austin', 'Texas', '73301'),
(2, 'GreenField Ltd', '45 Oak Ave', 'Denver', 'Colorado', '80201'),
(3, 'Toll Brothers', '900 Market St', 'San Francisco', 'California', '94103');

CREATE TABLE Contact (
    ContactID INT PRIMARY KEY,
    CompanyID INT,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Street VARCHAR(55),
    City VARCHAR(45),
    State VARCHAR(40),
    Zip VARCHAR(50),
    IsMain BOOLEAN,
    Email VARCHAR(55),
    Phone VARCHAR(20),
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);

INSERT INTO Contact (ContactID, CompanyID, FirstName, LastName, Street, City, State, Zip, IsMain, Email, Phone) 
VALUES
(1, 1, 'John', 'Miller', '123 Main St', 'Austin', 'Texas', '73301', TRUE, 'john.miller@technova.com', '512-555-1001'),
(2, 1, 'Emma', 'Stone', '124 Main St', 'Austin', 'Texas', '73301', FALSE, 'emma.stone@technova.com', '512-555-1002'),
(3, 2, 'Dianne', 'Connor', '45 Oak Ave', 'Denver', 'Colorado', '80201', TRUE, 'liam.brown@greenfield.com', '303-555-2001'),
(4, 3, 'Olivia', 'Davis', '900 Market St', 'San Francisco', 'California', '94103', TRUE, 'olivia.davis@skyline.com', '415-555-3001');

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Salary INT,
    HireDate DATE,
    JobTitle VARCHAR(35),
    Email VARCHAR(55),
    Phone VARCHAR(20)
);

INSERT INTO Employee (EmployeeID, FirstName, LastName, Salary, HireDate, JobTitle, Email, Phone) 
VALUES
(1, 'Michael', 'Scott', 75000, '2021-05-10', 'Sales Manager', 'michael.scott@company.com', '215-111-0001'),
(2, 'Lesley', 'Bland', 68000, '2022-03-15', 'Account Executive', 'sarah.connor@company.com', '215-111-0002'),
(3, 'Jack', 'Lee', 82000, '2020-11-20', 'Project Manager', 'Jack.lee@company.com', '215-111-0003');

CREATE TABLE ContactEmployee (
    ContactEmployeeID INT PRIMARY KEY,
    ContactID INT,
    EmployeeID INT,
    ContactDate DATE,
    Description VARCHAR(100),
    FOREIGN KEY (ContactID) REFERENCES Contact(ContactID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

INSERT INTO ContactEmployee (ContactEmployeeID, ContactID, EmployeeID, ContactDate, Description) VALUES
(1, 1, 1, '2023-06-01', 'Initial sales discussion'),
(2, 2, 2, '2023-06-05', 'Follow-up meeting'),
(3, 3, 1, '2023-07-10', 'Contract negotiation'),
(4, 4, 3, '2023-08-02', 'Project requirement discussion');

UPDATE Employee
SET Phone = '215-555-8800'
WHERE FirstName = 'Lesley' AND LastName = 'Bland';

UPDATE Company
SET CompanyName = 'Urban Outfitters'
WHERE CompanyName = 'Urban Outfitters, Inc.';

DELETE ce
FROM ContactEmployee ce
JOIN Contact c ON ce.ContactID = c.ContactID
JOIN Employee e ON ce.EmployeeID = e.EmployeeID
WHERE c.FirstName = 'Dianne' AND c.LastName = 'Connor'
  AND e.FirstName = 'Jack' AND e.LastName = 'Lee';

SELECT DISTINCT e.FirstName, e.LastName
FROM Employee e
LEFT JOIN ContactEmployee ce 
ON e.EmployeeID = ce.EmployeeID
LEFT JOIN Contact c 
ON ce.ContactID = c.ContactID
LEFT JOIN Company co 
ON c.CompanyID = co.CompanyID
WHERE co.CompanyName = 'Toll Brothers';


/* Answer 8 */
/* Significance of % and _ in the LIKE statement.
 Ans : % (percent sign): Matches zero or more characters.
	 Example:
	  SELECT * FROM Employee WHERE FirstName LIKE 'J%';
      Finds names starting with "J" (e.g., John, James, Julia).
      _ (underscore): Matches exactly one character.
	 Example:
      SELECT * FROM Employee WHERE FirstName LIKE 'J_n';
      Finds names like "Jon" or "Jan" but not "John".
*/


/* Answer 9 */
/* Normalization in Databases
 Ans : Definition: A process of structuring a relational database to minimize redundancy and dependency.
       Goals:
             Avoid duplicate data.
			 Ensure data integrity.
             Simplify maintenance.
       Normal Forms:
			 1NF: Each column holds atomic values (no repeating groups).
             2NF: Every non-key attribute depends on the whole primary key.
             3NF: No transitive dependencies (non-key attributes depend only on the key).
	   Example: Instead of storing company details in every contact row, you separate them into a Company table and link via CompanyID.
*/

/* Answer 10 */
/* What does a JOIN in MySQL mean?
 Ans : - JOIN means Combines rows from two or more tables based on related columns.
       - Its Purpose is Retrieve meaningful combined data without duplicating storage.
      Example:
             SELECT e.FirstName, e.LastName, c.CompanyName
             FROM Employee e
             JOIN ContactEmployee ce ON e.EmployeeID = ce.EmployeeID
             JOIN Contact c ON ce—
*/

/* Answer 11 */
/*DDL, DCL, and DML in MySQL.
Ans : - DDL (Data Definition Language): Defines and modifies database structure.
          Commands: CREATE, ALTER, DROP.
          Example: Creating tables or changing schema.
	  - DML (Data Manipulation Language): Deals with data inside tables.
          Commands: INSERT, UPDATE, DELETE, SELECT.
          Example: Adding or updating employee records.
	  - DCL (Data Control Language): Manages access rights and permissions.
          Commands: GRANT, REVOKE.
          Example: Allowing or restricting user privileges.
   Together, they cover structure, data handling, and security in MySQL.

/* Answer 12 */
/*Role of MySQL JOIN Clause.
Ans : - The JOIN clause links rows from two or more tables using related columns.
      - It allows retrieval of connected data without duplicating storage.
	  - Essential for relational databases where information is spread across multiple tables.
      - Makes queries more powerful and efficient by combining data in one result set.

Common Types of Joins :
- INNER JOIN.
   Returns rows with matching values in both tables.
   Example: Shows only the records where both tables share a match.
- LEFT JOIN.
   Returns all rows from the left table, plus matching rows from the right.
   Example: Keeps everything from the left table, adds matches from the right.
- RIGHT JOIN.
   Returns all rows from the right table, plus matching rows from the left.
   Example: Keeps everything from the right table, adds matches from the left.
- FULL JOIN. (emulated with UNION in MySQL)
   Returns all rows when there is a match in either table.
   Example: Combines all rows from both tables, matched or unmatched.
- CROSS JOIN.
   Returns the Cartesian product (all possible combinations).
   Example: Pairs every row in one table with every row in the other.
*/