import mysql.connector
db=mysql.connector.connect(host='localhost',
                           user='root',
                           passwd='**Your Password**',
                           database='cyber_cafe')
cursor=db.cursor()


# Checking E-mail Validity 

def check_email(email_address, characters, min_length=6):
    while True:
        for character in characters:
            if character not in email_address:
                email_address = input("Your email address must have '{}' in it\nPlease write your email address again : ".format(character))
                continue
        if len(email_address) <= min_length:
            email_address = input("Your email address is too short\nPlease write your email address again : ")
            continue
        cursor.execute('SELECT email_address FROM customer_details WHERE email_address= %s', (email_address,))
        checkemail=cursor.fetchall()
        if len(checkemail)!=0:
            email_address = input("Email address Already Exists!\nPlease write your email address again : ")
            continue
        return email_address

# Checking Mobile Number Validity

def check_mob(mob_number):
    num='12345'
    while ((len(mob_number))!=10) or ((mob_number[0]) in num):
        print("**Invalid Mobile Number! Please Check and Enter Again!**")
        print()
        mob_number=input('Enter Mobile Number Again : ')
    return mob_number

# Adding Customer to the Database

def add_customer():
    name_cust=input('Enter Name of Customer : ')
    mob_cust=input('Enter Customer Mobile Number : ')
    mob_cust=check_mob(mob_cust)
    email_cust=input('Enter Email Id : ')
    email_cust=check_email(email_cust,'@.')
    addr_cust=input('Enter Customer Address : ')
    dur_cust=float(input('Enter Shift Duration of Customer ( in Hours ) : '))
    comp=int(input('Enter Computer no. of Customer : '))
    if dur_cust<=1:
        price_cust=40
    else:
        price_cust=round(dur_cust*40,2)
    cursor.execute("INSERT INTO customer_details (name,mobile_number,email_address,Address,Duration_in_hrs,Computer_number,Price,date_time) VALUES (%s,%s,%s,%s,%s,%s,%s,NOW())",(name_cust,mob_cust,email_cust,addr_cust,dur_cust,comp,price_cust))
    db.commit()
    print("CUSTOMER RECORD ADDED SUCCESSFULLY!")

# Searching For A Customer

def customer_detail():
    name_search=input('Enter Name Of Customer You Want To Search : ')
    mob_search=input('Enter Mobile Number of Customer You Want to Search : ')
    mob_search=check_mob(mob_search)
    cursor.execute('SELECT * FROM customer_details WHERE name=(%s) AND mobile_number=(%s)',(name_search,mob_search))
    title_cust=('Id','Name','Mobile number','Email Address','Address','Duration(in hrs)','Computer number','Price','Date and Time')
    detail=cursor.fetchone()
    try:
        if (len(detail))!=0:
            for i in range(len(detail)):
                print()
                print(title_cust[i],' :-: ',detail[i])
    except:
        print()
        print('**NO RECORD FOUND!**')

# Fetching All Customers Details

def show_all():
    title_cust=('Id','Name','Mobile number','Email Address','Address','Duration(in hrs)','Computer number','Price','Date and Time')
    cursor.execute('SELECT * FROM customer_details')
    result=cursor.fetchall()
    for i in result:
        for j in range(len(i)):
            print(title_cust[j],  ':-:'  ,i[j])
        print()
        print('**********************************')

# Deleting a Customer Record

def delete_customer():
    name_delete=input("Enter Name of Customer to delete his record : ")
    mob_delete=input("Enter Mobile number : ")
    mob_delete=check_mob(mob_delete)
    cursor.execute('SELECT * FROM customer_details')
    delete_check=cursor.fetchall()
    f=''
    for i in delete_check:
        if mob_delete in i:
            f=i
    if len(f)!=0:
        cursor.execute('DELETE FROM customer_details WHERE name=%s AND mobile_number=%s',(name_delete,mob_delete))
        db.commit()
        print("CUSTOMER RECORD DELETED SUCCESSFULLY!")
    else:
        print('**NO RECORD FOUND WITH THIS NUMBER!**')

# Editing a Customer Record

