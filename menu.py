import mysql.connector 

con = mysql.connector.connect(host="localhost",user="root",password="ashutoshverma7032",database="courier_service")

customer=con.cursor()

for i in range (0,99):
    print("----------- Yellow dart courier service---------")


    print(" press 1 for courier_order ")
    print("  press 2 for customer_details")
    print(" press 3 for courier_service_boys")
    print(" press 4 for invoice_procedure")
    print("press 5 for exit")

    choice=int(input("enter the section you want acess:<<<<1,2,3,4,5>>>:"))

    if choice==1:
               print("a, courier placement")
    sector=str(input("enter the secon that you want to acess:"))

    if sector=="A":
               print("couriers-order")

               a=(input("enter the customer name:"))
               b=int(input("enter the customer mobile number:"))
               c=(input("enter rhe customer address:"))
               d=(input("enter the reciever address:"))
               e=int(input("enter the alternate phone number:"))

               customer1.execute( "insert into courier_order values" (' "+a+" ',"+str(b)+",' "+c+" ',' "+d+" ',"+str(e)+",' "+f+" '))
con.commit()

print(customer1.rowcount,"congratualitions your order is place")
