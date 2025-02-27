import os , tempfile , smtplib # os used to create the folder. tempfile(create a temp file to store bill)
import random
import sys
from tkinter import *
from tkinter import messagebox
from datetime import datetime


#store purchase date and time
current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# checking bill folder is there or not
if not os.path.exists('bills'):
    os.mkdir('bills')

# FUNTIONALITY PART

#clear alll entry field


#send e-mail
def send_email():
    def send_gmail():
        try:
            # print('hello')
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()       #establish secure connection
            ob.login(senderEntry.get(), passwordEntry.get())
            message = message_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message )
            ob.quit()
            messagebox.showinfo('Seccess','Bill is successfully sent to customer')
            # root1.destroy()
        except:
            messagebox.showerror('Error', 'Something went wrong, Please try again later ')


    if text_area.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Text area is empty')

    else:
        root1 = Toplevel()
        # root1.grab_set()
        root1.title('Send Email')
        root1.config(bg  = 'gold')
        root1.resizable(0,0)

        senderFrame = LabelFrame(root1, text = 'SENDER', font = ('arail', 20, 'bold'), bd = 6,relief= RIDGE,
                                        bg = 'gray20', fg = 'white', width= 80)
        senderFrame.grid(row = 0, column = 0, padx = 20, pady = 20)

        senderLabel = Label(senderFrame, text = "Sender's Email", font=("arail", 14, 'bold'),
                             bd = 6,bg = 'gray20', fg = 'white',width=30 )
        senderLabel.grid(row = 0, column = 0, padx = 10, pady = 10)

        senderEntry = Entry(senderFrame,font=("arail", 14, 'bold'),bd = 6,bg = 'gray20', fg = 'white', width = 25 , relief= RIDGE)
        senderEntry.grid(row = 0, column = 1, padx = 10, pady = 10)

        passwordLabel = Label(senderFrame, text="Password", font=("arail", 14, 'bold'),
                              bd=6, bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=10)

        passwordEntry = Entry(senderFrame, font=("arail", 14, 'bold'), bd=6, bg='gray20', fg='white', width=25,
                              relief=RIDGE, show = '+') #show repelce text with +
        passwordEntry.grid(row=1, column=1, padx=10, pady=10)

    #recipient email data
        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arail', 20, 'bold'), bd=6, relief=RIDGE,
                                 bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=20, pady=20)

        recieverLabel = Label(recipientFrame, text="Reciever Email", font=("arail", 14, 'bold'),
                            bd=6, bg='gray20', fg='white',width = 30)
        recieverLabel.grid(row=0, column=0, padx=10, pady=10)

        recieverEntry = Entry(recipientFrame, font=("arail", 14, 'bold'), bd=6, bg='gray20', fg='white', width=25, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=10)

        messageLabel = Label(recipientFrame, text="Message", font=("arail", 16, 'bold'),
                              bd=6, bg='gray20', fg='white' )
        messageLabel.grid(row=1, column=0,  columnspan=2)


        message_textarea = Text(recipientFrame,wrap=WORD, font=("arail", 14, 'bold'), bd=2, fg='gray20',width=64, height = 15,
                              relief=RIDGE)
        message_textarea.grid(row=2, column=0, columnspan = 3)

        message_textarea.tag_configure("underline", underline=True)

        message_textarea.tag_configure("center", justify="center")

        message_textarea.delete(1.0, END)
        message_textarea.insert(END, text_area.get(1.0, END))


        #send button
        sendbutton = Button(root1, text='SEND', font=('arail', 20, 'bold'), bd=6, relief=RIDGE,
                                 bg='gray20', fg='olive', width=10, command=send_gmail)
        sendbutton.grid(row=2, column=0, padx=20, pady=20)

        root1.mainloop()


