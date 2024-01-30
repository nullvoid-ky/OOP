class Bank:
    user_count = 0
    atm_count = 0
    seller_count = 0

    def __init__(self, name):
        self.__name = name
        self.__user_list = []
        self.__atm_list = []
        self.__seller_list = []

    def send_message(self, message_type, message):
        if message_type == 0:
            return f"bank_message: Error {message}"
        elif message_type == 1:
            return f"bank_message: Success {message}"
        else:
            return "bank_message: no message text"

    def add_seller(self, seller):
        if not isinstance(seller, Seller):
            return self.send_message(0, f"Cannot add seller. Invalid seller instance: {seller}")
        self.__seller_list.append(seller)
        return self.send_message(1, f"Seller {seller.get_seller_no()} added successfully.")

    def add_atm_machine(self, atm):
        if not isinstance(atm, ATM_machine):
            return self.send_message(0, f"Cannot add ATM machine. Invalid ATM machine instance: {atm}")
        self.__atm_list.append(atm)
        return self.send_message(1, f"ATM machine {atm.get_atm_no()} added successfully.")

    def add_user(self, user):
        if not isinstance(user, User):
            return self.send_message(0, f"Cannot add user. Invalid user instance: {user}")
        self.__user_list.append(user)
        return self.send_message(1, f"User {user.get_citizen_id()} added successfully.")

    def search_user_from_id(self, citizen_id):
        if not (isinstance(citizen_id, str) and len(citizen_id) == 17):
            return self.send_message(0, "Search user from ID failed. Invalid citizen ID string.")
        for user in self.__user_list:
            if user.validate_citizen_id(citizen_id):
                return user
        return None


class User:
    def __init__(self, citizen_id, name):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__account_list = []

    def validate_citizen_id(self, citizen_id):
        return self.__citizen_id == citizen_id

    def add_account(self, account):
        if not isinstance(account, Account):
            return Bank.send_message(0, f"Cannot add account. Invalid account instance: {account}")
        self.__account_list.append(account)
        return Bank.send_message(1, f"Account {account.get_account_no()} added successfully.")

    def search_account(self, account_no):
        if not (isinstance(account_no, str) and len(account_no) == 10):
            return Bank.send_message(0, "Search account failed. Invalid account number string.")
        for account in self.__account_list:
            if account.validate_account_no(account_no):
                return account
        return None


class Account:
    def __init__(self, account_no, user, amount):
        self.__account_no = account_no
        self.__user = user
        self.__amount = amount
        self.__transaction_list = []
        self.__card = None

    def validate_account_no(self, account_no):
        return self.__account_no == account_no

    def add_card(self, card):
        if not isinstance(card, Card):
            return Bank.send_message(0, f"Cannot add card. Invalid card instance: {card}")
        self.__card = card
        return Bank.send_message(1, "Card added successfully.")

    def update_amount_in_account(self, money):
        self.__amount += money
        return Bank.send_message(1, "Amount updated successfully.")

    def __add__(self, money):
        self.update_amount_in_account(money)

    def __sub__(self, money):
        if self.__amount < money:
            return Bank.send_message(0, "Withdrawal amount exceeds account balance.")
        self.update_amount_in_account(-money)

    def __rshift__(self, tuple_operand):
        if not (isinstance(tuple_operand, tuple) and len(tuple_operand) == 2):
            return Bank.send_message(0, "Transfer failed. Invalid tuple instance.")
        target_account, money = tuple_operand
        if self.__amount < money:
            return Bank.send_message(0, "Transfer failed. Insufficient funds.")
        if not isinstance(target_account, Account):
            return Bank.send_message(0, "Transfer failed. Invalid target account instance.")

        if not (isinstance(tuple_operand, (int, float)) and tuple_operand > 0):
            return Bank.send_message(0, "Transfer failed. Invalid transfer amount.")
        
        self.update_amount_in_account(-money)
        target_account.update_amount_in_account(money)


class SavingAccount(Account):
    interest_rate = 0.5
    type = "Saving"

    def __init__(self, account_no, user, amount):
        Account.__init__(self, account_no, user, amount)
        self.__card = None


class FixDepositAccount(Account):
    interest_rate = 2.5


class Transaction:
    def __init__(self, transaction_type, amount, total, target_account):
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__total = total
        self.__target_account = target_account


class Card:
    def __init__(self, card_no, account, pin):
        self.__card_no = card_no
        self.__account = account
        self.__pin = pin
    
    def validate_card_pin(self, pin):
        return self.__pin == pin


class ATM_Card(Card):
    fee = 150


class Debit_Card(Card):
    fee = 300


class ATM_machine:
    withdraw_limit = 20000

    def __init__(self, atm_no, money):
        self.__atm_no = atm_no
        self.__money = money

    @property
    def atm_no(self):
        return self.__atm_no

    def insert_card(self, card, pin):
        if card.validate_card_pin(pin):
            return Bank.send_message(1, "Card inserted successfully.")
        return Bank.send_message(0, "Card insertion failed. Incorrect PIN.")

    def deposit(self, account, amount):
        account.update_amount_in_account(amount)
        self.update_amount_in_atm(amount)
        return Bank.send_message(1, "Deposit successful.")

    def withdraw(self, account, amount):
        if amount > self.withdraw_limit:
            return Bank.send_message(0, "Withdrawal failed. Withdrawal amount exceeds limit.")
        if account.validate_account_no(account.get_account_no()) and amount <= self.__money and amount <= account.get_amount():
            account.update_amount_in_account(-amount)
            self.update_amount_in_atm(-amount)
            return Bank.send_message(1, "Withdrawal successful.")
        return Bank.send_message(0, "Withdrawal failed. Insufficient funds or incorrect account number.")

    def transfer(self, account, amount, target_account):
        if amount <= self.__money and amount <= account.get_amount():
            target_account.update_amount_in_account(amount)
            account.update_amount_in_account(-amount)
            self.update_amount_in_atm(-amount)
            return Bank.send_message(1, "Transfer successful.")
        return Bank.send_message(0, "Transfer failed. Insufficient funds.")

    def update_amount_in_atm(self, amount):
        self.__money += amount
        return Bank.send_message(1, "ATM amount updated successfully.")


class Seller:
    def __init__(self, seller_no, name):
        self.__seller_no = seller_no
        self.__name = name
        self.__edc_list = []

    def add_edc(self, edc):
        if not isinstance(edc, EDC_machine):
            return Bank.send_message(0, f"Cannot add EDC machine. Invalid EDC machine instance: {edc}")


class EDC_machine:
    def __init__(self, edc_no, seller):
        self.__edc_no = edc_no
        self.__seller = seller
