import mysql.connector as db
import random
conn=db.connect(
    host='localhost',
    user='root',
    password='SLavanya@123',
    database='cognizant'
    )
cursor=conn.cursor()
print("connected successfully")
while True:
    print("1.Admin")
    print("2.user")
    print("3.exit")
    ch=int(input("enter (user or admin or exit):"))
    if ch==1:
        a_user=input("enter username:")
        password=int(input("enter password:"))
        if a_user=='sl67' and password==6776:
            while True:
                print("1.view all users")
                print("2.view complete account details of particular user")
                print("3.view complete transactions of particular user")
                print("4.view complete transactions of particular day")
                print("5.exit")
                op=int(input("choose one option:"))
                if op==1:
                   cursor.execute('select * from users3')
                   data=cursor.fetchall()
                   for i in data:
                       print(i)
                       print()
                if op==2:
                    a_num=input("enter account number:")
                    cursor.execute('select * from users3 where account_number=%s',(a_num,))
                    data=cursor.fetchall()
                    if not data:
                        print("no user found with this account")
                    else:
                      for i in data:
                        print(i)
                        print()
                if op==3:
                   a_num=input("enter account number:")
                   cursor.execute('select * from transactions1 where account_number=%s',(a_num,))
                   data=cursor.fetchall()
                   if not data:
                       print("No transctions found with this account")
                   else:
                    for i in data:
                       print(i)
                       print()
                if op==4:
                  d=input('enter date')
                  cursor.execute('select * from transactions1 where date(t_time)=%s',(d,))
                  data=cursor.fetchall()
                  for i in data:
                      a=i[0]
                      am=i[1]
                      t=i[2]
                      t_t=i[3]
                      print(a,'-',am,'-',t,'-',t_t)
                      print()
                if op==5:
                    break
                      
                  
                   
                
    elif ch==2:
        while True:
            print("1.new user")
            print("2.existing user")
            print("3.exit")

            first=int(input("new user or exisiting user:"))
            if first==3:
                break
            if first==1:
                name=input("enter your name:")
                while True:
                    mobile_number=input("enter your mobile number:")
                    if len(mobile_number)==10 and (mobile_number[0]=='9' or mobile_number[0]=='8' or mobile_number[0]=='7' or mobile_number[0]=='6'):
                        print("valid phone number")
                        break
                    else:
                        print("invalid mobile number ")
                while True:
                    adhar_no=input("enter adhar number:")
                    if len(adhar_no)==12:
                        print("adhar number is valid")
                        break
                    else:
                        print("invalid adhar number enter again")
                while True:
                    pin=input("create your pin:")
                    if len(pin)==4:
                        print("valid pin")
                        break
                    else:
                        print("generate another pin")
                amount=int(input("enter amount:"))
                account_number = str(random.randint(1000000000, 9999999999))
                print("your account number is:",account_number)
                cursor.execute('''insert into users3(user_name,mobile_number,adhar_no,pin,account_number,amount)
               values(%s,%s,%s,%s,%s,%s)''',(name,mobile_number,adhar_no,pin,account_number,amount))
                conn.commit()
                print("user register successfully")
                
            while True:
                acc_num=input("enter account number:")
                pin_login=input("enter pin:")
                cursor.execute("select account_number,pin from users3 where account_number=%s",(acc_num,))
                data=cursor.fetchone()
                if data and data[0]==acc_num and data[1]==pin_login:
                    print("Login successfully")
                    first=2
                    break
                else:
                    print("login again")
                    
            
            if first==2:
                while True:          
                    print("1.view account details")
                    print("2.debit amount")
                    print("3.credit amount")
                    print("4.pin change")
                    print("5.statement")
                    print("6.exit")
                    user_option=int(input("enter option:"))
                    if user_option==1:
                        acc_number=input('enter account number:')
                        cursor.execute('select * from users3 where account_number=%s',(acc_number,))
                        user=cursor.fetchone()
                        print(user)
                    if user_option==2:
                        a_num=input("enter account number:")
                        p=input("enter your pin:")
                        cursor.execute('select amount,pin from users3 where account_number=%s',(a_num,))
                        data=cursor.fetchone()
                        amount,p1=data
                        if p1==p:
                            a=int(input("enter how many you want to withdraw:"))
                            if amount>a:
                                amount=amount-a
                                print("amount debited successfully")
                                cursor.execute('update users3 set amount=%s where account_number=%s',(amount,a_num))
                                cursor.execute("insert into transactions1(account_number,amount,type,t_time) values(%s,%s,'debit',now())",(a_num,amount))
                                conn.commit()

                            else:
                                print("Insufficient balance")
                        else:
                            print("you entered wrong pin")
                                
                        cursor.execute('update transactions1 set amount=%s where account_number=%s',(amount,a_num))

                    if user_option==3:
                        a_num=input("enter your account number:")
                        p=input("enter your pin:")
                        cursor.execute("select amount,pin from users3 where account_number=%s",(a_num,))
                        data=cursor.fetchone()
                        amount,p1=data
                        if p1==p:
                            a=int(input("enter amount to credit:"))
                            amount=amount+a
                            print("amount credited successfully")
                            cursor.execute('update users3 set amount=%s where account_number=%s',(amount,a_num))
                            cursor.execute("insert into transactions1(account_number,amount,type,t_time) values(%s,%s,'credit',now())",(a_num,amount))
                        else:
                            print("you entered wrong number")
                    if user_option==4:
                       a_num=input("enter account number:")
                       p=input("enter your pin:")
                       cursor.execute("select pin from users3 where account_number=%s",(a_num,))
                       data=cursor.fetchone()
                       p1=data[0]
                       if p==p1:
                           pin1=input("enter new pin:")
                           if len(pin1)==4:
                               print("pin updated successfully")
                               cursor.execute('update users3 set pin=%s where account_number=%s',(pin1,a_num))
                           else:
                               print("you entered wrong pin")
                    
                    if user_option==5:
                        a_num=input("enter your account number:")
                        p=input("enter your pin")
                        cursor.execute('select pin from users3 where account_number=%s',(a_num,))
                        data=cursor.fetchone()
                        p1=data[0]
                        if p==p1:
                            cursor.execute('select amount,type,t_time from transactions1 where account_number=%s',(a_num,))
                            s=cursor.fetchall()
                            for i in s:
                               amount=i[0]
                               t=i[1]
                               time=i[2]
                               print(amount,'-',t,'-',time)
                               print()
                               
                   
                    if user_option==6:
                        break
    elif ch==3:
        break
                
               
                
            