#clear button
def clear_bill():
    if text_area.get(1.0, END) == '\n':

        bath_soap_entry.delete(0, END)
        bath_soap_entry.insert(0, 0)

        face_cream_entry.delete(0, END)
        face_cream_entry.insert(0, 0)

        face_wash_entry.delete(0, END)
        face_wash_entry.insert(0, 0)

        hair_spray_entry.delete(0, END)
        hair_spray_entry.insert(0, 0)

        hair_gel_entry.delete(0, END)
        hair_gel_entry.insert(0, 0)

        body_lotion_entry.delete(0, END)
        body_lotion_entry.insert(0, 0)

        rice_entry.delete(0, END)
        rice_entry.insert(0, 0)

        dal_entry.delete(0, END)
        dal_entry.insert(0, 0)

        oil_entry.delete(0, END)
        oil_entry.insert(0, 0)

        wheat_entry.delete(0, END)
        wheat_entry.insert(0, 0)

        sugar_entry.delete(0, END)
        sugar_entry.insert(0, 0)

        tea_entry.delete(0, END)
        tea_entry.insert(0, 0)

        red_bull_entry.delete(0, END)
        red_bull_entry.insert(0, 0)

        blue_bull_entry.delete(0, END)
        blue_bull_entry.insert(0, 0)

        hurricane_entry.delete(0, END)
        hurricane_entry.insert(0, 0)

        ocean_entry.delete(0, END)
        ocean_entry.insert(0, 0)

        monster_entry.delete(0, END)
        monster_entry.insert(0, 0)

        coca_cola_entry.delete(0, END)
        coca_cola_entry.insert(0, 0)

        cosmeticprice_entry.delete(0, END)
        cosmetictax_entry.delete(0, END)

        groceriestax_entry.delete(0, END)
        groceriesprice_entry.delete(0, END)

        coca_cola_entry.delete(0, END)
        coca_cola_entry.insert(0, 0)

        drinkprice_entry.delete(0, END)
        drinktax_entry.delete(0, END)

        cosmeticprice_entry.delete(0, END)
        cosmetictax_entry.delete(0, END)

        groceriesprice_entry.delete(0, END)
        groceriestax_entry.delete(0, END)

        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        bill_entry.delete(0, END)

        messagebox.showerror('Error', 'Text area is already cleared')

    else:
        text_area.delete(1.0, END)

        bath_soap_entry.delete(0, END)
        bath_soap_entry.insert(0, 0)

        face_cream_entry.delete(0, END)
        face_cream_entry.insert(0, 0)

        face_wash_entry.delete(0, END)
        face_wash_entry.insert(0, 0)

        hair_spray_entry.delete(0, END)
        hair_spray_entry.insert(0, 0)

        hair_gel_entry.delete(0, END)
        hair_gel_entry.insert(0, 0)

        body_lotion_entry.delete(0, END)
        body_lotion_entry.insert(0, 0)

        rice_entry.delete(0, END)
        rice_entry.insert(0, 0)

        dal_entry.delete(0, END)
        dal_entry.insert(0, 0)

        oil_entry.delete(0, END)
        oil_entry.insert(0, 0)

        wheat_entry.delete(0, END)
        wheat_entry.insert(0, 0)

        sugar_entry.delete(0, END)
        sugar_entry.insert(0, 0)

        tea_entry.delete(0, END)
        tea_entry.insert(0, 0)

        red_bull_entry.delete(0, END)
        red_bull_entry.insert(0, 0)

        blue_bull_entry.delete(0, END)
        blue_bull_entry.insert(0, 0)

        hurricane_entry.delete(0, END)
        hurricane_entry.insert(0, 0)

        ocean_entry.delete(0, END)
        ocean_entry.insert(0, 0)

        monster_entry.delete(0, END)
        monster_entry.insert(0, 0)

        coca_cola_entry.delete(0, END)
        coca_cola_entry.insert(0, 0)

        cosmeticprice_entry.delete(0, END)
        cosmetictax_entry.delete(0, END)

        groceriestax_entry.delete(0, END)
        groceriesprice_entry.delete(0, END)

        coca_cola_entry.delete(0, END)
        coca_cola_entry.insert(0, 0)

        drinkprice_entry.delete(0, END)
        drinktax_entry.delete(0, END)

        cosmeticprice_entry.delete(0, END)
        cosmetictax_entry.delete(0, END)

        groceriesprice_entry.delete(0, END)
        groceriestax_entry.delete(0, END)

        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        bill_entry.delete(0, END)