def edit_customer():
    mob_edit=input("Enter Mobile Number Of Customer You Want To Edit : ")
    mob_edit=check_mob(mob_edit)
    cursor.execute('SELECT * FROM customer_details')
    check=cursor.fetchall()
    f=''
    for i in check:
        if mob_edit in i:
            f=i
    if len(f)!=0:
        var=input('What You Want To Edit ( NAME//MOBILE NUMBER//EMAIL//ADDRESS//DURATION//COMPUTER NUMBER )? : ')
        lst=['NAME','MOBILE NUMBER','EMAIL','ADDRESS','DURATION','COMPUTER NUMBER']
        while (var.upper()) not in lst:
            print()
            print('**Invalid Input! Please give Input from given options!**')
            print()
            var=input('What You Want To Edit ( NAME//MOBILE NUMBER//EMAIL//ADDRESS//DURATION//COMPUTER NUMBER )? : ')
        else:
            if var.upper()=="NAME":
                new_name=input("Enter New Name : ")
                cursor.execute('UPDATE customer_details SET name=%s WHERE mobile_number=%s',(new_name,mob_edit))
                db.commit()
                print('CUSTOMER RECORD EDITED SUCCESSFULLY!')
            elif var.upper()=="MOBILE NUMBER":
                new_mob=input("Enter New Mobile Number : ")
                new_mob=(check_mob(new_mob))
                cursor.execute('UPDATE customer_details SET mobile_number=%s WHERE mobile_number=%s',(new_mob,mob_edit))
                db.commit()
                print('CUSTOMER RECORD EDITED SUCCESSFULLY!')
            elif var.upper()=="EMAIL":
                new_email=input("Enter New Email : ")
                cursor.execute('UPDATE customer_details SET email_address=%s WHERE mobile_number=%s',(new_email,mob_edit))
                db.commit()
                print('CUSTOMER RECORD EDITED SUCCESSFULLY!')
            elif var.upper()=="ADDRESS":
                new_addr=input("Enter New Address : ")
                cursor.execute('UPDATE customer_details SET Address=%s WHERE mobile_number=%s',(new_addr,mob_edit))
                db.commit()
                print('CUSTOMER RECORD EDITED SUCCESSFULLY!')
            elif var.upper()=="DURATION":
                new_dur=float(input("Enter New Duration (in hrs) : "))
                new_price=round((new_dur*40),2)
                cursor.execute('UPDATE customer_details SET Duration_in_hrs=%s WHERE mobile_number=%s',(new_dur,mob_edit))
                cursor.execute('UPDATE customer_details SET Price=%s WHERE mobile_number=%s',(new_price,mob_edit))
                db.commit()
                print('CUSTOMER RECORD EDITED SUCCESSFULLY!')
            elif var.upper()=="COMPUTER NUMBER":
                new_comp=input("Enter New Computer number : ")
                cursor.execute('UPDATE customer_details SET Computer_number=%s WHERE mobile_number=%s',(new_comp,mob_edit))
                db.commit()
                print('CUSTOMER RECORD EDITED SUCCESSFULLY!')
    else:
        print()
        print("**NO RECORD FOUND WITH THIS MOBILE NUMBER!**")


# MANAGING COMPUTERS



# Adding Computer in the Database

def add_computer():
    name_comp=input("Enter the Name of Computer : ")
    com_comp=input("Enter the Name of Company of Computer : ")
    type_comp=input("Enter the Type of Computer : ")
    model_comp=input("Enter Model Number of Computer : ")
    ram_comp=input("Enter RAM of Computer : ")
    price_comp=input("Enter the Price of Computer : ")
    cursor.execute('INSERT INTO computer_details (name,company,type,model_no,RAM,Price,Date_Time) VALUES (%s,%s,%s,%s,%s,%s,NOW())',(name_comp,com_comp,type_comp,model_comp,ram_comp,price_comp))
    db.commit()
    print("COMPUTER RECORD ADDED SUCCESSFULLY")

# Searching For a Computer

