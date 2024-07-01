import mysql.connector as mycon
import datetime
#from List import listfn
cn = mycon.connect(host='localhost',user='root',password="12345678",database="projecs")
cur = cn.cursor()
def getlist():
    global cn,cur
    print("\n*******************GET LIST**************************")
    cl = int(input("Enter the name of class: "))
    query="select * from stu where class="+str(cl)
    #cour = input("Enter course: ")
    #query="select * from stu where course="+'cour'
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\n *****SORRY! NO MATCHING DETAILS AVAILABLE*****")
    else:
        print("\n**************************************************")
        print('%5s'%"ID",'%15s'%'STUDENT NAME','%12s'%'ADDRESS','%10s'%'PHONE')
        print("\n**************************************************")
        count=0
        for row in results:
            print('%5s' % row[0],'%12s'%row[1],'%12s'%row[2],'%13s'%row[3])
            count+=1
        print("\n*************** TOTAL RECORD:",count,"**************") 
def showall():
    global cn
    global cur
    try:
        query="select * from stu"
        cur.execute(query)
        results = cur.fetchall()
        print("\n***********************************************************************************")
        print('%5s'%"ID",'%15s'%'STUDENT NAME','%12s'%'ADDRESS','%11s'%'PHONE','%11s'%'CLASS','%11s'%'COURSE')
        print("\n***********************************************************************************")
        count=0
        for row in results:
            print('%5s' % row[0],'%19s'%row[1].ljust(15),'%10s'%row[2].ljust(10),'%10s'%row[3],'%8s'%row[4],'%15s'%row[5].ljust(10))
            count+=1
        print("\n**************************** TOTAL RECORD:",count,"**************************************")
    except:
        print("error")
        
def showAll():
    global cn
    global cur
    try:
        query="select * from courses"
        cur.execute(query)
        results = cur.fetchall()
        print("\n**************************************************")
        print('%5s'%"SN.",'%7s'%'CLASS','%17s'%'COURSE NAME','%12s'%'FEE')
        print("\n**************************************************")
        count=0
        for row in results:
            print('%5s' %row[0],'%7s'%row[1],'%25s'%row[2].ljust(22),'%11s'%row[3].ljust(10))
            count+=1
        print("\n*************** TOTAL RECORD:",count,"**************")
    except:
        print("error")
        
def addstu():
    global cn,cur
    print("\n*******************ADD NEW STUDENT**************************")
    ID = int(input("Enter student ID: "))
    sn = input("Enter student name: ")
    ad = input("Enter address: ")
    ph = int(input("Enter phone no.: "))
    cls = int(input("Enter class: "))
    cour = input("Enter course: ") 
    query="insert into stu values("+str(ID)+",'"+sn+"','"+ad+"',"+str(ph)+","+str(cls)+",'"+cour+"')"
    cur.execute(query)
    cn.commit()
    print("\n *****RECORD ADDED SUCCESSFULLY!*****")
    