#print button
def print_bill():
    if text_area.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Text area is empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(text_area.get(1.0, END))
        os.startfile(file, 'print')


#search bill
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == bill_entry.get():
            f = open(f'bills/{i}', 'r')
            text_area.delete(1.0, END)

            for data in f:
                text_area.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Bill Number not found')
#saving the bill
# generating billnumber

global billnumber
billnumber = random.randint(500, 1000)
def save_bill():

    result  = messagebox.askyesno('confirm','Do you want to save the bill?')
    if result == 1:
        bill_content  = text_area.get(0.0,END)
        file = open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('success',f'{billnumber} saved sucessfully')
        # billnumber = random.randint(500, 1000)




def total():
#cosmetic
#globally declaring variable so that it can be used globally
    global soap_value
    soap_value = int(bath_soap_entry.get()) * 50
    global face_value
    face_value = int(face_cream_entry.get()) * 50
    global hairspray_value
    hairspray_value = int(hair_spray_entry.get()) * 50
    global lotion_value
    lotion_value = int(body_lotion_entry.get()) * 50
    global facewash_value
    facewash_value = int(face_wash_entry.get()) * 50
    global hairgel_value
    hairgel_value = int(hair_gel_entry.get())*50

    global totalCosmeticPrice
    totalCosmeticPrice = soap_value+face_value+hairspray_value+lotion_value+facewash_value+hairgel_value

#it will delete the previous value in entry field
    cosmeticprice_entry.delete(0, END)
#to insert the total value in cosmetic entry field
    cosmeticprice_entry.insert(0, f'{totalCosmeticPrice}Rs')

#Grocery
    global rice_value
    rice_value = int(rice_entry.get()) * 50
    global dal_value
    dal_value = int(dal_entry.get()) * 50
    global oil_value
    oil_value = int(oil_entry.get()) * 50
    global wheat_value
    wheat_value = int(wheat_entry.get()) * 50
    global sugar_value
    sugar_value = int(sugar_entry.get()) * 50
    global tea_value
    tea_value = int(tea_entry.get())*50

    global totalGroceryPrice
    totalGroceryPrice = rice_value+dal_value+oil_value+wheat_value+sugar_value+tea_value

#it will delete the previous value in entry field
    groceriesprice_entry.delete(0, END)
#to insert the total value in grocery entry field
    groceriesprice_entry.insert(0, f'{totalGroceryPrice}Rs')

#Energy Drink
    global redbull_value
    redbull_value = int(red_bull_entry.get()) * 50
    global hurricane_value
    hurricane_value = int(hurricane_entry.get()) * 50
    global bluebull_value
    bluebull_value = int(blue_bull_entry.get())*50
    global ocean_value
    ocean_value = int(ocean_entry.get()) * 50
    global monster_value
    monster_value = int(monster_entry.get()) * 50
    global cocacola_value
    cocacola_value = int(coca_cola_entry.get()) * 50

    global totalEnergyDrinkPrice
    totalEnergyDrinkPrice = redbull_value+hurricane_value+bluebull_value+ocean_value+monster_value+cocacola_value

#it will delete the previous value in entry field
    drinkprice_entry.delete(0, END)
#to insert the total value in grocery entry field
    drinkprice_entry.insert(0, f'{totalEnergyDrinkPrice}Rs')

#Adding Tax value
    global cosmeticTax , groceriesTax, drinkTax
    cosmetictax_entry.delete(0, END)
    cosmeticTax = totalCosmeticPrice * 0.18
    cosmetictax_entry.insert(0, f'{cosmeticTax}Rs')

    groceriestax_entry.delete(0,END)
    groceriesTax = totalGroceryPrice * 0.18
    groceriestax_entry.insert(0, f'{groceriesTax}Rs')

    drinktax_entry.delete(0, END)
    drinkTax = totalEnergyDrinkPrice * 0.18
    drinktax_entry.insert(0, f'{drinkTax}Rs')


# working on billing
def Bill_area():
#if name and phone number not entered
    if name_entry.get() == '' or phone_entry.get() == '':
        messagebox.showerror('Error', 'Enter the required detail')

