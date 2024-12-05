from tkinter import*
from tkinter import messagebox
import os

top=Tk()
top.title("Retail Billing ")
top.geometry("1300x700")
top.resizable(False,False)

def total():
    # Cosmetic totals
    global BathSoap, FaceCream, FaceWash, HairSpray, HairGel, rice, daal, oil, sugar, wheat, Maaza, Pepsi, Sprite, Dew, Frooti
    global totalbill
    # Get quantities and calculate total prices for cosmetics
    BathSoap = int(soapentry.get()) * 20
    FaceCream = int(soapentry2.get()) * 120
    FaceWash = int(soapentry3.get()) * 80
    HairSpray = int(soapentry4.get()) * 180
    HairGel = int(soapentry5.get()) * 80

    # Calculate Cosmetic Total and Tax
    CosmeticTotal = BathSoap + FaceCream + FaceWash + HairSpray + HairGel
    CosmeticTax = CosmeticTotal * 0.012

    # Display in the entry fields
    CosmeticpriceEntry.delete(0, END)
    CosmeticpriceEntry.insert(0, f'{CosmeticTotal} Rs')
    Cosmeticpricetax.delete(0, END)
    Cosmeticpricetax.insert(0, f'{CosmeticTax} Rs')

    # Get quantities and calculate total prices for groceries
    rice = int(Groceryentry1.get()) * 200
    oil = int(Groceryentry2.get()) * 120
    daal = int(Groceryentry3.get()) * 40
    sugar = int(Groceryentry4.get()) * 80
    wheat = int(Groceryentry5.get()) * 180

    # Calculate Grocery Total and Tax
    groceryTotal = rice + daal + oil + sugar + wheat
    GroceryTax = groceryTotal * 0.04

    # Display in the entry fields
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, f'{groceryTotal} Rs')
    grocerypricetax.delete(0, END)
    grocerypricetax.insert(0, f'{GroceryTax} Rs')

    # Get quantities and calculate total prices for cold drinks
    Maaza = int(colddrinkentry1.get()) * 50
    Pepsi = int(colddrinkentry2.get()) * 40
    Sprite = int(colddrinkentry3.get()) * 40
    Dew = int(colddrinkentry4.get()) * 80
    Frooti = int(colddrinkentry5.get()) * 50

    # Calculate Cold Drink Total and Tax
    drinkpricetotal = Maaza + Pepsi + Sprite + Dew + Frooti
    DrinkTax = drinkpricetotal * 0.01

    # Display in the entry fields
    drinkpriceEntry.delete(0, END)
    drinkpriceEntry.insert(0, f'{drinkpricetotal} Rs')
    drinkpricetax.delete(0, END)
    drinkpricetax.insert(0, f'{DrinkTax} Rs')

    # Calculate the Total Bill
    totalbill = CosmeticTotal + groceryTotal + drinkpricetotal + CosmeticTax + GroceryTax + DrinkTax

    
def bill():
    if entry1.get() == '' or entry2.get() == '':
        messagebox.showerror('Error', 'Customer Details Are Required')
    elif CosmeticpriceEntry.get() == '' and grocerypriceEntry.get() == '' and drinkpriceEntry.get() == '':
        messagebox.showerror('Error', 'No Products Are Selected')
