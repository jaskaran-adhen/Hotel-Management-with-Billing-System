import random
import datetime

room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []
name = []
phone = []
add = []
checkin = []
checkout = []

   
i = 0
   
def Home():
      
    print("\t\t\t\t\t\t WELCOME TO APNA HOTEL \n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Menu Card\n")
    print("\t\t\t 3 Payment\n")
    print("\t\t\t 4 Record\n")
    print("\t\t\t 0 Exit\n")
   
    ch=int(input("->"))
      
    if ch == 1:
        print(" ")
        Booking()
      
    elif ch == 2:
        print(" ")
        restaurant()
      
    elif ch == 3:
        print(" ")
        Payment()
      
    elif ch == 4:
        print(" ")
        Record()
      
    else:
        exit()
   
def date(c):
      
    if c[2] >= 2019 and c[2] <= 2022:
          
        if c[1] != 0 and c[1] <= 12:
              
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                  
                if c[2]%4 == 0 and c[0] <= 29:
                    pass
                  
                elif c[0]<29:
                    pass
                  
                else:
                    print("Invalid date\n")
                    name.pop(i)
                    phone.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Booking()
                  
def Booking():
    
        global i
        print(" BOOKING ROOMS")
        print(" ")
          
        while 1:
            n = str(input("Name: "))
            p1 = str(input("Phone No.: "))
            a = str(input("Address: "))
              
            if n!="" and p1!="" and a!="":
                name.append(n)
                add.append(a)
                break
                  
            else:
                 print("\tName, Phone no. & Address cannot be empty..!!")
               
        cii=str(input("Check-In: "))
        checkin.append(cii)
        cii=cii.split('/')
        ci=cii
        ci[0]=int(ci[0])
        ci[1]=int(ci[1])
        ci[2]=int(ci[2])
        date(ci)       
        
       
        coo=str(input("Check-Out: "))
        checkout.append(coo)
        coo=coo.split('/')
        co=coo
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])
          
        if co[1]<ci[1] and co[2]<ci[2]:
              
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
            name.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
              
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
            name.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        else:
            pass
          
        date(co)
        d1 = datetime.datetime(ci[2],ci[1],ci[0])
        d2 = datetime.datetime(co[2],co[1],co[0])
        d = (d2-d1).days
        day.append(d)
           
        print("----SELECT ROOM TYPE----")
        print(" 1. Standard Non-AC")
        print(" 2. Standard AC")
        print(" 3. 3-Bed Non-AC")
        print(" 4. 3-Bed AC")
        print(("\t\tPress 0 for Room Prices"))
          
        ch=int(input("->"))
        
        if ch==0:
            print(" 1. Standard Non-AC - Rs. 3500")
            print(" 2. Standard AC - Rs. 4000")
            print(" 3. 3-Bed Non-AC - Rs. 4500")
            print(" 4. 3-Bed AC - Rs. 5000")
            ch=int(input("->"))
        if ch==1:
            room.append('Standard Non-AC')
            print("Room Type- Standard Non-AC")  
            price.append(3500)
            print("Price- 3500")
        elif ch==2:
            room.append('Standard AC')
            print("Room Type- Standard AC")
            price.append(4000)
            print("Price- 4000")
        elif ch==3:
            room.append('3-Bed Non-AC')
            print("Room Type- 3-Bed Non-AC")
            price.append(4500)
            print("Price- 4500")
        elif ch==4:
            room.append('3-Bed AC')
            print("Room Type- 3-Bed AC")
            price.append(5000)
            print("Price- 5000")
        else:
            print(" Wrong choice..!!")
   
        rn = random.randrange(40)+300
        cid = random.randrange(40)+10
          
          
        while rn in roomno or cid in custid:
            rn = random.randrange(60)+300
            cid = random.randrange(60)+10
              
        rc.append(0)
        p.append(0)
                
        if p1 not in phone:
            phone.append(p1)
        elif p1 in phone:
            for n in range(0,i):
                if p1== phone[n]:
                    if p[n]==1:
                        phone.append(p1)
        elif p1 in phone:
            for n in range(0,i):
                if p1== phone[n]:
                    if p[n]==0:
                        print("\tPhone no. already exists and payment yet not done..!!")
                        name.pop(i)
                        add.pop(i)
                        checkin.pop(i)
                        checkout.pop(i)
                        Booking()
        print("")
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
        print("Room No. - ",rn)
        print("Customer Id - ",cid)
        roomno.append(rn)
        custid.append(cid)
        i=i+1
        n=int(input("0-BACK\n ->"))
        if n==0:
            Home()
        else:
            exit()
  