def computer_detail():
    com_sear=input("Enter Company of Computer you want to Search : ")
    model_sear=input("Enter Model Number of Computer you want to Search : ")
    cursor.execute('SELECT * FROM computer_details WHERE company=(%s) AND model_no=(%s)',(com_sear,model_sear))
    title=('Id','Name','Company','Type','Model_no','RAM','Price','Date_Time')
    detail_comp=cursor.fetchone()
    try:
        if (len(detail_comp))!=0:
            for i in range(len(detail_comp)):
                print()
                print(title[i],' :-: ',detail_comp[i])
    except:
        print('**NO RECORD FOUND!**')

# Fetching Details of All Computers

def show_all_comp():
    cursor.execute('SELECT * FROM computer_details')
    res=cursor.fetchall()
    title=('Id','Name','Company','Type','Model_no','RAM','Price','Date_Time')
    for i in res:
        for j in range(len(i)):
            print(title[j],'  :-:  ',i[j])
        print()
        print("*******************************")

# Deleting a Computer Record

def delete_computer():
    name_comp_delete=input("Enter Name of Computer to delete its record : ")
    com_delete=input("Enter Company of Computer : ")
    cursor.execute("SELECT * FROM computer_details")
    delete_comp=cursor.fetchall()
    f=''
    for i in delete_comp:
        if (name_comp_delete in i) and (com_delete in i):
            f=i
    if len(f)!=0:
        cursor.execute("DELETE FROM computer_details WHERE name=(%s) AND company=(%s)",(name_comp_delete,com_delete))
        db.commit()
        print("COMPUTER RECORD DELETED SUCCESSFULLY!")
    else:
        print('**NO RECORD FOUND!**')

# Editing a Computer Record

def edit_computer():
    name_comp_edit=input("Enter Name Of Computer You Want To Edit : ")
    cursor.execute('SELECT * FROM computer_details')
    check=cursor.fetchall()
    f=''
    for i in check:
        if name_comp_edit in i:
            f=i
    if len(f)!=0:
        var_comp=input('What You Want To Edit ( NAME//COMPANY//TYPE//MODEL//RAM//PRICE )? : ')
        lst=['NAME','COMPANY','TYPE','MODEL','RAM','PRICE']
        while (var_comp.upper()) not in lst:
            print()
            print('**Invalid Input! Please give Input from given options!**')
            print()
            var_comp=input('What You Want To Edit ( NAME//COMPANY//TYPE//MODEL//RAM//PRICE )? : ')
        else:
            if var_comp.upper()=="NAME":
                new_name=input("Enter New Name : ")
                cursor.execute('UPDATE computer_details SET name=%s WHERE name=%s',(new_name,name_comp_edit))
                db.commit()
                print('COMPUTER RECORD EDITED SUCCESSFULLY!')
            elif var_comp.upper()=="COMPANY":
                new_com=input("Enter New Company : ")
                cursor.execute('UPDATE computer_details SET company=%s WHERE name=%s',(new_com,name_comp_edit))
                db.commit()
                print('COMPUTER RECORD EDITED SUCCESSFULLY!')
            elif var_comp.upper()=="TYPE":
                new_type=input("Enter New Computer Type : ")
                cursor.execute('UPDATE computer_details SET type=%s WHERE name=%s',(new_type,name_comp_edit))
                db.commit()
                print('COMPUTER RECORD EDITED SUCCESSFULLY!')
            elif var_comp.upper()=="MODEL":
                new_model=input("Enter New Model Number : ")
                cursor.execute('UPDATE computer_details SET model_no=%s WHERE name=%s',(new_model,name_comp_edit))
                db.commit()
                print('COMPUTER RECORD EDITED SUCCESSFULLY!')
            elif var_comp.upper()=="RAM":
                new_ram=input("Enter New RAM : ")
                cursor.execute('UPDATE computer_details SET RAM=%s WHERE name=%s',(new_ram,name_comp_edit))
                db.commit()
                print('COMPUTER RECORD EDITED SUCCESSFULLY!')
            elif var_comp.upper()=="PRICE":
                new_comp_price=input("Enter New Price : ")
                cursor.execute('UPDATE computer_details SET price=%s WHERE name=%s',(new_comp_price,name_comp_edit))
                db.commit()
                print('COMPUTER RECORD EDITED SUCCESSFULLY!')
    else:
        print()
        print('**NO RECORD FOUND!**')