##Check if no products are selected (all entries are zero)
    elif CosmeticpriceEntry.get() == '0 Rs' and grocerypriceEntry.get() == '0 Rs' and drinkpriceEntry.get() == '0 Rs':
        messagebox.showerror('Error', 'No Products Are Selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t** Welcome Customer **')
        textarea.insert(END, f"\nCustomer Name: {entry1.get()}")
        textarea.insert(END, f"\nPhone Number: {entry2.get()}")
        textarea.insert(END, f"\nCosmetic Price: {CosmeticpriceEntry.get()}")
        textarea.insert(END, '\n======================================================' )
        textarea.insert(END, '\nProducts\t\t\tQty\t\t\tprice' )
        textarea.insert(END, '\n=======================================================' )
        if soapentry.get() != '0':
            textarea.insert(END, f'BathSoap\t\t\t{soapentry.get()}\t\t\t{BathSoap} Rs\n')
        if soapentry2.get() != '0':
            textarea.insert(END, f'FaceCream\t\t\t{soapentry2.get()}\t\t\t{FaceCream} Rs\n')
        if soapentry3.get() != '0':
            textarea.insert(END, f'FaceWash\t\t\t{soapentry3.get()}\t\t\t{FaceWash} Rs\n')
        if soapentry4.get() != '0':
            textarea.insert(END, f'HairSpray\t\t\t{soapentry4.get()}\t\t\t{HairSpray} Rs\n')
        if soapentry5.get() != '0':
            textarea.insert(END, f'HairGel\t\t\t{soapentry5.get()}\t\t\t{HairGel} Rs\n')

        if Groceryentry1.get() != '0':
            textarea.insert(END, f'rice\t\t\t{Groceryentry1.get()}\t\t\t{rice} Rs\n')
        if Groceryentry2.get() != '0':
            textarea.insert(END, f'oil\t\t\t{Groceryentry2.get()}\t\t\t{daal} Rs\n')
        if Groceryentry3.get() != '0':
            textarea.insert(END, f'daal\t\t\t{Groceryentry3.get()}\t\t\t{oil} Rs\n')
        if Groceryentry4.get() != '0':
            textarea.insert(END, f'sugar\t\t\t{Groceryentry4.get()}\t\t\t{sugar} Rs\n')
        if Groceryentry5.get() != '0':
            textarea.insert(END, f'wheat\t\t\t{Groceryentry5.get()}\t\t\t{wheat} Rs\n')

        if colddrinkentry1.get() != '0':
            textarea.insert(END, f'Maaza\t\t\t{colddrinkentry1.get()}\t\t\t{Maaza} Rs\n')
        if colddrinkentry2.get() != '0':
            textarea.insert(END, f'Pepsi\t\t\t{colddrinkentry2.get()}\t\t\t{Pepsi} Rs\n')
        if colddrinkentry3.get() != '0':
            textarea.insert(END, f'Sprite\t\t\t{colddrinkentry3.get()}\t\t\t{Sprite} Rs\n')
        if colddrinkentry4.get() != '0':
            textarea.insert(END, f'Dew\t\t\t{colddrinkentry4.get()}\t\t\t{Dew} Rs\n')
        if colddrinkentry5.get() != '0':
            textarea.insert(END, f'Frooti\t\t\t{colddrinkentry5.get()}\t\t\t{Frooti} Rs\n')
        textarea.insert(END, '\n-------------------------------------------------------' )

        if Cosmeticpricetax.get()!="0.0 Rs":
             textarea.insert(END,f'\n CosmeticTax \t\t{Cosmeticpricetax.get()}')
        if grocerypricetax.get()!="0.0 Rs":
             textarea.insert(END,f'\n groceryTax \t\t{grocerypricetax.get()}')
        if drinkpricetax.get()!="0.0 Rs":
             textarea.insert(END,f'\n colddrinkTax \t\t{drinkpricetax.get()}')
        textarea.insert(END,f'\nTotal Bill :\t\t\t\t\t{totalbill} Rs')
        textarea.insert(END, '\n-------------------------------------------------------' )

def clear():
    # Clear all entry fields
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

    soapentry.delete(0, END) 
    soapentry2.delete(0, END)
    soapentry3.delete(0, END)
    soapentry4.delete(0, END)
    soapentry5.delete(0, END)

    Groceryentry1.delete(0, END)
    Groceryentry2.delete(0, END)
    Groceryentry3.delete(0, END)
    Groceryentry4.delete(0, END)
    Groceryentry5.delete(0, END)

    colddrinkentry1.delete(0, END)
    colddrinkentry2.delete(0, END)
    colddrinkentry3.delete(0, END)
    colddrinkentry4.delete(0, END)
    colddrinkentry5.delete(0, END)

    CosmeticpriceEntry.delete(0, END)
    Cosmeticpricetax.delete(0, END)  
    grocerypriceEntry.delete(0, END)
    grocerypricetax.delete(0, END)  
    drinkpriceEntry.delete(0, END)
    drinkpricetax.delete(0, END)  

    textarea.delete(1.0, END)
    # Reset all values to 0
    soapentry.insert(0, 0)
    soapentry2.insert(0, 0)
    soapentry3.insert(0, 0)
    soapentry4.insert(0, 0)
    soapentry5.insert(0, 0)

    Groceryentry1.insert(0, 0)
    Groceryentry2.insert(0, 0)
    Groceryentry3.insert(0, 0)
    Groceryentry4.insert(0, 0)
    Groceryentry5.insert(0, 0)

    colddrinkentry1.insert(0, 0)
    colddrinkentry2.insert(0, 0)
    colddrinkentry3.insert(0, 0)
    colddrinkentry4.insert(0, 0)
    colddrinkentry5.insert(0, 0)

    CosmeticpriceEntry.insert(0, 0)
    Cosmeticpricetax.insert(0, 0)
    grocerypriceEntry.insert(0, 0)
    grocerypricetax.insert(0, 0)
    drinkpriceEntry.insert(0, 0)
    drinkpricetax.insert(0, 0)