def searchstu():
    global cn,cur
    print("\n*******************SEARCH STUDENT FORM **************************")
    ID = int(input("Enter student ID to be searched: "))
    query="select * from stu where ID="+str(ID)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\n *****SORRY! NO MATCHING DETAILS AVAILABLE*****")
    else:
        print("\n**************************************************")
        print('%5s'%"ID",'%15s'%'STUDENT NAME','%12s'%'ADDRESS','%10s'%'PHONE')
        print("\n**************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
    print("-"*50)
    
def editstu():
    global cn,cur
    print("\n*******************EDIT STUDENT FORM **************************")
    ID = int(input("Enter student ID to edit: "))
    query="select * from stu where ID="+str(ID)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\n *****SORRY! NO MATCHING DETAILS AVAILABLE*****")
    else:
        print("\n**************************************************")
        print('%5s'%"ID",'%15s'%'STUDENT NAME','%12s'%'ADDRESS','%10s'%'PHONE ')
        print("\n**************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
    print("-"*50)
    ans = input("\nAre you sure to update ? (y/n)")
    if ans=="y" or ans=="Y":
        a = input("Enter new address to update (enter old value if not to update): ")
        p = int(input("Enter new phone to update (enter old value if not to update): "))
        query="update stu set ad='"+a+"',ph="+str(p) + " where ID="+str(ID)
        cur.execute(query)
        cn.commit()
        print("\n *****RECORD UPDATED*****")
                
def delstu():
    global cn,cur
    print("\n*******************DELETE STUDENT FORM **************************")
    ID = int(input("Enter student ID to delete: "))
    query="select * from stu where ID="+str(ID)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\n*****SORRY! NO MATCHING DETAILS AVAILABLE*****")
    else:
        print("\n**************************************************")
        print('%5s'%"ID",'%15s'%'STUDENT NAME','%12s'%'ADDRESS','%10s'%'PHONE')
        print("\n**************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
    print("-"*50)
    ans = input("\nAre you sure to delete ? (y/n)")
    if ans=="y" or ans=="Y":
        query="delete from stu where ID="+str(ID)
        cur.execute(query)
        cn.commit()
        print("\n*****RECORD DELETED*****")
def clear():
      for i in range(1,50):
          print()
          
def generateslip():
    global cn,cur
    print("\n*******************FEE SLIP **************************")
    ID = int(input("Enter student ID to print fee slip: "))
    query="select * from stu where ID="+str(ID)
    cur.execute(query)
    results = cur.fetchone()
    if cur.rowcount<=0:
        print("\n ******SORRY! NO MATCHING DETAILS AVAILABLE*****")
    else:
        cd = datetime.datetime.now()
        ct = datetime.date.today()
        print("\n\t\tTIME INSTITUTE")
        print("\nFEE RECEIPT FOR THE PERIOD (01-APR-2020 TO 31-MAR-2021)")
        print("\nDATE & TIME: ",cd)
        print("ID: ",results[0]," "*20,"NAME: ",results[1])
        print("CLASS: ",results[4]," "*20,"COURSE: ",results[5])
        print("-"*65)
        t = "90,000"
        l = "50,000"
        d = "40,000"
        m = "20,000"
        a = "0"
        net = "200,000"
        print("CATEGORY","%20s"%"FEE","%15s"%"CONCESSION","%18s"%"NET AMOUNT")
        print("-"*65)
        print("TUITION\t\t\t"+str(t)+"\t\t"+str(a)+"\t\t"+str(t))
        print("LIBRARY\t\t\t"+str(l)+"\t\t"+str(a)+"\t\t"+str(l))
        print("DPP\t\t\t"+str(d)+"\t\t"+str(a)+"\t\t"+str(d))
        print("MODULE\t\t\t"+str(m)+"\t\t"+str(a)+"\t\t"+str(m))
        print("-"*65)
        print("NET FEES: ",net)
        print("AMOUNT IN WORDS: TWO LAKHS ONLY")
        print("Cheque no.: 97860")
        print("Dated:",ct)
        print("Branch: DELHI")      
    print("-"*65)
    print("\n\t\t*****PRESS ANY KEY*****")
    input()
        

print("\t******WELCOME TO INSTITUTE MANAGEMENT SYSTEM*****")
print("\n\t\t*****TIME INSTITUE*****")
pwd = "123"
print("\n1. ADMIN")
print("2. VIEWER")
choice = int(input("\nEnter your choice: "))
if choice == 1:
    pw = input("Enter password: ")
    if pw != pwd:
        print("OOPS! Incorrect password")
    else:
        while True:
            print("\n1. SHOW STUDENT LIST ")
            print("2. GET LIST CLASS WISE")
            print("3. ADD NEW STUDENT")
            print("4. SEARCH STUDENT ")
            print("5. EDIT STUDENT ")
            print("6. DELETE STUDENT ")
            print("7. GENERATE FEE SLIP ")
            print("8. CONTACT US")
            print("0. EXIT")
            ans = int(input("Enter your choice: "))
            if ans==1:
                showall()
            elif ans==2:
                getlist()
            elif ans==3:
                addstu()
            elif ans==4:
                searchstu()
            elif ans==5:
                editstu()
            elif ans==6:
                delstu()
            elif ans==7:
                generateslip()
            elif ans==8:
                print("*"*60)
                print(" "*20,"DIRECTOR : VIPIN VERMA ")
                print(" "*20,"EMAIL  : VIPIN221@GMAIL.COM")
                print("*"*60)
            elif ans==0:
                print("\nBye!!!")
                cn.close()
                break
            
elif choice == 2:
    while True:
            print("\n1. SHOW STUDENT LIST ")
            print("2. SEARCH STUDENT ")
            print("3. GET LIST CLASS WISE")
            print("4. GENERATE FEE SLIP ")
            print("5. SHOW COURSES")
            print("6. CONTACT US")
            print("0. EXIT")
            ans = int(input("\nEnter your choice: "))
            if ans==1:
                showall()
            elif ans==2:
                searchstu()
            elif ans==3:
                getlist()
            elif ans==4:
                generateslip()
            elif ans==5:
                showAll()                
            elif ans==6:
                print("*"*60)
                print(" "*20,"DIRECTOR : VIPIN VERMA ")
                print(" "*20,"EMAIL  : VIPIN221@GMAIL.COM")
                print("*"*60)                
            elif ans==0:
                print("\nBye!!!")
                cn.close()
                break
    

              
    
