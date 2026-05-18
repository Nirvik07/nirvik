# Employee Management System using JDBC and PostgreSQL

## Project Report

---

# Table of Contents

1. Introduction
2. Objective
3. Technologies Used
4. Software Requirements
5. System Architecture
6. Database Design
7. Project Structure
8. Source Code
9. Working Procedure
10. Output Screens
11. Advantages
12. Limitations
13. Future Enhancements
14. Conclusion
15. References

---

# 1. Introduction

The Employee Management System is a Java-based console application developed using JDBC and PostgreSQL. The system performs CRUD (Create, Read, Update, Delete) operations on employee records stored in a PostgreSQL database.

This project demonstrates how Java applications communicate with relational databases using JDBC API.

---

# 2. Objective

The main objectives of this project are:

- To learn JDBC connectivity with PostgreSQL
- To implement CRUD operations
- To understand SQL query execution using Java
- To create a menu-driven database application
- To manage employee records efficiently

---

# 3. Technologies Used

| Technology | Purpose |
|------------|---------|
| Java | Programming Language |
| JDBC | Database Connectivity |
| PostgreSQL | Relational Database |
| IntelliJ IDEA | IDE |
| SQL | Database Query Language |

---

# 4. Software Requirements

## Hardware Requirements

- Processor: Intel i3 or above
- RAM: 4 GB minimum
- Storage: 500 MB free space

---

## Software Requirements

- JDK 17 or above
- IntelliJ IDEA
- PostgreSQL
- PostgreSQL JDBC Driver

---

# 5. System Architecture

```text
+-------------------+
|   Java Program    |
|  (Console Based)  |
+-------------------+
          |
          | JDBC
          |
+-------------------+
| PostgreSQL Server |
+-------------------+
          |
          |
+-------------------+
| Employee Database |
+-------------------+
```

---

# 6. Database Design

## Database Creation

```sql
CREATE DATABASE company;
```

---

## Connect Database

```sql
\c company
```

---

## Employee Table

```sql
CREATE TABLE Employee (
    emp_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(200),
    contact VARCHAR(15),
    designation VARCHAR(100)
);
```

---

## Table Structure

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| emp_id | INTEGER | Employee ID |
| name | VARCHAR(100) | Employee Name |
| address | VARCHAR(200) | Employee Address |
| contact | VARCHAR(15) | Contact Number |
| designation | VARCHAR(100) | Job Designation |

---

# 7. Project Structure

```text
JDBC_CRUD
│
├── src
│   ├── Employee.java
│   ├── DBConnection.java
│   ├── EmployeeDAO.java
│   └── Main.java
│
└── External Libraries
    └── postgresql-42.x.x.jar
```

---

# 8. Source Code

# 8.1 Employee.java

```java
public class Employee {

    private int empId;
    private String name;
    private String address;
    private String contact;
    private String designation;

    // Default Constructor
    public Employee() {
    }

    // Parameterized Constructor
    public Employee(int empId,
                    String name,
                    String address,
                    String contact,
                    String designation) {

        this.empId = empId;
        this.name = name;
        this.address = address;
        this.contact = contact;
        this.designation = designation;
    }

    // Getter and Setter Methods

    public int getEmpId() {
        return empId;
    }

    public void setEmpId(int empId) {
        this.empId = empId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }

    public String getDesignation() {
        return designation;
    }

    public void setDesignation(String designation) {
        this.designation = designation;
    }
}
```

---

# 8.2 DBConnection.java

```java
import java.sql.Connection;
import java.sql.DriverManager;

public class DBConnection {

    static Connection con;

    public static Connection getConnection() {

        try {

            // PostgreSQL JDBC Driver
            Class.forName("org.postgresql.Driver");

            String url =
                    "jdbc:postgresql://localhost:5432/company";

            String username = "postgres";

            String password = "your_password";

            con = DriverManager.getConnection(
                    url,
                    username,
                    password);

            System.out.println(
                    "Database Connected Successfully");

        } catch (Exception e) {

            System.out.println(
                    "Connection Failed");

            e.printStackTrace();
        }

        return con;
    }
}
```

---

# 8.3 EmployeeDAO.java

