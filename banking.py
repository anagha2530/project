import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

class Bank:
    def __init__(self, name: str, branch: str):
        self.name = name
        self.branch = branch
        self.customers = []

    def add_customer(self, customer_obj: 'Customer') -> None:
        self.customers.append(customer_obj)

    def display_info(self) -> None:
        logging.info(f"Bank Name: {self.name}, Branch: {self.branch}")
        logging.info("Customers:")
        for index, customer in enumerate(self.customers):
            customer.display_info(index=index)

    def transfer_money(self, from_customer: 'Customer', to_customer: 'Customer', amount: float) -> bool:
        if from_customer not in self.customers or to_customer not in self.customers:
            logging.info("Error: One or both customers not found in the bank.")
            return False
        if from_customer == to_customer:
            logging.info("Error: Sender and receiver cannot be the same.")
            return False
        if from_customer.balance < amount:
            logging.info(f"Error: Insufficient balance in {from_customer.name}'s account.")
            return False
        if amount <= 0:
            logging.info("Error: Transfer amount must be positive.")
            return False
        from_customer.balance -= amount
        to_customer.balance += amount
        logging.info(f"Success: {amount} rupees transferred from {from_customer.name} to {to_customer.name}.")
        return True

class Customer:
    def __init__(self, name: str, branch: str, account_no: int, age: int, balance: float):
        self.name = name
        self.branch = branch
        self.account_no = account_no
        self.age = age
        self.balance = balance

    def display_info(self, index: int = None) -> None:
        if index is not None:
            logging.info(f"[{index}] Name: {self.name}, Branch: {self.branch}, Account No: {self.account_no}, Age: {self.age}, Balance: {self.balance}")
        else:
            logging.info(f"Name: {self.name}, Branch: {self.branch}, Account No: {self.account_no}, Age: {self.age}, Balance: {self.balance}")

if __name__ == "__main__":
    bank = Bank("SBI", "TVM")
    customer1 = Customer("Alice", "TVM", 123456, 25, 10000.0)
    customer2 = Customer("Bob", "Kochi", 234567, 35, 500.0)
    customer3 = Customer("Charlie", "TVM", 345678, 30, 2000.0)
    
    bank.add_customer(customer1)
    bank.add_customer(customer2)
    bank.add_customer(customer3)

    logging.info("Account Details:")
    bank.display_info()

    logging.info("\nTransactions:")
    while True:
        logging.info("\nAvailable Customers:")
        bank.display_info()
        
        try:
            sender_index = int(input("Enter the index of the sender: "))
            if sender_index < 0 or sender_index >= len(bank.customers):
                logging.info("Error: Invalid sender index.")
                continue
            receiver_index = int(input("Enter the index of the receiver: "))
            if receiver_index < 0 or receiver_index >= len(bank.customers):
                logging.info("Error: Invalid receiver index.")
                continue
            if sender_index == receiver_index:
                logging.info("Error: Sender and receiver cannot be the same.")
                continue
            
            amount = float(input("Enter the amount to be transferred: "))
            if amount <= 0:
                logging.info("Error: Amount must be positive.")
                continue

            sender = bank.customers[sender_index]
            receiver = bank.customers[receiver_index]
            bank.transfer_money(sender, receiver, amount)

        except ValueError:
            logging.info("Error: Please enter valid numbers for index and amount.")
            continue

        continue_transaction = input("\nDo you want to perform another transaction? (y/n): ").lower()
        if continue_transaction != 'y':
            break

    logging.info("\nFinal Account Details:")
    bank.display_info()