def print_bill():
    file_name = "bill.txt"
    with open(file_name, "w") as f:
        f.write(textarea.get(1.0, END))
    os.startfile(file_name, "print")

               
lab=Label(top,text="Retail Billing System",
           font=('times new roman', 30, 'bold'),fg='gold',bg='gray20',bd=12,relief=GROOVE)
lab.pack(fill=X)


custome_details = LabelFrame(top, text='Customer Details',
                             font=('times new roman', 15, 'bold'),fg='gold',bg='gray20',bd=12,relief=GROOVE)
custome_details.pack(fill=X,pady=10)

namelable = Label(custome_details, text="Name",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
namelable.grid(row=0, column=0,padx=20)
entry1 = Entry(custome_details,font=('times new roman', 15) ,bd=7,width=18,relief=GROOVE)
entry1.grid(row=0, column=1,padx=8)

phonelable = Label(custome_details, text="Phone Number",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
phonelable.grid(row=0, column=2,padx=20)
entry2 = Entry(custome_details,font=('times new roman', 15),bd=7,width=18,relief=GROOVE)
entry2.grid(row=0, column=3,padx=8)

billlable = Label(custome_details, text="Bill Number",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
billlable.grid(row=0, column=4,padx=20)
entry3 = Entry(custome_details,font=('times new roman', 15),bd=7,width=18,relief=GROOVE)
entry3.grid(row=0, column=5,padx=8)

"""b1 = Button(custome_details,text='Search',fg="gray20",bg="white",
            font=("Consolas", 13, "bold"),height="1",width="13",bd=7,relief=GROOVE)
b1.grid(row=0,column=6,padx=20)"""

##----
productsFrame=Frame(top)
productsFrame.pack(fill=X)

Cosmeticdetails = LabelFrame(productsFrame, text='Cosmetic',
                             font=('times new roman', 15, 'bold'),fg='gold',bg='gray20',bd=12,relief=GROOVE)
Cosmeticdetails.grid(row=0,column=0,padx=10,pady=10)

soap = Label(Cosmeticdetails, text="Bath Soap",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
soap.grid(row=0, column=0,sticky='w')
soapentry= Entry(Cosmeticdetails,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
soapentry.grid(row=0, column=1,padx=10,pady=10)
soapentry.insert(0,0)

soap2 = Label(Cosmeticdetails, text="Face Cream",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
soap2.grid(row=1, column=0,sticky='w')
soapentry2= Entry(Cosmeticdetails,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
soapentry2.grid(row=1, column=1,padx=10,pady=10)
soapentry2.insert(0,0)

soap3 = Label(Cosmeticdetails, text="Face Wash",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
soap3.grid(row=2, column=0,sticky='w')
soapentry3= Entry(Cosmeticdetails,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
soapentry3.grid(row=2, column=1,padx=10,pady=10)
soapentry3.insert(0,0)

soap4= Label(Cosmeticdetails, text="Hair Spray",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
soap4.grid(row=3, column=0,sticky='w')
soapentry4= Entry(Cosmeticdetails,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
soapentry4.grid(row=3,column=1,padx=10,pady=10)
soapentry4.insert(0,0)

soap5= Label(Cosmeticdetails, text="Hair Gel",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
soap5.grid(row=4, column=0,sticky='w')
soapentry5= Entry(Cosmeticdetails,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
soapentry5.grid(row=4,column=1,padx=10,pady=10)
soapentry5.insert(0,0)

##_____-



Grocery= LabelFrame(productsFrame, text='Grocery',
                             font=('times new roman', 15, 'bold'),fg='gold',bg='gray20',bd=12,relief=GROOVE)
Grocery.grid(row=0,column=1,padx=10,pady=10)

Grocery1= Label(Grocery, text="Rice",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
Grocery1.grid(row=0, column=0,padx=10,pady=10,sticky='w')
Groceryentry1= Entry(Grocery,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
Groceryentry1.grid(row=0, column=1,padx=10,pady=10)
Groceryentry1.insert(0,0)


Grocery2 = Label(Grocery, text="Oil",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
Grocery2.grid(row=1, column=0,padx=10,pady=10,sticky='w')
Groceryentry2= Entry(Grocery,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
Groceryentry2.grid(row=1, column=1,padx=10,pady=10)
Groceryentry2.insert(0,0)

Grocery3 = Label(Grocery, text="Daal",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
Grocery3.grid(row=2, column=0,padx=10,pady=10,sticky='w')
Groceryentry3= Entry(Grocery,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
Groceryentry3.grid(row=2, column=1,padx=10,pady=10)
Groceryentry3.insert(0,0)

Grocery4= Label(Grocery, text="Wheat",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
Grocery4.grid(row=3, column=0,padx=10,pady=10,sticky='w')
Groceryentry4= Entry(Grocery,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
Groceryentry4.grid(row=3,column=1,padx=10,pady=10)
Groceryentry4.insert(0,0)

Grocery5= Label(Grocery, text="Sugar",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
Grocery5.grid(row=4, column=0,padx=10,pady=10,sticky='w')
Groceryentry5= Entry(Grocery,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
Groceryentry5.grid(row=4,column=1,padx=10,pady=10)
Groceryentry5.insert(0,0)

##_____

colddrink= LabelFrame(productsFrame, text='Cold Drink',
                             font=('times new roman', 15, 'bold'),fg='gold',bg='gray20',bd=12,relief=GROOVE)
colddrink.grid(row=0,column=2,padx=10,pady=10)

colddrink1= Label(colddrink, text="Maaza",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
colddrink1.grid(row=0, column=0,padx=10,pady=10,sticky='w')
colddrinkentry1= Entry(colddrink,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
colddrinkentry1.grid(row=0, column=1,padx=10,pady=10)
colddrinkentry1.insert(0,0)

colddrink2 = Label(colddrink, text="Pepsi",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
colddrink2.grid(row=1, column=0,padx=10,pady=10,sticky='w')
colddrinkentry2= Entry(colddrink,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
colddrinkentry2.grid(row=1, column=1,padx=10,pady=10)
colddrinkentry2.insert(0,0)

colddrink3 = Label(colddrink, text="Sprite",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
colddrink3.grid(row=2, column=0,padx=10,pady=10,sticky='w')
colddrinkentry3= Entry(colddrink,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
colddrinkentry3.grid(row=2, column=1,padx=10,pady=10)
colddrinkentry3.insert(0,0)

colddrink4= Label(colddrink, text="Dew",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
colddrink4.grid(row=3, column=0,padx=10,pady=10,sticky='w')
colddrinkentry4= Entry(colddrink,font=('times new roman', 10) ,bd=7,width=12,relief=GROOVE)
colddrinkentry4.grid(row=3,column=1,padx=10,pady=10)
colddrinkentry4.insert(0,0)

colddrink5= Label(colddrink, text="Frooti",
                  font=('times new roman', 15, 'bold'),fg='white',bg='gray20')
colddrink5.grid(row=4, column=0,padx=10,pady=10,sticky='w')
colddrinkentry5= Entry(colddrink,font=('times new roman', 10),bd=7,width=12,relief=GROOVE)
colddrinkentry5.grid(row=4,column=1,padx=10,pady=10)
colddrinkentry5.insert(0,0)

# Create the Frame for the bill area
bill_frame = Frame(productsFrame, bd=8, relief=GROOVE)
bill_frame.grid(row=0, column=3, padx=10, pady=0)

# Create and add the Label to the Frame
bill_label = Label(bill_frame, text="Bill Area",
                   font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
bill_label.pack()


scrollbar=Scrollbar(bill_frame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(bill_frame,height=16,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

##_______

billmenu = LabelFrame(top, text='Bill Menu',
                             font=('times new roman', 15, 'bold'),fg='gold',bg='gray20',bd=12,relief=GROOVE)
billmenu.pack(fill=X)

Cosmeticpricelable = Label(billmenu, text='Cosmetic Price',
                             font=('times new roman', 15, 'bold'),fg='white',bg='gray20',bd=12)
Cosmeticpricelable.grid(row=0,column=0)

CosmeticpriceEntry= Entry(billmenu,font=('times new roman', 10),bd=10,width=12,relief=GROOVE)
CosmeticpriceEntry.grid(row=0,column=1)
CosmeticpriceEntry.insert(0,0)

grocerypricelable = Label(billmenu, text='Grocery Price',
                             font=('times new roman', 15, 'bold'),fg='white',bg='gray20',bd=12)
grocerypricelable.grid(row=1,column=0,)

grocerypriceEntry= Entry(billmenu,font=('times new roman', 10),bd=10,width=12,relief=GROOVE)
grocerypriceEntry.grid(row=1,column=1)
grocerypriceEntry.insert(0,0)

drinkpricelable = Label(billmenu, text='Cold Drink Price',
                             font=('times new roman', 15, 'bold'),fg='white',bg='gray20',bd=12)
drinkpricelable.grid(row=2,column=0)

drinkpriceEntry= Entry(billmenu,font=('times new roman', 10),bd=10,width=12,relief=GROOVE)
drinkpriceEntry.grid(row=2,column=1)
drinkpriceEntry.insert(0,0)
#___

Cosmetictax = Label(billmenu, text='Cosmetic Tax',
                             font=('times new roman', 15, 'bold'),fg='white',bg='gray20',bd=12)
Cosmetictax.grid(row=0,column=2)

Cosmeticpricetax= Entry(billmenu,font=('times new roman', 10,'bold'),bd=10,width=12,relief=GROOVE)
Cosmeticpricetax.grid(row=0,column=3)
Cosmeticpricetax.insert(0,0)

groceryprice = Label(billmenu, text=' Grocery Tax',
                             font=('times new roman', 15, 'bold'),fg='white',bg='gray20',bd=12)
groceryprice.grid(row=1,column=2)

grocerypricetax= Entry(billmenu,font=('times new roman', 10,'bold'),bd=10,width=12,relief=GROOVE)
grocerypricetax.grid(row=1,column=3)
grocerypricetax.insert(0,0)


drinkprice = Label(billmenu, text='Cold Drink Tax',
                             font=('times new roman', 15, 'bold'),fg='white',bg='gray20',bd=12)
drinkprice.grid(row=2,column=2)

drinkpricetax= Entry(billmenu,font=('times new roman', 10,'bold'),bd=10,width=12,relief=GROOVE)
drinkpricetax.grid(row=2,column=3)
drinkpricetax.insert(0,0)

##_____

b1 = Button(billmenu, text='Total',command=total, bg="white", fg="black",
            font=("Consolas", 13, "bold"), width=10,bd=7,relief=GROOVE)
b1.grid(row=1,column=4,padx=40,pady=10)

b2 = Button(billmenu, text='Bill',command = bill, bg="white", fg="black",
            font=("Consolas", 13, "bold"), width=10,bd=7,relief=GROOVE)
b2.grid(row=1,column=5,padx=40,pady=10)

b3 = Button(billmenu, text='Clear',command=clear, bg="white", fg="black",
            font=("Consolas", 13, "bold"), width=10,bd=7,relief=GROOVE)
b3.grid(row=1,column=6,padx=40,pady=10)

b4 = Button(billmenu, text='print', command = print_bill,bg="white", fg="black",
            font=("Consolas", 13, "bold"), width=10,bd=7,relief=GROOVE)
b4.grid(row=1,column=7,padx=40,pady=10)

top.mainloop()