#when no product total is made
    elif cosmeticprice_entry.get() == '' and groceriesprice_entry.get() == '' and drinkprice_entry.get() == '':
        messagebox.showerror("Error", 'No product are selected')

#when all product price are 0 Rs
    elif cosmeticprice_entry.get() == '0Rs' and groceriesprice_entry.get() == '0Rs' and drinkprice_entry.get() == '0Rs':
        messagebox.showerror('Error', 'No product are selected')

    else:

        #it will delete any previous value in text area
            text_area.delete(1.0, END)

        #now inserting the value in text area


            text_area.tag_configure("underline", underline=True)

            text_area.tag_configure("center", justify="center")


            text_area.insert(END,'** Welcome Customer **', "center")
            text_area.insert(END, f'\nBill Number: {billnumber}')
            text_area.insert(END, f'\nCustomer Name: {name_entry.get()}')
            text_area.insert(END, f'\nPhone Number: {phone_entry.get()}')

            text_area.insert(END, f"\nPurchase Date and Time: {current_time}")

            text_area.insert(END, f'\nProduct\t\t\tQuantity\t\t\tPrice\n', 'underline')

        #print the cosmetic items on text area
            if bath_soap_entry.get() != '0':
                text_area.insert(END, f'Bath Soap\t\t\t{bath_soap_entry.get()}\t\t\t{soap_value}Rs\n')
            if face_cream_entry.get() != '0':
                text_area.insert(END, f'Face Cream\t\t\t{face_cream_entry.get()}\t\t\t{face_value}Rs\n')
            if face_wash_entry.get() != '0':
                text_area.insert(END, f'Face Wash\t\t\t{face_wash_entry.get()}\t\t\t{facewash_value}Rs\n')
            if hair_spray_entry.get() != "0":
                text_area.insert(END, f'Hair Spray\t\t\t{hair_spray_entry.get()}\t\t\t{hairspray_value}Rs\n')
            if hair_gel_entry.get() != '0':
                text_area.insert(END, f'Hair Gel\t\t\t{hair_gel_entry.get()}\t\t\t{hairgel_value}Rs\n')
            if body_lotion_entry.get() != '0':
                text_area.insert(END, f'Body Lotion\t\t\t{body_lotion_entry.get()}\t\t\t{lotion_value}Rs\n')

        #printing the groceries items on text area
            if rice_entry.get() != '0':
                text_area.insert(END, f'Rice\t\t\t{rice_entry.get()}\t\t\t{rice_value}Rs\n')
            if dal_entry.get() != '0':
                text_area.insert(END, f'Dal\t\t\t{dal_entry.get()}\t\t\t{dal_value}Rs\n')
            if oil_entry.get() != '0':
                text_area.insert(END, f'Oil\t\t\t{oil_entry.get()}\t\t\t{oil_value}Rs\n')
            if wheat_entry.get() != "0":
                text_area.insert(END, f'Whaet\t\t\t{wheat_entry.get()}\t\t\t{wheat_value}Rs\n')
            if sugar_entry.get() != '0':
                text_area.insert(END, f'Sugar\t\t\t{sugar_entry.get()}\t\t\t{sugar_value}Rs\n')
            if tea_entry.get() != '0':
                text_area.insert(END, f'Tea\t\t\t{tea_entry.get()}\t\t\t{tea_value}Rs\n')

        #printing the energy drink items on text area
            if red_bull_entry.get() != '0':
                text_area.insert(END, f'Red Bull\t\t\t{red_bull_entry.get()}\t\t\t{redbull_value}Rs\n')
            if hurricane_entry.get() != '0':
                text_area.insert(END, f'Hurricane\t\t\t{hurricane_entry.get()}\t\t\t{hurricane_value}Rs\n')
            if blue_bull_entry.get() != '0':
                text_area.insert(END, f'Blue Bull\t\t\t{blue_bull_entry.get()}\t\t\t{bluebull_value}Rs\n')
            if ocean_entry.get() != "0":
                text_area.insert(END, f'Ocean\t\t\t{ocean_entry.get()}\t\t\t{ocean_value}Rs\n')
            if monster_entry.get() != '0':
                text_area.insert(END, f'Monster\t\t\t{monster_entry.get()}\t\t\t{monster_value}Rs\n')
            if coca_cola_entry.get() != '0':
                text_area.insert(END, f'Coca Cola\t\t\t{coca_cola_entry.get()}\t\t\t{cocacola_value}Rs\n')

            text_area.insert(END, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            if cosmetictax_entry.get() != '0.0Rs':
                text_area.insert(END, f'\nCosmetics Tax\t\t\t\t{cosmetictax_entry.get()}')

            if groceriestax_entry.get() != '0.0Rs':
                text_area.insert(END, f'\nGroceries Tax\t\t\t\t{groceriestax_entry.get()}')

            if drinktax_entry.get() != '0.0Rs':
                text_area.insert(END, f'\nEnergy Drink Tax\t\t\t\t{drinktax_entry.get()}')

        #adding total bill
            global overallcosmetic_price
            overallcosmetic_price = totalCosmeticPrice + cosmeticTax
            #
            global overallgroceries_price
            overallgroceries_price = totalGroceryPrice + groceriesTax
            #
            global overalldrink_price
            overalldrink_price = totalEnergyDrinkPrice + drinkTax

        #total bill of all product
            global total_bill
            total_bill = overallcosmetic_price + overallgroceries_price + overalldrink_price

            #
            if overallcosmetic_price != 0.0:
                text_area.insert(END, f'\nOverall Cosmetic Price\t\t\t\t{overallcosmetic_price}')
            #
            if overallgroceries_price != 0.0:
                text_area.insert(END, f'\nOverall Groceries Price\t\t\t\t{overallgroceries_price}')
            #
            if overalldrink_price != 0.0:
                text_area.insert(END, f'\nOverall Energy Drink Price\t\t\t\t{overalldrink_price}')
            text_area.insert(END, f'\nTotal Bill\t\t\t\t{total_bill}')



        #total bill of all product
            global total_overallbill
            total_overallbill = overallcosmetic_price + overallgroceries_price + overalldrink_price

            save_bill()

# GUI PART
root = Tk()

root.title("Billing Machine")  #title
root.geometry("1450x920")
current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "bill.ico")
root.iconbitmap(icon_path)


