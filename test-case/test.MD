# Test Case Scenario
1. Authentication test
    - Register
        - User can register successfully

            ![](docs/1-register.png)
    - Login
        - User can login sucessfully

            ![](docs/2-login.png)

        - User failed to login, wrong email/password

            ![](docs/7-wrong-password.png)

    - Validation
        - Input is empty

            ![](docs/3-empty-input.png)

        - E-mail address too long

            ![](docs/4-long-email.png)

        - Invalid e-mail

            ![](docs/5-invalid-email.png)

        - Invalid password

            ![](docs/6-invalid-password.png)

2. Transaction test
    - User could add items

        ![](docs/9-add-items.png)

    - User could update item
        - Only update name

            ![](docs/10-update-name.png)

        - Only update qty

            ![](docs/11-update-qty.png)

        - Only update price

            ![](docs/12-update-price.png)

        - Update all

            ![](docs/13-update-all.png)

    - User could delete an item

        ![](docs/14-delete-item.png)

    - User could reset transaction (delete entire items)

        ![](docs/16-reset-transaction.png)

    - User could check item on their transaction
    
        ![](docs/15-check-transaction.png)

    - User could check out their transaction

        ![](docs/17-checkout.png)

    - User could see item that they have checked out
    
        ![](docs/18-see-checkout.png)

    - User could exit the program

        ![](docs/19-exit-program.png)