#########################################################
##CREATING TWO TABLES FOR CUSTOMER AND COMPUTER RECORDS##
#########################################################


cursor.execute('CREATE TABLE IF NOT EXISTS customer_details (Id int(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,Name varchar(30) NOT NULL,Mobile_Number varchar(15) NOT NULL,Email_Address varchar(320),Address varchar(50),Duration_in_hrs int(4),Computer_number int(2),Price decimal(10,2),Date_Time DATETIME)')
cursor.execute('CREATE TABLE IF NOT EXISTS computer_details (Id int(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,Name varchar(30) NOT NULL,Company varchar(20) NOT NULL,Type varchar(20),Model_no varchar(20),RAM varchar(7),Price decimal(10,2),Date_Time DATETIME)')
db.commit()

print('''
#####################################################################################################################
##########                               CYBER_CAFE MANAGEMENT SYSTEM                                      ##########
#####################################################################################################################
***************************************************WELCOME***********************************************************''')
print()
a=0
while a!=1:
    print()
    print("**********Choose One Option to do any Task**************")
    print()
    print('''
              1-> MANAGE CUSTOMER
              2-> MANAGE COMPUTER
              3-> EXIT''')
    print()
    manage=input('Enter 1/2/3 to choose one from above : ')
    while (manage!='1') and (manage!='2') and (manage!='3'):
        print()
        print("**Invalid Input! Please give input Correctly ! Try Again !**")
        print()
        print('''
                  1-> MANAGE CUSTOMER
                  2-> MANAGE COMPUTER
                  3-> EXIT''')
        manage=input('Enter 1/2/3 to choose one from above : ')
    else:
        if manage=='1':
            a=0
            while a!=2:
                print('''****************MANAGE CUSTOMERS****************

                          1-> To Add Customer.
                          2-> To Search Customer.
                          3-> To Edit Customer Record.
                          4-> To Delete Customer Record.
                          5-> To Show All Customer.
                          6-> To Go to Main Menu.''')
                print()
                ch=input('Enter 1/2/3/4/5/6 to Choose from above : ')
                num='123456'
                while ch not in num:
                    print("**Invalid Input! Please give input Correctly ! Try Again !**")
                    print()
                    ch=input('Enter 1/2/3/4/5/6 to Choose from above : ')
                    print()
                else:
                    if ch=='1':
                        add_customer()
                        print()
                        b=input('Press "Enter" to continue or enter "add" to Add Customer again.... : ')
                        while (b.upper()!='ADD') and (b!=''):
                            print('Invalid Input! Please Enter again!')
                            print()
                            b=input('Press "Enter" to continue or enter "add" to Add Customer again.... : ')
                        else:
                            while b.upper()=='ADD':
                                add_customer()
                                print()
                                b=input('Press "Enter" to continue or enter "add" to Add Customer again.... : ')
                                print()
                            else:
                                continue

                    elif ch=='2':
                        customer_detail()
                        print()
                        b=input('Press "Enter" to continue or enter "detail" to search another Customer.... : ')
                        while (b.upper()!='DETAIL') and (b!=''):
                            print('Invalid Input! Please Enter again!')
                            print()
                            b=input('Press "Enter" to continue or enter "detail" to search another Customer.... : ')
                        else:
                            while b.upper()=='DETAIL':
                                customer_detail()
                                print()
                                b=input('Press "Enter" to continue or enter "detail" to search another Customer.... : ')
                                print()
                            else:
                                continue

                    elif ch=='3':
                        edit_customer()
                        print()
                        b=input('Press "Enter" to continue or enter "edit" to edit another Customer.... : ')
                        while (b.upper()!='EDIT') and (b!=''):
                            print('Invalid Input! Please Enter again!')
                            print()
                            b=input('Press Enter to continue or enter "edit" to edit another Customer.... : ')
                        else:
                            while b.upper()=='EDIT':
                                edit_customer()
                                print()
                                b=input('Press Enter to continue or enter "edit" to edit another Customer.... : ')
                                print()
                            else:
                                continue

                    elif ch=='4':
                        delete_customer()
                        print()
                        b=input('Press "Enter" to continue or enter "delete" to delete another Customer record.... : ')
                        while (b.upper()!='DELETE') and (b!=''):
                            print('Invalid Input! Please Enter again!')
                            print()
                            b=input('Press "Enter" to continue or enter "delete" to delete another Customer record.... : ')
                        else:
                            while b.upper()=='DELETE':
                                delete_customer()
                                print()
                                b=input('Press "Enter" to continue or enter "delete" to delete another Customer record.... : ')
                                print()
                            else:
                                continue

                    elif ch=='5':
                        show_all()
                        b=input('Press "Enter" to continue....')
                        print()
                        print()

                    elif ch=='6':
                        a=2
        elif manage=='2':
            a=0
            while a!=2:
                print('''****************MANAGE COMPUTERS****************

                          1-> To Add Computer.
                          2-> To Search Computer.
                          3-> To Edit Computer Record.
                          4-> To Delete Computer Record.
                          5-> To Show All Computer.
                          6-> To Go to Main Menu.''')
                print()
                ch=input('Enter 1/2/3/4/5/6 to Choose from above : ')
                num='123456'
                while ch not in num:
                    print("**Invalid Input! Please give input Correctly ! Try Again !**")
                    print()
                    ch=input('Enter 1/2/3/4/5/6 to Choose from above : ')
                    print()
                else:
                    if ch=='1':
                        add_computer()
                        print()
                        b=input('Press "Enter" to continue or enter "add" to Add Computer again.... : ')
                        while (b.upper()!='ADD') and (b!=''):
                            print('Invalid Input! Please Enter again!')
                            print()
                            b=input('Press "Enter" to continue or enter "add" to Add Computer again.... : ')
                        else:
                            while b.upper()=='ADD':
                                add_computer()
                                print()
                                b=input('Press "Enter" to continue or enter "add" to Add Computer again.... : ')
                                print()
                            else:
                                continue

                    elif ch=='2':
                        computer_detail()
                        print()
                        b=input('Press "Enter" to continue or enter "detail" to search another Computer.... : ')
                        while (b.upper()!='DETAIL') and (b!=''):
                            print('Invalid Input! Please Enter again!')
                            print()
                            b=input('Press "Enter" to continue or enter "detail" to search another Computer.... : ')
                        else:
                            while b.upper()=='DETAIL':
                                computer_detail()
                                print()
                                b=input('Press "Enter" to continue or enter "detail" to search another Computer.... : ')
                                print()
                            else:
                                continue

                    elif ch=='3':
                        edit_computer()
                        print()
                        b=input('Press "Enter" to continue or enter "edit" to edit another Computer.... : ')
                        while (b.upper()!='EDIT') and (b!=''):
                            print('Invalid Input! Please Enter again!')
                            print()
                            b=input('Press "Enter" to continue or enter "edit" to edit another Computer.... : ')
                        else:
                            while b.upper()=='EDIT':
                                edit_computer()
                                print()
                                b=input('Press Enter to continue or enter "edit" to edit another Computer.... : ')
                                print()
                            else:
                                continue

                    elif ch=='4':
                        delete_computer()
                        print()
                        b=input('Press "Enter" to continue or enter "delete" to delete another Computer record.... : ')
                        while (b.upper()!='DELETE') and (b!=''):
                            print('Invalid Input! Please Enter again!')
                            print()
                            b=input('Press "Enter" to continue or enter "delete" to delete another Computer record.... : ')
                        else:
                            while b.upper()=='DELETE':
                                delete_computer()
                                print()
                                b=input('Press "Enter" to continue or enter "delete" to delete another Computer record.... : ')
                                print()
                            else:
                                continue

                    elif ch=='5':
                        show_all_comp()
                        b=input('Press "Enter" to continue....')
                        print()
                        print()

                    elif ch=='6':
                        a=2    
        elif manage=='3':
            print()
            print("THANKYOU FOR USING OUR SERVICE :) HAVE A NICE DAY !")
            a=1
