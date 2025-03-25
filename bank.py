import datetime as d
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="91221",
    database="bank"
)
mycursor = conn.cursor()


class Bank:
    B_name = "Axis bank"
    ROI = 0.05

    def checkCust(number, pin):
        sql = f"SELECT cust_id FROM customer where phno={number} and pin='{pin}'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()[0]
        return myresult
    conn.commit()

    def Create_new_account():

        name = input("Enter ur name : ")
        email = input("Enter ur mail id : ")
        age = int(input("Enter ur age : "))
        phno = input("Enter ur phone: ")
        address = input("Enter ur address : ")
        pin = int(input("set ur pin : "))
        balance = int(input("Enter ur initial amount : "))
        print()

        sql = f"insert into customer(cust_name, email_id, age, phno, address, pin, balance) values('{name}', '{email}', '{age}', '{phno}', '{address }', '{pin}', '{balance}')"
        mycursor.execute(sql)
        conn.commit()
        print("*-"*50)
        print(f"Hello {name} Congratulations !, your account is created successfully !!!")
        print("*-"*50)
        print()

    def deposit(id):

        sql_name = f"select cust_name from customer where cust_id={id} "
        mycursor.execute(sql_name)
        name = mycursor.fetchone()[0]
        de_amt = int(input("Enter how much amount u want to deposit : "))
        trans_type = "deposit"
        sql1 = f"insert into transactions values('{id}','{name}','{de_amt}','{trans_type}','{str(d.datetime.now())}')"
        mycursor.execute(sql1)

        sql_bal = f"select balance from customer where cust_id={id} "
        mycursor.execute(sql_bal)
        balance = mycursor.fetchone()[0]

        balance = balance + de_amt
        sql2 = f"update customer set balance={balance} where cust_id={id}"
        mycursor.execute(sql2)
        conn.commit()
        print("-"*80)
        print(f"Transaction completed, Rs.{de_amt} deposited successfully in your account !!")
        print("-"*80)
        print("\n")

    def withdraw(id):

        sql_name = f"select cust_name from customer where cust_id={id} "
        mycursor.execute(sql_name)
        name = mycursor.fetchone()[0]

        wi_amt = int(input("Enter how much amount u want to withdraw : "))
        trans_type = "withdraw"
        sql1 = f"insert into transactions values('{id}','{name}','{wi_amt}','{trans_type}','{str(d.datetime.now())}')"
        mycursor.execute(sql1)

        sql_bal = f"select balance from customer where cust_id={id} "
        mycursor.execute(sql_bal)
        balance = mycursor.fetchone()[0]

        if balance >= wi_amt:

            balance = balance - wi_amt
            sql2 = f"update customer set balance={balance} where cust_id={id}"
            mycursor.execute(sql2)
            conn.commit()
            print("-"*70)
            print(
                f"Transaction completed, Rs.{wi_amt} withdraw successfully in your account !!")
            print("-"*80)
            print("\n")
        else:
            print("-"*70)
            print(
                f"insufficeint Balance!! , {name} your available balance is : {balance}")
            print("-"*70)
            print("\n")

    def checkbalance(id):

        sql_name = f"select cust_name from customer where cust_id={id} "
        mycursor.execute(sql_name)
        name = mycursor.fetchone()[0]

        sql = f"select balance from customer where cust_id={id}"
        mycursor.execute(sql)
        balance = mycursor.fetchone()[0]
        conn.commit()
        print("-"*70)
        print(f" {name} your availabe Account Balance : {balance}")
        print("-"*70)
        print("\n")
        # return balance

    def Modify_account(id):

        while True:
            print("*"*100)
            print("  What do you want to change : ")
            print("-"*100)
            print("1.customer name")
            print("2.age")
            print("3.phone number")
            print("4.Address")
            print("5.pin")
            print("6.exit")
            print("\n")

            option = int(input("Enter your option : "))

            field_name = ''

            if option == 1:

                field_name = "cust_name"
                new_data = input("Enter new value : ")
                sql_name = f"select cust_name from customer where cust_id={id} "
                mycursor.execute(sql_name)
                name = mycursor.fetchone()[0]
                sql = 'update customer set ' + field_name + '="' + \
                    new_data + '" where cust_id='+str(id)+';'
                mycursor.execute(sql)
                print("-"*50)
                print("Name updated Successfully !!")
                print(f"initial name : {name} updated name : {new_data}")
                print("="*50)
                print("\n")
                conn.commit()

            elif option == 2:

                field_name = "age"
                new_data = input("Enter new value : ")
                sql_age = f"select age from customer where cust_id={id} "
                mycursor.execute(sql_age)
                age = mycursor.fetchone()[0]
                sql = 'update customer set ' + field_name + '="' + \
                    new_data + '" where cust_id='+str(id)+';'
                mycursor.execute(sql)
                print("-"*50)
                print("age updated Successfully !!")
                print(f"initial age : {age} updated age : {new_data}")
                print("="*50)
                print("\n")
                conn.commit()

            elif option == 3:

                field_name = "phno"
                new_data = input("Enter new value : ")
                sql_phone = f"select phno from customer where cust_id={id} "
                mycursor.execute(sql_phone)
                phone = mycursor.fetchone()[0]
                sql = 'update customer set ' + field_name + '="' + \
                    new_data + '" where cust_id='+str(id)+';'
                mycursor.execute(sql)
                print("-"*50)
                print("Phone number updated Successfully !!")
                print(
                    f"initial phone number : {phone} updated phone number : {new_data}")
                print("="*50)
                print("\n")
                conn.commit()

            elif option == 4:

                field_name = "address"
                new_data = input("Enter new value : ")
                sql_address = f"select address from customer where cust_id={id} "
                mycursor.execute(sql_address)
                address = mycursor.fetchone()[0]
                sql = 'update customer set ' + field_name + '="' + \
                    new_data + '" where cust_id='+str(id)+';'
                mycursor.execute(sql)
                print("-"*50)
                print("customer address is updated Successfully !!")
                print(
                    f"initial Address : {address} updated Address : {new_data}")
                print("="*50)
                print("\n")
                conn.commit()

            elif option == 5:

                field_name = "pin"
                new_data = input("Enter new value : ")
                sql_pin = f"select pin from customer where cust_id={id} "
                mycursor.execute(sql_pin)
                pin = mycursor.fetchone()[0]
                sql = 'update customer set ' + field_name + '="' + \
                    new_data + '" where cust_id='+str(id)+';'
                mycursor.execute(sql)
                print("-"*50)
                print("pin number is updated Successfully !!")
                print(f"initial pin : {pin} updated pin : {new_data}")
                print("="*50)
                print("\n")
                conn.commit()

            elif option == 6:
                break

            else:
                print("-"*50)
                print("Invalid option !!, select a valid option !!!")
                print("="*50)
                

    def Customer_details(id):

        sql1 = f"select * from customer where cust_id={id}"
        mycursor.execute(sql1)
        details = mycursor.fetchall()[0]
        conn.commit()

        a = list(details)
        print("*-"*40)
        print("Customer Name            : "+a[1])
        print("customer email id        : "+a[2])
        print("Customer age             :", a[3])
        print("Customer phone number    :", a[4])
        print("Customer address         : "+a[5])
        print("Customer pin             :", a[6])
        print("Customer Account balance :", a[7])
        print("*-"*40)
        print("\n")

    def close_account(id):
        sql1 = f" select cust_name from customer where cust_id={id}"
        mycursor.execute(sql1)
        my_result = mycursor.fetchone()[0]
        sql2 = f"delete from customer where cust_id={id}"
        mycursor.execute(sql2)
        conn.commit()
        print("-"*70)
        print(f"{my_result} your account was closed Successfully")
        print("-"*70)
        print("\n")


