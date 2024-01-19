# Class Code
 
class Card:
    def __init__(self, id):
        self.__id = id
        self.__pin = None
        self.__account_id = None
        
    @property
    def id(self):
        return self.__id
    
    def update_account_id(self, new_account_id):
        self.__account_id = new_account_id
    def update_pin(self, new_pin):
        self.__pin = new_pin

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
            print (transaction.type, "-ATM:", transaction.atm_id,sep="", end="")
            if transaction.type == "T":
                print("+", end="",sep="")
            print("-", transaction.money, "-", transaction.total, sep="")

    @property
    def money(self):
        return self.__money
    @property
    def card(self):
        return self.__card
    
    def change_pin(self, old_pin, new_pin):
        if old_pin is not None:
            if new_pin is not old_pin:
                return "Incorrect PIN"
        self.card.update_pin(new_pin)
        return "Success"

    
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

    def update_money(self, money):
        self.__money += money

    def insert_card(self, bank, card_id, pin):
        for user in bank.user_list:
            for account in user.account_list:
                if card_id == account.card.id :
                    if account.card.pin == pin:
                        return account
        return None
    
    # def add_transaction(self, type, atm, money, account):
    #     transaction = Transaction(type, atm.id, money, account.money)
    #     account.transaction_list.append(transaction)

class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__account_list = []

    @property
    def account_list(self):
        return self.__account_list
    @property
    def id(self):
        return self.__id
    
    def add_account(self, bank, account : Account):
        self.__account_list.append(account)
        account.card.update_account_id(account.id)
        bank.update_account_data(account)
        return bank.console_print( bank.account_data_list, account, "Account")

class Bank:
    def __init__(self, id) :
        self.__user_list = []
        self.__atm_list = []
        self.__account_data_list = []
        self.__add_data_history = []
        self.__id = id
    
    @property
    def id(self):
        return self.__id   
    
    # @property
    # def atm_list(self):
    #     return self.__atm_list
        
    # @property
    # def user_list(self):
    #     return self.__user_list
    
    @property
    def account_data_list(self):
        return self.__account_data_list
    
    def console_print(self, item_list, item, item_name):
        return f"console.log | {self.console_print_data(item_list, item, item_name)}"

    def console_print_data(self, item_list, item, item_name):
        number = len(item_list)
        error_text = f"<====== Error \t  #{number}\tid :{self.id} ======>\n\t - {item_name}: "
        if item_name == "Data":
            return f"<====== Done {item_name} #{number} \tid :{item.id} ======>"
        elif item_name == "Error_01": return f"{error_text} Nothing Changed\n"
        elif item_name == "Error_02": return f"{error_text} Existed Data\n"
        elif item_name == "Error_03": return f"{error_text} Exited Account\n"
        elif item_name == "Error_04": return f"{error_text} Exited ATM\n"
        elif item_name == "Error_05": return f"{error_text} Incorrect Data Format\n"

        return f"Added :{item_name} \t#{number} \tid :{item.id}"


    def update_account_data(self, account):
        self.__account_data_list.append(account)

    def add_user(self, user : User):
        self.__user_list.append(user)
        return self.console_print(self.__user_list, user, "User")
    
    def add_atm(self, atm : Atm):
        self.__atm_list.append(atm)
        return self.console_print(self.__atm_list, atm, "Atm")
    
    def add_atm_money(self, atm : Atm, money : int):
        atm.update_money(money)

    def add_data(self, user, atm):
        add_count = 0
        if user is atm is None:
            self.__add_data_history.append(add_count)
            return self.console_print(self.__add_data_history, self, "Error_01")
        
        """
        check data format before add
        return self.console_print(self.__add_data_history, self, "Error_05")
        """

        if user is not None:
            for k, v in user.items():
                valid = True
                for bank_user in self.__user_list:
                    if bank_user.id is k:
                        valid = False
                        break
                if valid:
                    print(self.add_user(User(k, v[0])))
                    add_count+=1
            for k, v in user.items():
                valid = True
                for bank_user in self.__user_list:
                    if bank_user.id is k:
                        for account in self.account_data_list:
                            if account.id is v[1]:
                                valid = False
                if valid:
                    print(bank_user.add_account(self, Account(v[1], Card(v[2]), v[3])))
                    add_count+=1
                else:
                    self.__add_data_history.append(add_count)
                    return self.console_print(self.__add_data_history, self, "Error_03")
        if atm is not None:
            for k, v in atm.items():
                valid = True
                for atm in self.__atm_list:
                    if atm.id is k:
                        valid = False
                if valid :
                    print(self.add_atm(Atm(k, v)))
                    add_count+=1
                else:
                    self.__add_data_history.append(add_count)
                    return self.console_print(self.__add_data_history, self, "Error_04")
        self.__add_data_history.append(add_count)
        if add_count == 0:
            return {self.console_print(self.__add_data_history, self, "Error_02")}
        return f"{self.console_print(self.__add_data_history, self, "Data")}\n"

##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000],
       '1-1101-12345-12-4':['Kanyok Handsome','32178956409','43121',10]}

user2 ={'1-2222-12345-10-4':['Nana Narak','1234567890','11109',12300],
       '1-2222-10045-13-0':['Nunu is Nana','0828983663','12346',444],
       '1-2222-12345-12-4':['Nullvoid Debateyourdense','32178956409','43121',40]}
user3 = {'1-1101-12345-12-0':['Harry Potter','010101','12345',20000]}
user4 = {'1-1101-32221-12-0':['Nani Potter','010101','12345',20000]}
user5 = {'1-1101-32221-12-0':['Nani Potter','010201','12346',20000]}
user6 = {'1-1101-32221-12-0':['Nani Potter']}
atm ={'1001':1000000,'1002':200000}

# kanyok_bank.add_user(User("1-1101-12345-12-0", "Harry Potter"))
# kanyok_bank.user_list[0].add_account(Account(Card("12345"),2000))

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

def create_instance(bank_id):
    bank = Bank(bank_id)
    print(bank.add_data(user,atm))
    # print(bank.add_data(user6,atm))
    # print(bank.add_data(user6,atm))
    # print(bank.add_data(user6,atm))
    # print(bank.add_data(user6,atm))
    # print(bank.add_data(user6,atm))
    return bank
my_bank = create_instance("101")

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
        print(my_bank.atm_list[0].insert_card(bank, card_id, pin).id, my_bank.atm_list[0].insert_card(bank, card_id, pin).card.id, "Success")
    else:
        print("Error")
testcase_1_pin = None
testcase_1(my_bank, "12345" , testcase_1_pin)
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