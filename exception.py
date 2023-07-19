class BalException(Exception):
    def __init__(self, msg):
        self.msg = msg
        customerid = "123445"
        customername = "mohammed"
        balance = "20000"

        amount = int(input("Enter the amount that you want to withdraw: "))

    if (amount > balance):
        print("Insufficient balance in account")

    else:

        try:
            balance = balance-amount

            if (balance < 5000):
                balance = balance+amount

            raise BalException("min balance shall be maintained is 5000:")
        except BalException as be:
            print(be)

        finally:
            print("the remaining balance is:", balance)