while True:

    print("-"*100)
    print(
        f"     ----------================   Welcome to {Bank.B_name} !!!  ================--------------")
    print("-"*100)
    print("*******----- Menu ------*******\n")
    print("1.Create New account")
    print("2.deposit")
    print("3.withdraw")
    print("4.check balance")
    print("5.Modify Account")
    print("6.customer details")
    print("7.close account")
    print("8.Exit")
    print("\n")
    print("="*100)

    choice = int(input("Enter which operation u want to perform : "))
    print()

    if choice == 1:

        Bank.Create_new_account()

    elif choice == 2:

        phno = input("Enter ur phone number : ")
        pin = int(input("Enter your pin : "))
        print()
        id = Bank.checkCust(phno, pin)
        Bank.deposit(id)

    elif choice == 3:

        phno = input("Enter ur phone number : ")
        pin = int(input("Enter your pin : "))
        print()
        id = Bank.checkCust(phno, pin)
        Bank.withdraw(id)

    elif choice == 4:

        phno = input("Enter ur phone number : ")
        pin = int(input("Enter your pin : "))
        print()
        id = Bank.checkCust(phno, pin)
        Bank.checkbalance(id)

    elif choice == 5:

        phno = input("Enter ur phone number : ")
        pin = int(input("Enter your pin : "))
        print()
        id = Bank.checkCust(phno, pin)
        Bank.Modify_account(id)

    elif choice == 6:

        phno = input("Enter ur phone number : ")
        pin = int(input("Enter your pin : "))
        print()
        id = Bank.checkCust(phno, pin)
        Bank.Customer_details(id)

    elif choice == 7:

        phno = input("Enter ur phone number : ")
        pin = int(input("Enter your pin : "))
        print()
        id = Bank.checkCust(phno, pin)
        Bank.close_account(id)

    elif choice == 8:
        break

    else:
        print("Invalid choice !! , Choose anyone above option")