#heading
HeadingLabel = Label(root, text="Billing System", font=("Jacques Francois Shadow", 30, "bold"),
                     bg = "gray20", fg = "gold" , bd = 12, relief=RIDGE)
#to make text billing system visible
HeadingLabel.pack(fill = X, pady = 6)

#creating label frame of customer detail
customer_detail = LabelFrame(root, text="Customer Details", font=("times new roman", 15, "bold"),
                             bg = "gray20",fg = "gold", bd = 8, relief=RIDGE)
customer_detail.pack(fill = X)
#1
name_label = Label(customer_detail, text = "Name", font=("times new roman", 18, "bold")
                   ,bg = "gray20",fg = "white", bd = 6 )
name_label.grid(row = 0, column = 0,padx = 30)

name_entry = Entry(customer_detail, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold"),
                   width=15)
name_entry.grid(row = 0, column = 1)

#2
phone_label = Label(customer_detail, text = "Phone No.",font=("times new roman", 18, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
phone_label.grid(row = 0, column = 2,padx = 30)

phone_entry = Entry(customer_detail, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 15)
phone_entry.grid(row = 0, column = 3)

#3
bill_label = Label(customer_detail, text = "Bill No.", font=("times new roman", 18, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
bill_label.grid(row = 0, column = 4, padx= 30)

bill_entry = Entry(customer_detail, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 15)
bill_entry.grid(row = 0, column = 5)

#4 button
search_button = Button(customer_detail, text="SEARCH", font=("arail", 12,"bold"),
                       bd = 8, relief=RIDGE, width=12,command = search_bill)
search_button.grid(row = 0, column = 6, pady = 15,  padx = 80)

#creating product frame
product_frame = Frame(root,)
product_frame.pack(fill = X ,pady = 6)

#adding cosmetic label frame
cosmetic_frame = LabelFrame(product_frame,text="Cosmetics", font=("times new roman", 15, "bold"),
                             bg = "gray20",fg = "gold", bd = 8, relief=RIDGE)
cosmetic_frame.grid(row = 0, column = 0)

#adding items
#1
bath_soap = Label(cosmetic_frame, text="Bath Soap", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
bath_soap.grid(row = 0, column = 0,  sticky = "w")

bath_soap_entry = Entry(cosmetic_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold",)
                   ,width = 5)
bath_soap_entry.grid(row = 0, column = 1, pady = 6, padx = 10)
bath_soap_entry.insert(0,0)

#2
face_cream = Label(cosmetic_frame, text="Face Cream", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
face_cream.grid(row = 1, column = 0,  sticky = "w")

face_cream_entry = Entry(cosmetic_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
face_cream_entry.grid(row = 1, column = 1, pady = 6, padx = 10)
face_cream_entry.insert(0,0)

# #3
face_wash = Label(cosmetic_frame, text="Face Wash", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
face_wash.grid(row = 2, column = 0,sticky = "w")

face_wash_entry = Entry(cosmetic_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
face_wash_entry.grid(row = 2, column = 1, pady = 6, padx = 10 )
face_wash_entry.insert(0,"0")

#4
hair_spray = Label(cosmetic_frame, text="Hair Spray", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
hair_spray.grid(row = 3, column = 0, sticky = "w")

hair_spray_entry = Entry(cosmetic_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
hair_spray_entry.grid(row = 3, column = 1, pady = 6, padx = 10)
hair_spray_entry.insert(0,0)

#5
hair_gel = Label(cosmetic_frame, text="Hair Gel", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
hair_gel.grid(row = 4, column = 0,  sticky = "w")

hair_gel_entry = Entry(cosmetic_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
hair_gel_entry.grid(row = 4, column = 1, pady = 6, padx = 10)
hair_gel_entry.insert(0,0)

#6
body_lotion = Label(cosmetic_frame, text="Body Lotion", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
body_lotion.grid(row = 5, column = 0,  sticky = "w")

body_lotion_entry = Entry(cosmetic_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
body_lotion_entry.grid(row = 5, column = 1, pady = 6, padx = 10)
body_lotion_entry.insert(0,0)

#adding grocery label frame
grocery_frame = LabelFrame(product_frame,text="Grocery", font=("times new roman", 15, "bold"),
                             bg = "gray20",fg = "gold", bd = 8, relief=RIDGE)
grocery_frame.grid(row = 0, column = 1)

#1
rice = Label(grocery_frame, text="Rice", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
rice.grid(row = 0, column = 0,  sticky = "w")

rice_entry = Entry(grocery_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
rice_entry.grid(row = 0, column = 1, pady = 6, padx = 10)
rice_entry.insert(0,0)

#2
dal = Label(grocery_frame, text="Dal", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
dal.grid(row = 1, column = 0,  sticky = "w")

dal_entry = Entry(grocery_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
dal_entry.grid(row = 1, column = 1, pady = 6, padx = 10)
dal_entry.insert(0,0)

#3
oil = Label(grocery_frame, text="Oil", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
oil.grid(row = 2, column = 0,  sticky = "w")

oil_entry = Entry(grocery_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
oil_entry.grid(row = 2, column = 1, pady = 6, padx = 10)
oil_entry.insert(0,0)

#4
wheat = Label(grocery_frame, text="Wheat", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
wheat.grid(row = 3, column = 0,  sticky = "w")

wheat_entry = Entry(grocery_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
wheat_entry.grid(row = 3, column = 1, pady = 6, padx = 10)
wheat_entry.insert(0,0)

#5
sugar = Label(grocery_frame, text="Sugar", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
sugar.grid(row = 4, column = 0,  sticky = "w")

sugar_entry = Entry(grocery_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
sugar_entry.grid(row = 4, column = 1, pady = 6, padx = 10)
sugar_entry.insert(0,0)

#6
tea = Label(grocery_frame, text="Tea", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
tea.grid(row = 5, column = 0,  sticky = "w")

tea_entry = Entry(grocery_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
tea_entry.grid(row = 5, column = 1, pady = 6, padx = 10)
tea_entry.insert(0,0)


#adding cold drink label frame
drink_frame = LabelFrame(product_frame,text="Cold-Drink", font=("times new roman", 15, "bold"),
                             bg = "gray20",fg = "gold", bd = 8, relief=RIDGE)
drink_frame.grid(row = 0, column = 2)

#1
red_bull = Label(drink_frame, text="Red Bull", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
red_bull.grid(row = 0, column = 0,  sticky = "w")

red_bull_entry = Entry(drink_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
red_bull_entry.grid(row = 0, column = 1, pady = 6, padx = 10)
red_bull_entry.insert(0,0)

#2
hurricane = Label(drink_frame, text="Hurricane", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
hurricane.grid(row = 1, column = 0,  sticky = "w")

hurricane_entry = Entry(drink_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
hurricane_entry.grid(row = 1, column = 1, pady = 6, padx = 10)
hurricane_entry.insert(0,0)
#3
blue_bull = Label(drink_frame, text="Blue Bull", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
blue_bull.grid(row = 2, column = 0,  sticky = "w")

blue_bull_entry = Entry(drink_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
blue_bull_entry.grid(row = 2, column = 1, pady = 6, padx = 10)
blue_bull_entry.insert(0,0)
#4
ocean = Label(drink_frame, text="Ocean", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
ocean.grid(row = 3, column = 0,  sticky = "w")
ocean_entry = Entry(drink_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
ocean_entry.grid(row = 3, column = 1, pady = 6, padx = 10)
ocean_entry.insert(0,0)

#5
monster = Label(drink_frame, text="Monster", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
monster.grid(row = 4, column = 0,  sticky = "w")

monster_entry = Entry(drink_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
monster_entry.grid(row = 4, column = 1, pady = 6, padx = 10)
monster_entry.insert(0,0)

#6
coca_cola = Label(drink_frame, text="Coca Cola", font=("times new roman", 15, "bold"),
                   bg = "gray20",fg = "white", bd = 6)
coca_cola.grid(row = 5, column = 0,  sticky = "w")

coca_cola_entry = Entry(drink_frame, bg = "white", bd = 8, relief=RIDGE, font=("arail", 18, "bold")
                   ,width = 5)
coca_cola_entry.grid(row = 5, column = 1, pady = 6, padx = 10)
coca_cola_entry.insert(0,0)



#creating bill frame
bill_frame = Frame(product_frame, bd = 8, relief=RIDGE)
bill_frame.grid(row=0, column = 3)

bill_area = Label(bill_frame, text="Billing Area", font = ("times new roman", 15, "bold"), bd = 7, relief=GROOVE)
bill_area.pack(fill = X)

#adding scrolllbar
scrollbar = Scrollbar(bill_frame, orient=VERTICAL, )
scrollbar.pack(side = RIGHT,fill= Y)

#adding text area
text_area = Text(bill_frame,height = 21, width = 80, yscrollcommand = scrollbar.set, wrap='word')
text_area.pack()

#LINKING SCROLL BAR WITH TEXT AREA FOR MOVING THE TEXT
scrollbar.config(command = text_area.yview)


#creating billl menu frame
billmenu_frame = LabelFrame(root, text = "Bill Menu", font = ("times new roman", 15, "bold"),
                            bd = 8, relief=RIDGE, bg = "gray20", fg = "gold")
billmenu_frame.pack(fill = X)

#1
cosmeticprice_label = Label(billmenu_frame, text = "Cosmetics Price", font=("times new roman", 15, "bold"),
                            bg = "gray20", fg = "white")
cosmeticprice_label.grid( row = 0, column = 0, padx = 10, sticky = "w")

cosmeticprice_entry = Entry(billmenu_frame, width = 10, font = ("times new roman", 15,"bold"),
                            bd = 8, relief = RIDGE)
cosmeticprice_entry.grid(row = 0, column = 1, pady = 10, padx = 8)

#2
groceriesprice_label = Label(billmenu_frame, text = "Groceries Price", font=("times new roman", 15, "bold"),
                            bg = "gray20", fg = "white")
groceriesprice_label.grid( row = 1, column = 0, padx = 10, sticky = "w")

groceriesprice_entry = Entry(billmenu_frame, width = 10, font = ("times new roman", 15,"bold"),
                            bd = 8, relief = RIDGE)
groceriesprice_entry.grid(row = 1, column = 1, pady = 10, padx = 8)

#3
drinkprice_label = Label(billmenu_frame, text = "Cold Drink Price", font=("times new roman", 15, "bold"),
                            bg = "gray20", fg = "white")
drinkprice_label.grid( row = 2, column = 0, padx = 10, sticky = "w")

drinkprice_entry = Entry(billmenu_frame, width = 10, font = ("times new roman", 15,"bold"),
                            bd = 8, relief = RIDGE)
drinkprice_entry.grid(row = 2, column = 1, pady = 10, padx = 8)

#cosmetic tax under billling frame

#1
cosmetictax_label = Label(billmenu_frame, text = "Cosmetics Tax", font=("times new roman", 15, "bold"),
                            bg = "gray20", fg = "white")
cosmetictax_label.grid( row = 0, column = 2, padx = 10, sticky = "w")

cosmetictax_entry = Entry(billmenu_frame, width = 10, font = ("times new roman", 15,"bold"),
                            bd = 8, relief = RIDGE)
cosmetictax_entry.grid(row = 0, column = 3, pady = 10, padx = 8)

#2
groceriestax_label = Label(billmenu_frame, text = "Groceries Tax", font=("times new roman", 15, "bold"),
                            bg = "gray20", fg = "white")
groceriestax_label.grid( row = 1, column = 2, padx = 10, sticky = "w")

groceriestax_entry = Entry(billmenu_frame, width = 10, font = ("times new roman", 15,"bold"),
                            bd = 8, relief = RIDGE)
groceriestax_entry.grid(row = 1, column = 3, pady = 10, padx = 8)


#3
drinktax_label = Label(billmenu_frame, text = "Cold Drink Tax", font=("times new roman", 15, "bold"),
                            bg = "gray20", fg = "white")
drinktax_label.grid( row = 2, column = 2, padx = 10, sticky = "w")

drinktax_entry = Entry(billmenu_frame, width = 10, font = ("times new roman", 15,"bold"),
                            bd = 8, relief = RIDGE)
drinktax_entry.grid(row = 2, column = 3, pady = 10, padx = 8)


#creatink button frame
buttonframe = Frame(billmenu_frame, bg = "white", bd = 8, relief=RIDGE)
buttonframe.grid(row = 0, column = 4,  rowspan = 3,padx=30)

#total button
totalbutton = Button(buttonframe, text="Total", bd = 8, relief= RIDGE, bg = "red", fg = "white"
                     ,font = ("arial", 16, "bold"),  width = 8, pady = 5, command= total)
totalbutton.grid(row = 0, column = 0, padx = 10, pady = 20)


billbutton = Button(buttonframe, text="Bill", bd = 8, relief= RIDGE, bg = "red", fg = "white"
                     ,font = ("arial", 16, "bold"),  width = 8, pady = 5, command=Bill_area)
billbutton.grid(row = 0, column = 1, padx = 10, pady = 20)


emailbutton = Button(buttonframe, text="Email", bd = 8, relief= RIDGE, bg = "red", fg = "white"
                     ,font = ("arial", 16, "bold"),  width = 8, pady = 5, command = send_email)
emailbutton.grid(row = 0, column = 2, padx = 10, pady = 20)


printbutton = Button(buttonframe, text="Print", bd = 8, relief= RIDGE, bg = "red", fg = "white"
                     ,font = ("arial", 16, "bold"),  width = 8, pady = 5, command = print_bill)
printbutton.grid(row = 0, column = 3, padx = 10, pady = 20)


clearbutton = Button(buttonframe, text="Clear", bd = 8, relief= RIDGE, bg = "red", fg = "white"
                     ,font = ("arial", 16, "bold"),  width = 8, pady = 5 , command = clear_bill)
clearbutton.grid(row = 0, column = 4, padx = 20, pady = 20)

# creating main window
root.mainloop()
