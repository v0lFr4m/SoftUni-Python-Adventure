class MoneyNotEnoughError(Exception):
    """ Raised if there is not enough balance """
    pass

class PINCodeError(Exception):
    """ Raised when pin code is not valid """
    pass

class UnderageTransactionError(Exception):
    """ Raised when age is underage """
    pass

class MoneyIsNegativeError(Exception):
    """ Raised when given money is negative number """
    pass

REQUIRED_AGE = 18

# Unpack the input
pin_code , balance , age = list(map(int,input().split(",")))

while (line := input()) != "End":
    # Split the line in action
    command = line.split("#")
    action = command[0]

    # Checks if the age is under required age
    if age < REQUIRED_AGE:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

    if action == "Send Money":
        amount_of_money = int(command[1])
        given_pin_code = int(command[2])

        # Checks if balance is enough to send the money
        if amount_of_money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        # Pin code validation
        if given_pin_code != pin_code:
            raise PINCodeError("Invalid PIN code")

        balance -= amount_of_money
        # Print if transaction is successful
        print(f"Successfully sent {amount_of_money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif action == "Receive Money":
        amount_of_money = int(command[1])

        # Checks if salary is negative number
        if amount_of_money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        # Half of the salary goes to investments
        salary = amount_of_money / 2

        # Print if transaction is successful and add the salary to the balance
        balance += salary
        print(f"{salary:.2f} money went straight into the bank account")








