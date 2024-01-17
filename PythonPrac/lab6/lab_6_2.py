# Class Code
class Transaction:
    def __init__(self, type, atm, money, total):
        self.__type = type
        self.__atm_id = atm
        self.__money = money
        self.__total = total
    
    @property
    def type (self):
        return self.__type
    
    @property
    def atm_id (self):
        return self.__atm_id
    
    @property
    def money (self):
        return self.__money
    
    @property
    def total (self):
        return self.__total

class Card:
    def __init__(self, id):
        self.__id = id
        self.__pin = None
        
    @property
    def id(self):
        return self.__id
    
class Account:
    def __init__(self, id, card : Card, money):
        self.__id = id
        self.__card = card
        self.__money = money
        self.__transaction_list = []

    @property
    def id(self):
        return self.__id

    @property
    def transaction_list(self):
        return self.__transaction_list
    
    @transaction_list.setter
    def transaction_list(self, new_transaction):
        self.__transaction_list.append(new_transaction)

    def show_transaction(self):
        for transaction in self.__transaction_list:
            print (transaction.type, "-ATM:", transaction.atm_id, end="")
            if transaction.type == "T":
                print("+", end="")
            print("-", transaction.money, "-", transaction.total, sep="")

    @property
    def money(self):
        return self.__money
    
    def update_money(self, money):
        self.__money += money

    @property
    def card(self):
        return self.__card
    
class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__account_list = []

    @property
    def account_list(self):
        return self.__account_list
    
    def add_account(self, account : Account):
        self.__account_list.append(account)
        return ("Added " + account.id + " !")
    def set_pin(self, account, old_pin, new_pin):
        if isinstance(new_pin, str):
            for ch in new_pin:
                if ord(ch) < '0' or ord(ch) < '9':
                    return "Error"
        if account.card.pin == old_pin or account.card.pin is None:
            account.card.update_pin(new_pin)
            return "Updated new PIN !"
        return "Error"

class Atm:
    def __init__(self, id, money):
        self.__id = id
        self.__money = money
    
    @property
    def money(self):
        return self.__money

    @property
    def id(self):
        return self.__id

    def insert_card(self, bank, card_id, pin):
        for user in bank.user_list:
            for account in user.account_list:
                if card_id == account.card.id :
                    if account.card.pin == pin:
                        return account
        return None

    def deposit(self, account : Account, money : int):
        if money <= 0 or account.money < money:
            return "Error"
        account.update_money(+money)
        atm.money -= money
        atm.add_transaction("D", atm, money, account)
        return "Success"
    

    def withdraw(self, account : Account, money : int):
        if money <= 0 or account.money < money:
            return "Error"
        account.update_money(-money)
        atm.money += money
        atm.add_transaction("W", atm, money, account)
        return "Success"
        
    def transfer(self, old : Account, new : Account, money : int):
        if money <= 0 or old.money < money:
            return "Error"
        old.update_money(-money)
        new.update_money(money)
        self.add_transaction("T", money, old)
        self.add_transaction("T", money, new)
        return "Success"

    def add_transaction(self, type, money, account):
        transaction = Transaction(type, self, money, account.money)
        account.transaction_list.append(transaction)

class Bank:
    def __init__(self) :
        self.__user_list = []
        self.__atm_list = []
    
    @property
    def atm_list(self):
        return self.__atm_list
        
    @property
    def user_list(self):
        return self.__user_list
    
    def add_user(self, user : User):
        self.__user_list.append(user)
    def add_atm(self, atm : Atm):
        self.__atm_list.append(atm)
    def add_data(self, user, atm):
        i = 0
        # print()
        for k, v in user.items():
            self.add_user(User(k, v[0]))
            self.__user_list[i].add_account(Account(v[1], Card(v[2]), v[3]))
            # print(User(k, v[0]).name)
            # print(Account(v[1], Card(v[2]), v[3]).id)
            i+=1
        # print()
        for k, v in atm.items():
            self.add_atm(Atm(k, v))
        #     print(Atm(k, v).id)
        # print()

##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm ={'1001':1000000,'1002':200000}

# kanyok_bank.add_user(User("1-1101-12345-12-0", "Harry Potter"))
# kanyok_bank.user_list[0].add_account(Account(Card("12345"),2000))

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

def create_instance():
    bank = Bank()
    bank.add_data(user, atm)
    return bank
my_bank = create_instance()


# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 
# TODO     1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM

# DONE

# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0

# DONE

# TODO 4 :  เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 
# TODO     1) instance ของ bank
# TODO     2) instance ของ account 
# TODO     3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี (Account)
# TODO     return หากการทำรายการเรียบร้อยให้   return success 
# TODO     ถ้าไม่เรียบร้อยให้                    return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

# DONE

#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test Case #1")
def testcase_1(bank, card_id, pin):
    if (my_bank.atm_list[0].insert_card(bank, card_id, pin) != None ):
        print(my_bank.atm_list[0].insert_card(bank, card_id, pin).id, my_bank.atm_list[0].insert_card(bank, card_id).card.id, "Success")
    else:
        print("Error")
testcase_1(my_bank, "12345", "1245")
print()


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000

print("Test Case #2")
def testcase_2(atm, account, money):
    print ("Hermione account before test : ", account.money)
    my_bank.deposit(atm, account, money)
    print ("Hermione account before test : ", account.money)
testcase_2(my_bank.atm_list[1], my_bank.user_list[1].account_list[0] , 1000)
print()

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test Case #3")
def testcase_3(atm, account, money):
    print(my_bank.deposit(atm, account, money))
testcase_3(my_bank.atm_list[1], my_bank.user_list[1].account_list[0] , -1)
print()

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("Test Case #4")
def testcase_4(atm, account, money):
    print ("Hermione account before test : ", account.money)
    my_bank.withdraw(atm, account, money)
    print ("Hermione account before test : ", account.money)
testcase_4(my_bank.atm_list[1], my_bank.user_list[1].account_list[0] , 500)
print()

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

print("Test Case #5")
def testcase_5(atm, account, money):
    print(my_bank.deposit(atm, account, money))
testcase_5(my_bank.atm_list[1], my_bank.user_list[1].account_list[0] , 2000)
print()

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500


print("Test Case #6")
def testcase_6(atm, account1, account2, money):
    def before1():
        money = account1.money
        def func():
            print("Harry account before test : ", money )
        return func
    def before2():
        money = account2.money
        def func():
            print("Hermione account before test : ", money )
        return func
    first1 = before1()
    first2 = before2()
    my_bank.transfer(atm, account1, account2, money)
    first1()
    print("Harry account after test : ", account1.money)
    first2()
    print("Hermione account after test : ", account2.money )

testcase_6(my_bank.atm_list[1], my_bank.user_list[0].account_list[0],my_bank.user_list[1].account_list[0] , 10000)
print()

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
my_bank.user_list[1].account_list[0].show_transaction()