def restaurant():
    ph=int(input("Customer Id: "))
    global i
    f=0
    r=0
    for n in range(0,i):
        if custid[n]==ph and p[n]==0:
            f=1
            print("----------------------------------")
            print("          Hotel AnCasa")
            print("----------------------------------")
            print("          Menu Card")
            print("----------------------------------")
            print("\n BEVARAGES    ")
            print("----------------------------------")
            print(" 1  Regular Tea............. 20.00")
            print(" 2  Coffee.................. 25.00 ")
            print(" 3  Cold Drink.............. 25.00")
            print(" 4  Bread Butter............ 30.00")
            print(" 5  Bread Jam............... 30.00")
            print(" 6  Veg. Toast Sandwich..... 50.00 ")    
            print("----------------------------------")
            print(" MAIN COURSE     ")    
            print("---------------------------------- ")     
            print(" 7 Shahi Paneer........... 110.00 ")
            print(" 8 Chilli Paneer.......... 140.00 ")     
            print(" 9  Dal Fry................ 140.00") 
            print(" 10 Plain Rice.............. 90.00")
            print(" 11 Dal Tadka.............. 150.00")
            print(" 12 Plain Roti.............. 15.00")
            print(" 13 Butter Roti............. 15.00")
            print("Press 0 -to end ")
            ch=1
            while(ch!=0):
                  
                ch=int(input(" -> "))
                
                if ch==1 :
                    rs=20
                    r=r+rs
                elif ch<=3 and ch>=2:
                    rs=25
                    r=r+rs
                elif ch<=5 and ch>=4:
                    rs=30
                    r=r+rs
                elif ch==6:
                    rs=50
                    r=r+rs
                
                elif ch==7:
                    rs=110
                    r=r+rs
                elif ch<=9 and ch>=8:
                    rs=140
                    r=r+rs
                elif ch==10:
                    rs=90
                    r=r+rs
                elif ch==11 :
                    rs=150
                    r=r+rs
                elif ch<=13 and ch>=12:
                    rs=15
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("Wrong Choice..!!")
            print("Total Bill: ",r)
            
            r=r+rc.pop(n)
            rc.append(r)    
        else:
            pass
    if f == 0:
        print("Invalid Customer Id")
    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()
                    
def Payment():
      
    ph=str(input("Phone Number: "))
    global i
    f=0
      
    for n in range(0,i):
        if ph==phone[n] :
              
             if p[n]==0:
                f=1
                print(" Payment")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")
                   
                print("  1- Credit/Debit Card")
                print("  2- Paytm/PhonePe")
                print("  3- Using UPI")
                print("  4- Cash")
                x=int(input("-> "))
                print("\n  Amount: ",(price[n]*day[n])+rc[n])
                print("\n            Pay For APNA Hotel")
                print("  (y/n)")
                ch=str(input("->"))
                  
                if ch=='y' or ch=='Y':
                    print("\n\n --------------------------------")
                    print("       Apna  Hotel ")
                    print(" --------------------------------")
                    print("              Bill")
                    print(" --------------------------------")
                    print(" Name: ",name[n],"\t\n Phone No.: ",phone[n],"\t\n Address: ",add[n],"\t")
                    print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                    print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                    print(" Restaurant Charges: \t",rc[n])
                    print(" --------------------------------")
                    print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t")
                    print(" --------------------------------")
                    print("          Thank You")
                    print("          Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n,1)
                      
                    roomno.pop(n)
                    custid.pop(n)
                    roomno.insert(n,0)
                    custid.insert(n,0)
                      
             else:
                  
                for j in range(n+1,i):
                    if ph==phone[j] :
                        if p[j]==0:
                            pass
                          
                        else:
                            f=1
                            print("\n\tPayment has been Made :)\n\n") 
    if f==0:    
        print("Invalid Customer Id")
          
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()
  
def Record():
      
    if phone!=[]:
        print("        *** HOTEL RECORD ***\n")
        print("| Name        | Phone No.    | Address       | Check-In  | Check-Out     | Room Type     | Price      |")
        print("----------------------------------------------------------------------------------------------------------------------")
          
        for n in range(0,i):
            print("|",name[n],"\t |",phone[n],"\t|",add[n],"\t|",checkin[n],"\t|",checkout[n],"\t|",room[n],"\t|",price[n])
          
        print("----------------------------------------------------------------------------------------------------------------------")
      
    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
          
    else:
        exit()
  

Home()

