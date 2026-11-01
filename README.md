# Chiranjeevi-Verma_01028_Resturant-Billing-System

# 🍽️ Restaurant Billing System

### Python Programming Project – PS No. 33

**Developed by:** Chiranjeevi Verma  
**Branch:** Bachelor of Technology – Computer Science and Engineering  
**Programming Language:** Python 3

---

## 📌 Project Overview

The Restaurant Billing System is a simple console-based application developed using Python.

This project helps restaurant cashiers manage customer orders and generate bills automatically. It allows users to select food items, enter quantities, calculate the subtotal, apply discounts, calculate GST, and display the final bill.

## 🎯 Objectives

- To create a simple restaurant billing application.
- To manage food items and their prices using a dictionary.
- To accept customer orders and quantities.
- To calculate subtotal, discount, GST, and grand total.
- To validate invalid item names and quantities.
- To generate a properly formatted customer bill.

## 🍴 Restaurant Menu

| Food Item | Price |
|---|---:|
| Dosa | ₹80 |
| Idli | ₹40 |
| Thali | ₹150 |
| Tea | ₹20 |

## 💰 Billing Rules

1. A 10% discount is provided when the subtotal is more than ₹500.
2. GST is calculated at 5% on the amount after discount.
3. The final bill displays subtotal, discount, GST, and grand total.

**Formula:**

- Subtotal = Sum of item price × quantity
- Discount = 10% of subtotal (if subtotal > ₹500)
- GST = 5% of amount after discount
- Grand Total = Subtotal − Discount + GST

## ⚙️ Features

- Display restaurant menu.
- Add multiple food items.
- Enter item quantities.
- Validate item names.
- Validate quantities (minimum 1).
- Automatic subtotal calculation.
- Automatic discount calculation.
- Automatic GST calculation.
- Generate formatted customer bills.
- Handle invalid inputs.

## 🛠️ Technologies Used

- Python 3
- Visual Studio Code
- Python Dictionaries
- Python Lists
- Loops
- Functions
- Conditional Statements
- Exception Handling

## 📂 Project Structure

```text
Restaurant Billing System/
│
└── restaurant_billing.py
```

## ▶️ How to Run the Project

**Step 1:** Install Python 3 on your computer.

**Step 2:** Download or clone this repository.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal and execute:

```bash
python restaurant_billing.py
```

**Step 5:** Enter food item names and quantities.

**Step 6:** Type `done` to generate the final bill.

## 🧪 Test Cases

| Test Case | Description | Expected Result |
|---|---|---|
| Test Case 1 | Dosa × 2 | Amount ₹160 |
| Test Case 2 | Tea × 1 | Grand Total ₹21 |
| Test Case 3 | Invalid item / quantity | Error message |
| Test Case 4 | Thali × 4, Dosa × 2, Tea × 2 | Grand Total ₹756 |

## 📚 Concepts Learned

Through this project, I learned:

1. How to use dictionaries to store menu items and prices.
2. How to use lists to store customer orders.
3. How to use loops for repeated input.
4. How to create functions for different calculations.
5. How to use conditional statements.
6. How to handle invalid input using try-except.
7. How to perform mathematical calculations in Python.

## 🎓 Conclusion

The Restaurant Billing System is a beginner-friendly Python project that demonstrates the practical use of basic programming concepts.

It makes restaurant billing easier by automatically calculating item amounts, discounts, GST, and the final bill.

This project helped me improve my Python programming, logical thinking, and problem-solving skills.

---

**Project Name:** Restaurant Billing System  
**Project Number:** PS No. 33  
**Developed by:** Chiranjeevi Verma

⭐ Thank you for visiting my project repository!
