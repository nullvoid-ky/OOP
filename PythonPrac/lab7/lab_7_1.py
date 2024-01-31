class Bank:
    user_count = 0
    atm_count = 0
    seller_count = 0

    def __init__(self,name):
        self.__name=name
        self.__user_list = []
        self.__atm_list = []
        self.__seller_list = []


    @staticmethod
    def search_function_method(item ,id, instance, instance_name):
        final_search = None
        if isinstance(item , instance):
            final_search = item
            print(Bank.send_message(1, f'{instance_name} {id} searched successfully.'))
        else :
            print(Bank.send_message(0, f'{instance_name} {id} not found'))
        return final_search


    @staticmethod
    def send_message(message_type, message):
        if message_type == 0:
            return ("bank_message: #Error "+message)
        elif message_type == 1:
            return ("bank_message: #Success "+message)
        else:
            return ("bank_message: no message text")

    def add_seller(self, seller):
        if not isinstance(seller, Seller):
            return self.send_message(0, f"Cannot add seller. Invalid seller instance: {seller}")
        self.__seller_list += [seller]
        return self.send_message(1, f"Seller {seller.seller_no} added successfully.")

    def add_atm_machine(self, atm):
        if not isinstance(atm, ATM_machine):
            return self.send_message(0, f"Cannot add ATM machine. Invalid ATM machine instance: {atm}")
        self.__atm_list += [atm]
        return self.send_message(1, f"ATM machine {atm.atm_no} added successfully.")
    
    def add_user(self, user):
        if not isinstance(user, User):
            return self.send_message(0, f"Cannot add user. Invalid user instance: {user}")
        self.__user_list += [user]
        return self.send_message(1,f"User {user.citizen_id} added successfully.")

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

    @property
    def citizen_id(self):
        return self.__citizen_id

    def validate_citizen_id(self, citizen_id):
        return self.__citizen_id == citizen_id
    
    def add_account(self, account):
        if not isinstance(account, Account):
            return Bank.send_message(0, f"Cannot add account. Invalid account instance: {account}")
        self.__account_list += [account]
        return Bank.send_message(1, f"Account {account.account_no} added successfully.")

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
        self.__transaction = []
        self.__card = None

    @property
    def account_no(self):
        return self.__account_no
    
    def validate_account_no(self, account_no):
        return self.__account_no == account_no
    
    def add_card(self, card):
        if not isinstance(card, Card):
            return Bank.send_message(0, f"Cannot add card. Invalid card instance: {card}")
        self.__card = card
        return Bank.send_message(1, f"Card {card.card_no} added successfully.")

    def update_amount_in_account(self, money):
        self.__amount += money

    def __add__(self, money):
        self.update_amount_in_account(+money)

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
        target_account.update_amount_in_account(+money)

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
    def __init__(self,card_no, account, pin):
        self.__card_no = card_no
        self.__account = account
        self.__pin = pin
    
    @property
    def card_no(self):
        return self.__card_no
    
    def validate_card_pin(self, pin):
        return self.__pin == pin

class ATM_Card(Card):

    fee = 150

class Debit_Card(Card):

    fee = 300

class ATM_machine:

    withdraw_limit = 20000

    def __init__(self,atm_no,money):
        self.__atm_no = atm_no
        self.__money = money

    @property
    def atm_no(self):
        return self.__atm_no

    def insert_card(self, card, pin):
        if card.validate(pin):
            return Bank.send_message(1, "Insert card successful")
        return Bank.send_message(0, "Incorrect PIN")

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
    def __init__(self,seller_no,name):
        self.__seller_no = seller_no
        self.__name = name
        self.__edc_list = []
    
    @property
    def seller_no(self):
        return self.__seller_no
    
    def add_edc(self, edc):
        if not isinstance(edc, EDC_machine):
            return Bank.send_message(0, f"Cannot add EDC machine. Invalid EDC machine instance: {edc}")
        self.__edc_list += [edc]
        return Bank.send_message(1, f"Account {edc.edc_no} added successfully.")



class EDC_machine:
    def __init__(self,edc_no,seller):
        self.__edc_no = edc_no
        self.__seller = seller
    
    @property
    def edc_no(self):
        return self.__edc_no



##################################################################################

# กำหนด รูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, ประเภทบัญชี, หมายเลขบัญชี, จำนวนเงินในบัญชี, ประเภทบัตร, หมายเลขบัตร ]}
user ={'1-1101-12345-12-0':['Harry Potter','Savings','1234567890',20000,'ATM','12345'],
       '1-1101-12345-13-0':['Hermione Jean Granger','Saving','0987654321',1000,'Debit','12346'],
       '1-1101-12345-13-0':['Hermione Jean Granger','Fix Deposit','0987654322',1000,'',''],
       '9-0000-00000-01-0':['KFC','Savings','0000000321',0,'',''],
       '9-0000-00000-02-0':['Tops','Savings','0000000322',0,'','']}

