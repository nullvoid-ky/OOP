# Class Code
class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
class Bank:
    def __init__(self, id, money):
        self.__id = id
        self.__money = money
    
    @property
    def id(self):
        return self.__id
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, new_money):
        self.__money = new_money
    

class Card:
    def __init__(self, id, bank):
        self.__id = id
        self.__bank = bank
        self.__pin = None

    @property
    def id(self):
        return self.__id
    @property
    def bank(self):
        return self.__bank
    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, new_pin):
        self.__pin = new_pin

class Atm:
    def __init__(self, id, money):
        self.__id = id
        if money is None:
            self.__money = 1000000
        else:
            self.__money = money
    
    def insert_card(self, bank, card_id : str):
        for account in account_list:
            if account.bank == bank:
                if account.card.id == card_id:
                    return account
                else :
                    return None
                

    @property
    def id (self):
        return self.__id
    
    @property
    def money (self):
        return self.__money
    @money.setter
    def money(self, new_money):
        self.__money = new_money

class Account:
    def __init__(self, user : User, bank : Bank, card : Card):
        self.__user = user
        self.__bank = bank
        self.__card = card
        # self.__account = {user.id : [user.name, bank.id, card.id, bank.money]}

    # @property
    # def money(self):
    #     return self.__money
    # @property
    # def account(self):
    #     return self.__account
    
    @property
    def user(self):
        return self.__user
    
    @property
    def bank(self):
        return self.__bank
    
    @property
    def card(self):
        return self.__card
    # @card.setter
    # def card (self, new_card):
    #     self.__card = new_card

##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm ={'1001':1000000,'1002':200000}


user_list = []
card_list = []
bank_list = []
atm_list = []
account_list = []
transaction_list = []

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

user_list.append(User("1-1101-12345-12-0", "Harry Potter"))
user_list.append(User("1-1101-12345-13-0", "Hermione Jean Granger"))


bank_list.append(Bank("1234567890", 20000))
bank_list.append(Bank("0987654321", 1000))

card_list.append(Card("12345", bank_list[0]))
card_list.append(Card("12346", bank_list[1]))

account_list.append(Account(user_list[0], bank_list[0], card_list[0]))
account_list.append(Account(user_list[1], bank_list[1], card_list[1]))

atm_list.append(Atm("1001", 1000000))
atm_list.append(Atm("1002", 200000))


# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM




# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0



def deposit(atm : Atm, account : Account, money : int):
    if money <= 0:
        return "error"
    if account.bank.money < money:
        return "error"
    account.bank.money += money
    atm.money -= money
    return "success"


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


def withdraw(atm : Atm, account : Account, money : int):
    if money <= 0:
        return "error"
    if account.bank.money < money:
        return "error"
    account.bank.money -= money
    atm.money += money
    # atm_info = ("ATM:", atm.id)
    # transaction_list.append("W", atm_info,)
    return "success"


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

def transfer(atm : Atm, old : Account, new : Account, money : int):
    if money <= 0:
        return "error"
    if old.bank.money < money:
        return "error"
    old.bank.money -= money
    new.bank.money += money
    return "success"

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success

print()
def test_case_1(atm, bank, card_id ):
    return atm.insert_card(bank, card_id)
print("TEST CASE 1")
ans1 = test_case_1(atm_list[0], bank_list[0], "12345")
if ans1 != None:
    print (ans1.bank.id, ans1.card.id, "Success")
else : print ("ERROR")
print()

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
def test_case_2(atm, account, money):
    return deposit(atm, account, money)
print("TEST CASE 2")
print("Hermione account before test :", account_list[1].bank.money)
ans2 = test_case_2(atm_list[1], account_list[1], 1000)
print("Hermione account before test :", account_list[1].bank.money)
print()


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error


def test_case_3(atm, account, money):
    return deposit(atm, account, money)
print("TEST CASE 3")
ans3 = test_case_3(atm_list[1], account_list[1], -1)
print(ans3)
print()


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500

def test_case_4(atm, account, money):
    return withdraw(atm, account, money)
print("TEST CASE 4")
print("Hermione account before test :", account_list[1].bank.money)
ans4 = test_case_4(atm_list[1], account_list[1], 500)
print("Hermione account before test :", account_list[1].bank.money)
print()

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error


def test_case_5(atm, account, money):
    return withdraw(atm, account, money)
print("TEST CASE 5")
ans5 = test_case_5(atm_list[1], account_list[1], 2000)
print(ans5)
print()

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500


print("TEST CASE 6")
def before_1():
    money = account_list[0].bank.money
    def func():
        print("Harry account before test : ", money )
    return func
def before_2():
    money = account_list[1].bank.money
    def func():
        print("Hermione account before test : ", money)
    return func
def after_1():
    def func():
        print("Harry account after test : ", account_list[0].bank.money)
    return func
def after_2():
    def func():
        print("Hermione account after test : ", account_list[1].bank.money)
    return func

first1 = before_1()
first2 = before_2()
def test_case_6(atm, old, new, money):
    return transfer(atm, old, new, money)
ans6 = test_case_6(atm_list[1], account_list[0], account_list[1], 10000)
last1 = after_1()
last2 = after_2()

first1()
last1()
first2()
last2()
print()

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500