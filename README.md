# bank-management-system
# 🏦 Bank Management System  

A simple **Bank Management System** built using **Python** and **MySQL**.  
This project allows **Admin** and **Users** to perform various banking operations like account creation, login, deposits, withdrawals, pin changes, and transaction history management.  

---

## 🚀 Features  

### 👨‍💻 Admin  
- View all users  
- View complete account details of a particular user  
- View complete transactions of a particular user  
- View transactions of a particular day  

### 👤 User  
- Register as a new user with account number & pin generation  
- Secure login with account number and pin  
- View account details  
- Debit (withdraw) money  
- Credit (deposit) money  
- Change ATM Pin  
- View mini statement / transaction history  

---

## 🛠️ Technologies Used  
- **Python 3.13**  
- **MySQL Connector for Python**  
- **MySQL Database**  

---

## 🗄️ Database Structure  

### Table: `users3`  
| Column          | Type        | Description              |  
|-----------------|-------------|--------------------------|  
| user_name       | VARCHAR     | User’s name              |  
| mobile_number   | VARCHAR(10) | Mobile number            |  
| adhar_no        | VARCHAR(12) | Aadhaar number           |  
| pin             | VARCHAR(4)  | ATM pin                  |  
| account_number  | VARCHAR(10) | Unique account number    |  
| amount          | INT         | Current balance          |  

### Table: `transactions1`  
| Column          | Type        | Description              |  
|-----------------|-------------|--------------------------|  
| account_number  | VARCHAR     | User’s account number    |  
| amount          | INT         | Transaction amount       |  
| type            | VARCHAR     | debit/credit             |  
| t_time          | DATETIME    | Transaction timestamp    |  

---