atm ={'1001':1000000,'1002':200000}

seller_dic = {'210':"KFC", '220':"Tops"}

EDC = {'2101':"KFC", '2201':"Tops"}

# TODO 1 : สร้าง Instance ของธนาคาร และ สร้าง Instance ของ User, Account, บัตร
# TODO   : จากข้อมูลใน user รูปแบบการนำข้อมูลไปใช้สามารถใช้ได้โดยอิสระ
# TODO   : โดย Account แบ่งเป็น 2 subclass คือ Savings และ FixedDeposit
# TODO   : โดย บัตร แบ่งเป็น 2 subclass คือ ATM และ Debit


scb = Bank('SCB')
print(scb.add_user(User('1-1101-12345-12-0','Harry Potter')))
print(scb.add_user(User('1-1101-12345-13-0','Hermione Jean Granger')))
print(scb.add_user(User('9-0000-00000-01-0','KFC')))
print(scb.add_user(User('9-0000-00000-02-0','Tops')))
harry = Bank.search_function_method(scb.search_user_from_id('1-1101-12345-12-0'),"1-1101-12345-12-0", User, "User")
print(harry.add_account(SavingAccount('1234567890', harry, 20000)))
harry_account = Bank.search_function_method(harry.search_account('1234567890') ,"1234567890", Account, "Account")
print(harry_account.add_card(ATM_Card('12345', harry, '1234')))
hermione = Bank.search_function_method(scb.search_user_from_id('1-1101-12345-13-0'),'1-1101-12345-13-0',User,"User")
print(hermione.add_account(SavingAccount('0987654321',hermione,2000)))
hermione_account1 = Bank.search_function_method( hermione.search_account('0987654321'), "0987654321", Account, "Account")
print(hermione_account1.add_card(Debit_Card('12346',hermione_account1,'1234')))
print(hermione.add_account(FixDepositAccount('0987654322',hermione,1000)))
kfc = Bank.search_function_method( scb.search_user_from_id('9-0000-00000-01-0'), '9-0000-00000-01-0', User, "User")
print(kfc.add_account(SavingAccount('0000000321', kfc, 0)))
tops = Bank.search_function_method( scb.search_user_from_id('9-0000-00000-02-0'), '9-0000-00000-02-0', User, "User")
print(tops.add_account(SavingAccount('0000000322', tops, 0)))
# TODO 2 : สร้าง Instance ของเครื่อง ATM

print(scb.add_atm_machine(ATM_machine('1001',1000000)))
print(scb.add_atm_machine(ATM_machine('1002',200000)))

# TODO 3 : สร้าง Instance ของ Seller และใส่เครื่อง EDC ใน Seller 

temp = Seller('210','KFC')
print(temp.add_edc(EDC_machine('2101',temp)))
print(scb.add_seller(temp))
temp = Seller('220',"Tops")
print(temp.add_edc(EDC_machine('2201',temp)))
print(scb.add_seller(temp))

# TODO 4 : สร้าง method ฝาก โดยใช้ __add__ ถอน โดยใช้ __sub__ และ โอนโดยใช้ __rshift__
# TODO   : ทดสอบการ ฝาก ถอน โอน โดยใช้ + - >> กับบัญชีแต่ละประเภท


#clear
print("clear")
exit()

# TODO 5 : สร้าง method insert_card, deposit, withdraw และ transfer ที่ตู้ atm และเรียกผ่าน account อีกที
# TODO   : ทดสอบโอนเงินระหว่างบัญชีแต่ละประเภท

# TODO 6 : สร้าง method paid ที่เครื่อง EDC และเรียกผ่าน account อีกที

# TODO 7 : สร้าง method __iter__ ใน account สำหรับส่งคืน transaction เพื่อให้ใช้กับ for ได้ 

# Test case #1 : ทดสอบ การฝาก จากเครื่อง ATM โดยใช้บัตร ATM ของ harry
# ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method deposit จากเครื่อง ATM และเรียกใช้ + จาก account
# ผลที่คาดหวัง :
# Test Case #1
# Harry's ATM No :  12345
# Harry's Account No :  1234567890
# Success
# Harry account before deposit :  20000
# Deposit 1000
# Harry account after deposit :  21000

