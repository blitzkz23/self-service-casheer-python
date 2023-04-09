# Self Service Cashier
<img src="https://user-images.githubusercontent.com/68576505/223395308-bc9a8817-e3df-4a51-bfdb-7f9b37984c48.png" alt="Telco Customer Churn" width="60%">
Photo by <a href="https://unsplash.com/@simonkadula?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Simon Kadula</a> on <a href="https://unsplash.com/photos/-gkndM1GvSA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

## Problem Description
Andi is the owner of a large supermarket in one of the cities in Indonesia. Andi plans to improve the business process by creating a self-service cashier system in his supermarket with the hope that customers can directly input the items purchased, the quantity of items purchased, the item price, and other features. Customers who are not in the city can also purchase goods from the supermarket.

After conducting research, Andi realized that he has a problem, which is that he needs a programmer to create the necessary features to ensure the smooth operation of the self-service cashier system in his supermarket.

As a Software Engineer, my role would be to work closely with Andi to gather requirements for the self-service cashier program and understand his specific needs. I would then use my technical expertise to design and develop a software solution that meets these requirements, incorporating the necessary features that Andi requires for his supermarket.

## Requirement
To fulfill Andi's request, here are some objective I decided the program works:

### Technical requirement:
- Create self-service cashier program using Python language
- Connect the program to SQLite database
- Use OOP and modularization to ensure the program's quality
- Apply PEP8 principles to write clean Python program
- Write documentation for each function for accessibility

### Bussiness requirement:
- User could make make/login into their account to access their transaction
- User could make a new transaction
- User could add, update, delete an item from cart and reset transaction to empty the whole cart
- User could check what items on their transaction
- User could check out the their transaction, which will be recorded in database
- Cashier program will implement a discount for each individual item if the total price reach certain value
    - 7% discount if total price > Rp 500.000
    - 6% discount if total price > Rp 300.000
    - 5% discount if total price > Rp 200.000

## Flowchart

![](flowchart.png)

## How to Use
```
    # Create virtual environment
    On Windows: python -m venv <name>
    On Unix/Linux: python3 -m venv <name>

    # Activate scripts
    On Windows: .\<name>\Scripts\activate
    On Unix/Linux: source <name>/bin/activate
    
    # Install dependencies
    pip install requirements.txt

    # Run the program
    python main.py

    # The program then will prompt you about the next instruction that you can follow!
```

## Test Case Scenario
The test case scenario of this program are documented in this following [link](test-case/test.MD)

## Conclusion/Future Work
This simple CLI program is pretty good stuffs that had me review my fundamental programming skills and even learn some new stuff.
Here are few things that could be done to improve this program for future work:
1. Implement clean architecture and S.O.L.I.D principle for cleaner and more robust approach
2. Write more validation for edge case
3. Refactor functions for more efficiency
4. Dockerize program
