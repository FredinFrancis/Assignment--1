print("Program to Calculate Cost of a Shirt")
print("Experience the new feel of Shopping!")
print("\n")
print( "Welcome to Abbys's Merchandizing !!")
print("\n")
print("Please choose your desired selection: ")
print("1. Polo Shirt")
print("2. T-Shirt")
print("\n")

# Input from user

select=int(input("Please enter your selection:- "))

# Execution as per selection

if (select==1):
    print("You have chosen Polo Shirts!")
    print("\n")
    col1= str(input("Please enter your desired colour:- "))
    qty1= int(input("Please enter your required quantity:- "))
    rate=9.99
    hstrate=1.13
    netprice1=rate*qty1
    hst1=netprice1*hstrate
    hst=hst1-netprice1
    total=netprice1+hst

    #Order confirmation query
    print("\n")
    print(" Confirm your order !")
    print(" Type of Shirt- Polo Shirt")
    print(" Colour- "+ col1)
    print(" Quantity- "+ str(qty1))
    print(" Taxable Value = %.2f" % (netprice1))
    print(" HST @ 13 = %.2f" % (hst))
    print(" Total Price = $ %.2f" % (total))

    #Confirmation Page
    
    confirm=int(input(" Enter 1 to confirm :- "))
    
    if(confirm==1):
        print("\n")
        print(" Order confirmed !")
        print(" Thanks for shopping with Abby's Merchandizing ! \n Come Again !!!!!!!!")

    else:
        print(" Order Not Confirmed !")

elif(select==2):
    print("You have chosen T-Shirts!")
    print("\n")
    col1= str(input("Please enter your desired colour:- "))
    qty1= int(input("Please enter your required quantity:- "))
    rate=9.99
    hstrate=1.13
    netprice1=rate*qty1
    hst1=netprice1*hstrate
    hst=hst1-netprice1
    total=netprice1+hst1

    #Order confirmation query
    print("\n")
    print(" Confirm your order !")
    print(" Type of Shirt- T-Shirt")
    print(" Colour- "+ col1)
    print(" Quantity- "+ str(qty1))
    print(" Taxable Value = %.2f" % (netprice1))
    print(" HST @ 13 = %.2f" % (hst))
    print(" Total Price = $ %.2f" % (total))

    #Confirmation Page
    
    confirm=int(input("Enter 1 to confirm :- "))
    
    if(confirm==1):
        print("\n")
        print(" Order confirmed !")
        print(" Thanks for shopping with Abby's Merchandizing ! \n Come Again !!!!!!!!")

    else:
        print("Order not confirmed !")
        
    
else:
    print("Error!")
        