atm_machine = scb.search_atm_machine('1001')
harry_account = scb.search_account_from_card('12345')
atm_card = harry_account.get_card()
print("Test Case #1")
print("Harry's ATM No : ",atm_card.card_no)
print("Harry's Account No : ",harry_account.account_no)
print(atm_machine.insert_card(atm_card, "1234"))
print("Harry account before deposit : ",harry_account.amount)
print("Deposit 1000")
atm_machine.deposit(harry_account,1000)
print("Harry account after deposit : ",harry_account.amount)
print("")

# Test case #2 : ทดสอบ การถอน จากเครื่อง ATM โดยใช้บัตร ATM ของ hermione
# ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 2 และบัตร atm ของ hermione
# และเรียกใช้ function หรือ method withdraw จากเครื่อง ATM และเรียกใช้ - จาก account
# ผลที่คาดหวัง :
# Test Case #2
# Hermione's ATM No :  12346
# Hermione's Account No :  0987654321
# Success
# Hermione account before withdraw :  2000
# withdraw 1000
# Hermione account after withdraw :  1000

atm_machine = scb.search_atm_machine('1002')
hermione_account = scb.search_account_from_card('12346')
atm_card = hermione_account.get_card()
print("Test Case #2")
print("Hermione's ATM No : ", atm_card.card_no)
print("Hermione's Account No : ", hermione_account.account_no)
print(atm_machine.insert_card(atm_card, "1234"))
print("Hermione account before withdraw : ",hermione_account.amount)
print("withdraw 1000")
atm_machine.withdraw(hermione_account,1000)
print("Hermione account after withdraw : ",hermione_account.amount)
print("")


# Test case #3 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ที่เคาน์เตอร์
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง
# Test Case #3
# Harry's Account No :  1234567890
# Hermione's Account No :  0987654321
# Harry account before transfer :  21000
# Hermione account before transfer :  1000
# Harry account after transfer :  11000
# Hermione account after transfer :  11000

harry_account = scb.search_account_from_card('12345')
hermione_account = scb.search_account_from_card('12346')
print("Test Case #3")
print("Harry's Account No : ",harry_account.account_no)
print("Hermione's Account No : ", hermione_account.account_no)
print("Harry account before transfer : ",harry_account.amount)
print("Hermione account before transfer : ",hermione_account.amount)
harry_account.transfer("0000", 10000, hermione_account)
print("Harry account after transfer : ",harry_account.amount)
print("Hermione account after transfer : ",hermione_account.amount)
print("")

# Test case #4 : ทดสอบการชำระเงินจากเครื่องรูดบัตร ให้เรียกใช้ method paid จากเครื่องรูดบัตร
# โดยให้ hermione ชำระเงินไปยัง KFC จำนวน 500 บาท ผ่านบัตรของตัวเอง
# ผลที่คาดหวัง
# Hermione's Debit Card No :  12346
# Hermione's Account No :  0987654321
# Seller :  KFC
# KFC's Account No :  0000000321
# KFC account before paid :  0
# Hermione account before paid :  11000
# KFC account after paid :  500
# Hermione account after paid :  10500

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
kfc_account = scb.search_account_from_account_no('0000000321')
kfc = scb.search_seller('KFC')
edc = kfc.search_edc_from_no('2101')

print("Test Case #4")
print("Hermione's Debit Card No : ", debit_card.card_no)
print("Hermione's Account No : ",hermione_account.account_no)
print("Seller : ", kfc.name)
print("KFC's Account No : ", kfc_account.account_no)
print("KFC account before paid : ",kfc_account.amount)
print("Hermione account before paid : ",hermione_account.amount)
edc.paid(debit_card, 500, kfc_account)
print("KFC account after paid : ",kfc_account.amount)
print("Hermione account after paid : ",hermione_account.amount)
print("")

# Test case #5 : ทดสอบการชำระเงินแบบอิเล็กทรอนิกส์ ให้เรียกใช้ method paid จาก kfc
# โดยให้ Hermione ชำระเงินไปยัง Tops จำนวน 500 บาท
# ผลที่คาดหวัง
# Test Case #5
# Hermione's Account No :  0987654321
# Tops's Account No :  0000000322
# Tops account before paid :  0
# Hermione account before paid :  10500
# Tops account after paid :  500
# Hermione account after paid :  10000

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
tops_account = scb.search_account_from_account_no('0000000322')
tops = scb.search_seller('Tops')
print("Test Case #5")
print("Hermione's Account No : ",hermione_account.account_no)
print("Tops's Account No : ", tops_account.account_no)
print("Tops account before paid : ",tops_account.amount)
print("Hermione account before paid : ",hermione_account.amount)
tops.paid(hermione_account,500,tops_account)
print("Tops account after paid : ",tops_account.amount)
print("Hermione account after paid : ",hermione_account.amount)
print("")


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด โดยใช้ for loop 