```java
import java.sql.*;

public class EmployeeDAO {

    Connection con;

    public EmployeeDAO() {
        con = DBConnection.getConnection();
    }

    // Insert Employee
    public void insertEmployee(Employee emp) {

        try {

            String query =
                    "INSERT INTO Employee VALUES (?, ?, ?, ?, ?)";

            PreparedStatement ps =
                    con.prepareStatement(query);

            ps.setInt(1, emp.getEmpId());
            ps.setString(2, emp.getName());
            ps.setString(3, emp.getAddress());
            ps.setString(4, emp.getContact());
            ps.setString(5, emp.getDesignation());

            int rows = ps.executeUpdate();

            if (rows > 0) {

                System.out.println(
                        "Employee Inserted Successfully");
            }

        } catch (Exception e) {

            e.printStackTrace();
        }
    }

    // View Employees
    public void viewEmployees() {

        try {

            String query =
                    "SELECT * FROM Employee";

            Statement st =
                    con.createStatement();

            ResultSet rs =
                    st.executeQuery(query);

            while (rs.next()) {

                System.out.println(
                        "----------------------");

                System.out.println(
                        "Employee ID : "
                                + rs.getInt("emp_id"));

                System.out.println(
                        "Name : "
                                + rs.getString("name"));

                System.out.println(
                        "Address : "
                                + rs.getString("address"));

                System.out.println(
                        "Contact : "
                                + rs.getString("contact"));

                System.out.println(
                        "Designation : "
                                + rs.getString("designation"));
            }

        } catch (Exception e) {

            e.printStackTrace();
        }
    }

    // Update Employee
    public void updateEmployee(int id,
                               String designation) {

        try {

            String query =
                    "UPDATE Employee SET designation=? WHERE emp_id=?";

            PreparedStatement ps =
                    con.prepareStatement(query);

            ps.setString(1, designation);

            ps.setInt(2, id);

            int rows = ps.executeUpdate();

            if (rows > 0) {

                System.out.println(
                        "Employee Updated Successfully");

            } else {

                System.out.println(
                        "Employee Not Found");
            }

        } catch (Exception e) {

            e.printStackTrace();
        }
    }

    // Delete Employee
    public void deleteEmployee(int id) {

        try {

            String query =
                    "DELETE FROM Employee WHERE emp_id=?";

            PreparedStatement ps =
                    con.prepareStatement(query);

            ps.setInt(1, id);

            int rows = ps.executeUpdate();

            if (rows > 0) {

                System.out.println(
                        "Employee Deleted Successfully");

            } else {

                System.out.println(
                        "Employee Not Found");
            }

        } catch (Exception e) {

            e.printStackTrace();
        }
    }
}
```

---

# 8.4 Main.java

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        EmployeeDAO dao = new EmployeeDAO();

        int choice;

        do {

            System.out.println(
                    "\n===== EMPLOYEE CRUD MENU =====");

            System.out.println(
                    "1. Insert Employee");

            System.out.println(
                    "2. View Employees");

            System.out.println(
                    "3. Update Employee");

            System.out.println(
                    "4. Delete Employee");

            System.out.println(
                    "5. Exit");

            System.out.print(
                    "Enter Your Choice: ");

            choice = sc.nextInt();

            switch (choice) {

                case 1:

                    System.out.print(
                            "Enter Employee ID: ");

                    int id = sc.nextInt();
                    sc.nextLine();

                    System.out.print(
                            "Enter Name: ");

                    String name = sc.nextLine();

                    System.out.print(
                            "Enter Address: ");

                    String address = sc.nextLine();

                    System.out.print(
                            "Enter Contact: ");

                    String contact = sc.nextLine();

                    System.out.print(
                            "Enter Designation: ");

                    String designation = sc.nextLine();

                    Employee emp =
                            new Employee(
                                    id,
                                    name,
                                    address,
                                    contact,
                                    designation);

                    dao.insertEmployee(emp);

                    break;

                case 2:

                    dao.viewEmployees();

                    break;

                case 3:

                    System.out.print(
                            "Enter Employee ID to Update: ");

                    int updateId = sc.nextInt();
                    sc.nextLine();

                    System.out.print(
                            "Enter New Designation: ");

                    String newDesignation =
                            sc.nextLine();

                    dao.updateEmployee(
                            updateId,
                            newDesignation);

                    break;

                case 4:

                    System.out.print(
                            "Enter Employee ID to Delete: ");

                    int deleteId = sc.nextInt();

                    dao.deleteEmployee(deleteId);

                    break;

                case 5:

                    System.out.println(
                            "Exiting Program...");

                    break;

                default:

                    System.out.println(
                            "Invalid Choice");
            }

        } while (choice != 5);

        sc.close();
    }
}
```

---

# 9. Working Procedure

1. Start PostgreSQL server
2. Run Java application
3. Menu options are displayed
4. User selects operation
5. JDBC establishes database connection
6. SQL queries execute
7. Results are displayed

---

# 10. Output Screens

## Main Menu

```text
===== EMPLOYEE CRUD MENU =====
1. Insert Employee
2. View Employees
3. Update Employee
4. Delete Employee
5. Exit
```

---

## Insert Employee

```text
Enter Employee ID: 101
Enter Name: John
Enter Address: Kolkata
Enter Contact: 9876543210
Enter Designation: Manager

Employee Inserted Successfully
```

---

## View Employees

```text
Employee ID : 101
Name : John
Address : Kolkata
Contact : 9876543210
Designation : Manager
```

---

#Demo

# 14. Conclusion

The Employee Management System successfully demonstrates CRUD operations using Java JDBC and PostgreSQL. The project helps in understanding database connectivity, SQL operations, and object-oriented programming concepts.

This system can be expanded into a full-scale enterprise application with additional functionalities.

---

# 15. References

## Official Documentation

- Java Documentation  
  https://docs.oracle.com/en/java/

- PostgreSQL Documentation  
  https://www.postgresql.org/docs/

- JDBC Documentation  
  https://docs.oracle.com/javase/tutorial/jdbc/

- IntelliJ IDEA  
  https://www.jetbrains.com/idea/

---
