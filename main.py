from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib


def clear():
    chickenfryEntry.delete(0, END)
    chickenmasalaEntry.delete(0, END)
    chickencuryEntry.delete(0, END)
    chickenkolhapuriEntry.delete(0, END)
    muttonmasalaEntry.delete(0, END)
    muttoncuryEntry.delete(0, END)
    muttonfryEntry.delete(0, END)
    andamasalaEntry.delete(0, END)
    fishfryEntry.delete(0, END)

    daalfryEntry.delete(0, END)
    daaltadakaEntry.delete(0, END)
    shevbhajiEntry.delete(0, END)
    kajucuryEntry.delete(0, END)
    paneermasalaEntry.delete(0, END)
    greenpiceEntry.delete(0, END)
    vegbiryaniEntry.delete(0, END)
    vegpulauEntry.delete(0, END)
    paneerpulauEntry.delete(0,END)

    chapatiEntry.delete(0, END)
    jowarbhakriEntry.delete(0, END)
    bajaribhakriEntry.delete(0, END)
    tandurrotiEntry.delete(0, END)
    kadakbhariEntry.delete(0, END)
    buttertandurEntry.delete(0, END)
    ricehalfEntry.delete(0, END)
    ricefullEntry.delete(0, END)
    watarbottelEntry.delete(0, END)

    pepsiEntry.delete(0, END)
    spriteEntry.delete(0, END)
    cocacolaEntry.delete(0, END)
    stingEntry.delete(0, END)
    frootiEntry.delete(0, END)
    maazaEntry.delete(0, END)
    jeerasodaEntry.delete(0, END)
    mastaniEntry.delete(0, END)

    chickenfryEntry.insert(0, 0)
    chickenmasalaEntry.insert(0, 0)
    chickencuryEntry.insert(0, 0)
    chickenkolhapuriEntry.insert(0, 0)
    muttonmasalaEntry.insert(0, 0)
    muttoncuryEntry.insert(0, 0)
    muttonfryEntry.insert(0, 0)
    andamasalaEntry.insert(0, 0)
    fishfryEntry.insert(0, 0)

    daalfryEntry.insert(0, 0)
    daaltadakaEntry.insert(0, 0)
    shevbhajiEntry.insert(0, 0)
    kajucuryEntry.insert(0, 0)
    paneermasalaEntry.insert(0, 0)
    greenpiceEntry.insert(0, 0)
    vegbiryaniEntry.insert(0, 0)
    paneerpulauEntry.insert(0, 0)
    vegpulauEntry.insert(0, 0)

    chapatiEntry.insert(0, 0)
    jowarbhakriEntry.insert(0, 0)
    bajaribhakriEntry.insert(0, 0)
    tandurrotiEntry.insert(0, 0)
    kadakbhariEntry.insert(0, 0)
    buttertandurEntry.insert(0, 0)
    ricehalfEntry.insert(0, 0)
    ricefullEntry.insert(0, 0)
    watarbottelEntry.insert(0, 0)

    pepsiEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    cocacolaEntry.insert(0, 0)
    stingEntry.insert(0, 0)
    frootiEntry.insert(0, 0)
    maazaEntry.insert(0, 0)
    jeerasodaEntry.insert(0, 0)
    mastaniEntry.insert(0, 0)

    nonvegpriceEntry.delete(0, END)
    vegpriceEntry.delete(0, END)
    extraitemspriceEntry.delete(0, END)
    colddrinkspriceEntry.delete(0, END)

    nameEntry.delete(0, END)
    PhonenumberEntry.delete(0, END)
    BillNumberEntry.delete(0, END)

    textarea.delete(1.0, END)


def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, E)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent', parent=root1)
            root1.destroy()

        except:
            messagebox.showerror('Error', 'something went wrong, please try again', parent=root1)

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('send email')
        root1.config(bg='gray20')
        root1.resizable(0, 0)

        senderFrame = LabelFrame(root1, text='SENEDR', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel = Label(senderFrame, text="Sender`s Email", font=('arial', 14, 'bold'), bd=6, bg='gray20',
                            fg='white')
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bd=6, bg='gray20',
                              fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(recipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN, width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace('=', '').replace('-', '').replace('\t\t\t', '\t\t'))

        sendButton = Button(root1, text='SEND', font=('arial', 16, 'bold'), width=15, command=send_gmail)
        sendButton.grid(row=2, column=0, pady=20)

        root1.mainloop()


def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == BillNumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'bill number {billnumber} is saved successfully')
        billnumber = random.randint(1, 1000)


billnumber = random.randint(1, 1000)


def bill_area():
    if nameEntry.get() == '' or PhonenumberEntry.get() == '':
        messagebox.showerror('Error', 'please insert customers details ')
    elif nonvegpriceEntry.get() == '' and vegpriceEntry.get() == '' and extraitemspriceEntry.get() == '' and colddrinkspriceEntry.get() == '':
        messagebox.showerror('Error', 'no products are selected')
    elif nonvegpriceEntry.get() == '0 Rs' and vegpriceEntry.get() == '0 Rs' and extraitemspriceEntry.get() == '0 Rs' and colddrinkspriceEntry.get() == '0Rs':
        messagebox.showerror('Error', 'no products are selected')

    else:
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t**welcome TO our Hotel**\n')
        textarea.insert(END, f'\nBill Number: {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END, f'\nCustomer phone number: {PhonenumberEntry.get()}\n')
        textarea.insert(END, '\n===============================================')
        textarea.insert(END, 'product\t\t\tQuantity\t\tPrice')
        textarea.insert(END, '\n===============================================')
    if chickenfryEntry.get() != '0':
        textarea.insert(END, f'\nChicken Fry\t\t\t{chickenfryEntry.get()}\t\t{chickenfryprice} Rs')
    if chickencuryEntry.get() != '0':
        textarea.insert(END, f'\nChicken Cury\t\t\t{chickencuryEntry.get()}\t\t{chickencuryprice} Rs')
    if chickenmasalaEntry.get() != '0':
        textarea.insert(END, f'\nChicken Masala\t\t\t{chickenmasalaEntry.get()}\t\t{chickenmasalaprice} Rs')
    if chickenkolhapuriEntry.get() != '0':
        textarea.insert(END, f'\nChicken Kolhapuri\t\t\t{chickenkolhapuriEntry.get()}\t\t{chickenkolhapuriprice} Rs')
    if muttonmasalaEntry.get() != '0':
        textarea.insert(END, f'\nMutton Masala\t\t\t{muttonmasalaEntry.get()}\t\t{muttonmasalaprice} Rs')
    if muttonfryEntry.get() != '0':
        textarea.insert(END, f'\nMutton Fry\t\t\t{muttonfryEntry.get()}\t\t{muttonfryprice} Rs')
    if fishfryEntry.get() != '0':
        textarea.insert(END, f'\nFish Fry\t\t\t{fishfryEntry.get()}\t\t{fishfryprice} Rs')
    if andamasalaEntry.get() != '0':
        textarea.insert(END, f'\nAnda Masala\t\t\t{andamasalaEntry.get()}\t\t{andamasalaprice} Rs')
    if muttoncuryEntry.get() != '0':
        textarea.insert(END, f'\nMutton Cury\t\t\t{muttoncuryEntry.get()}\t\t{muttoncuryprice} Rs')

    if daalfryEntry.get() != '0':
        textarea.insert(END, f'\nDaal Fry\t\t\t{daalfryEntry.get()}\t\t{daalfryprice} Rs')
    if daaltadakaEntry.get() != '0':
        textarea.insert(END, f'\nDaalTadaka\t\t\t{daaltadakaEntry.get()}\t\t{daaltadakaprice} Rs')
    if shevbhajiEntry.get() != '0':
        textarea.insert(END, f'\nShevbhaji\t\t\t{shevbhajiEntry.get()}\t\t{shevbhajiprice} Rs')
    if kajucuryEntry.get() != '0':
        textarea.insert(END, f'\nKaju Cury\t\t\t{kajucuryEntry.get()}\t\t{kajucuryprice} Rs')
    if paneermasalaEntry.get() != '0':
        textarea.insert(END, f'\nPaneer Masala\t\t\t{paneermasalaEntry.get()}\t\t{pannermasalaprice} Rs')
    if greenpiceEntry.get() != '0':
        textarea.insert(END, f'\nGreen Pice\t\t\t{greenpiceEntry.get()}\t\t{greenpiceprice} Rs')
    if vegbiryaniEntry.get() != '0':
        textarea.insert(END, f'\nVeg Biryani\t\t\t{vegbiryaniEntry.get()}\t\t{vegbiryaniprice} Rs')
    if vegpulauEntry.get() != '0':
        textarea.insert(END, f'\nVeg Pulau\t\t\t{vegpulauEntry.get()}\t\t{vegpulauprice} Rs')
    if paneerpulauEntry.get() != '0':
        textarea.insert(END, f'\nPaneer Pulau\t\t\t{paneerpulauEntry.get()}\t\t{paneerpulauprice} Rs')

    if chapatiEntry.get() != '0':
        textarea.insert(END, f'\nChapati\t\t\t{chapatiEntry.get()}\t\t{chapatiprice} Rs')
    if jowarbhakriEntry.get() != '0':
        textarea.insert(END, f'\nJowar Bhakari\t\t\t{jowarbhakriEntry.get()}\t\t{jowarbhakariprice} Rs')
    if bajaribhakriEntry.get() != '0':
        textarea.insert(END, f'\nBajari Bhakari\t\t\t{bajaribhakriEntry.get()}\t\t{bajaribhakariprice} Rs')
    if tandurrotiEntry.get() != '0':
        textarea.insert(END, f'\nTandur Roti\t\t\t{tandurrotiEntry.get()}\t\t{tandurrotiprice} Rs')
    if kadakbhariEntry.get() != '0':
        textarea.insert(END, f'\nKadak Bhakari\t\t\t{kadakbhariEntry.get()}\t\t{kadakbhakariprice} Rs')
    if buttertandurEntry.get() != '0':
        textarea.insert(END, f'\nButter Tandur\t\t\t{buttertandurEntry.get()}\t\t{buttertandurprice} Rs')
    if ricehalfEntry.get() != '0':
        textarea.insert(END, f'\nRice Half\t\t\t{ricehalfEntry.get()}\t\t{halfriceprice} Rs')
    if ricefullEntry.get() != '0':
        textarea.insert(END, f'\nRice Full\t\t\t{ricefullEntry.get()}\t\t{fullriceprice} Rs')
    if watarbottelEntry.get() != '0':
        textarea.insert(END, f'\nWater Bottel\t\t\t{watarbottelEntry.get()}\t\t{waterbottelprice} Rs')

    if maazaEntry.get() != '0':
        textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t{maazaprice} Rs')
    if pepsiEntry.get() != '0':
        textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t{pepsiprice} Rs')
    if spriteEntry.get() != '0':
        textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t{spriteprice} Rs')
    if stingEntry.get() != '0':
        textarea.insert(END, f'\nSting\t\t\t{stingEntry.get()}\t\t{stingprice} Rs')
    if frootiEntry.get() != '0':
        textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t{frootiprice} Rs')
    if cocacolaEntry.get() != '0':
        textarea.insert(END, f'\nCoca Cola\t\t\t{cocacolaEntry.get()}\t\t{cocacolaprice} Rs')
    if mastaniEntry.get() != '0':
        textarea.insert(END, f'\nMastani\t\t\t{mastaniEntry.get()}\t\t{mastaniprice} Rs')
    if jeerasodaEntry.get() != '0':
        textarea.insert(END, f'\nJeera Soda\t\t\t{jeerasodaEntry.get()}\t\t{jeerasodaprice} Rs')
    textarea.insert(END, '\n-----------------------------------------------')
    textarea.insert(END, f'\nTotal Bill \t=\t\t\t\t{totalbill}Rs')
    textarea.insert(END, '\n-----------------------------------------------')
    textarea.insert(END, '\t\t\t**... Visit Again ...**\n')
    save_bill()


def total():
    global chickenfryprice, chickenmasalaprice, chickencuryprice, chickenkolhapuriprice, muttonmasalaprice, muttonfryprice, muttoncuryprice, fishfryprice, andamasalaprice
    global daalfryprice, daaltadakaprice, shevbhajiprice, kajucuryprice, pannermasalaprice, greenpiceprice, vegbiryaniprice, vegpulauprice, paneerpulauprice
    global chapatiprice, jowarbhakariprice, bajaribhakariprice, tandurrotiprice, kadakbhakariprice, buttertandurprice, halfriceprice, fullriceprice, waterbottelprice
    global maazaprice, pepsiprice, spriteprice, stingprice, frootiprice, jeerasodaprice, mastaniprice, cocacolaprice
    global totalbill
    chickenfryprice = int(chickenfryEntry.get()) * 140
    chickenmasalaprice = int(chickenmasalaEntry.get()) *140
    chickencuryprice = int(chickencuryEntry.get()) * 140
    chickenkolhapuriprice = int(chickenkolhapuriEntry.get()) * 160
    muttonmasalaprice = int(muttonmasalaEntry.get()) *210
    muttonfryprice = int(muttonfryEntry.get()) * 190
    muttoncuryprice = int(muttoncuryEntry.get()) * 200
    fishfryprice = int(fishfryEntry.get()) * 150
    andamasalaprice = int(andamasalaEntry.get()) * 100

    totalnonvegprice = chickenfryprice + chickenmasalaprice + chickencuryprice + chickenkolhapuriprice + muttonmasalaprice + muttonfryprice + muttoncuryprice + fishfryprice + andamasalaprice
    nonvegpriceEntry.delete(0, END)
    nonvegpriceEntry.insert(0, f'{totalnonvegprice}Rs')

    daalfryprice = int(daalfryEntry.get()) * 80
    daaltadakaprice = int(daaltadakaEntry.get()) * 90
    shevbhajiprice = int(shevbhajiEntry.get()) * 90
    kajucuryprice = int(kajucuryEntry.get()) * 150
    pannermasalaprice = int(paneermasalaEntry.get()) * 150
    greenpiceprice = int(greenpiceEntry.get()) * 120
    vegbiryaniprice = int(vegbiryaniEntry.get()) * 120
    vegpulauprice = int(vegpulauEntry.get()) * 100
    paneerpulauprice = int(paneerpulauEntry.get()) * 120

    totalvegprice = daalfryprice + daaltadakaprice + shevbhajiprice + kajucuryprice + pannermasalaprice + greenpiceprice + vegbiryaniprice + vegpulauprice + paneerpulauprice
    vegpriceEntry.delete(0, END)
    vegpriceEntry.insert(0, str(totalvegprice) + 'Rs')

    chapatiprice = int(chapatiEntry.get()) * 20
    jowarbhakariprice = int(jowarbhakriEntry.get()) * 20
    bajaribhakariprice = int(bajaribhakriEntry.get()) * 20
    tandurrotiprice = int(tandurrotiEntry.get()) * 15
    kadakbhakariprice = int(kadakbhariEntry.get()) * 20
    buttertandurprice = int(buttertandurEntry.get()) * 20
    halfriceprice = int(ricehalfEntry.get()) * 80
    fullriceprice = int(ricefullEntry.get()) * 80
    waterbottelprice = int(watarbottelEntry.get()) * 20

    totalextraitemsprice = chapatiprice + jowarbhakariprice + bajaribhakariprice + tandurrotiprice + kadakbhakariprice + buttertandurprice + halfriceprice + fullriceprice + waterbottelprice

    extraitemspriceEntry.delete(0, END)
    extraitemspriceEntry.insert(0, str(totalextraitemsprice) + 'Rs')

    maazaprice = int(maazaEntry.get()) * 20
    pepsiprice = int(pepsiEntry.get()) * 20
    spriteprice = int(spriteEntry.get()) * 20
    stingprice = int(stingEntry.get()) * 20
    frootiprice = int(frootiEntry.get()) * 20
    cocacolaprice = int(cocacolaEntry.get()) * 20
    jeerasodaprice = int(jeerasodaEntry.get()) * 20
    mastaniprice = int(mastaniEntry.get()) * 90

    totalcolddrinkscprice = maazaprice + pepsiprice + spriteprice + stingprice + frootiprice + cocacolaprice + jeerasodaprice + mastaniprice
    colddrinkspriceEntry.delete(0, END)
    colddrinkspriceEntry.insert(0, str(totalcolddrinkscprice) + 'Rs')

    totalbill = totalnonvegprice + totalvegprice + totalcolddrinkscprice + totalextraitemsprice


root = Tk()
root.title('Hotel Zayka')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
headingLabel = Label(root, text='**-Hotel Zayka-**', font=('times new roman', 30, 'bold'), bg='gold', fg='black',
                     bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'), fg='black',
                                    bd=8, relief=GROOVE, bg='slateblue1')
customer_details_frame.pack()

nameLabel = Label(customer_details_frame, text='Name:-', font=('times new roman', 15, 'bold'), bg='cyan', fg='black')
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8, pady=2)

PhonenumberLabel = Label(customer_details_frame, text='PhoneNumber:-', font=('times new roman', 15, 'bold'), bg='cyan',
                         fg='black')
PhonenumberLabel.grid(row=0, column=2, padx=20)

PhonenumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
PhonenumberEntry.grid(row=0, column=3, padx=8)

BillNumberLabel = Label(customer_details_frame, text='BillNumber:-', font=('times new roman', 15, 'bold'), bg='cyan',
                        fg='black')
BillNumberLabel.grid(row=0, column=4, padx=20)

BillNumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
BillNumberEntry.grid(row=0, column=5, padx=8)

searchButton = Button(customer_details_frame, text='SEARCH', font=('arial', 12, 'bold'), bd=7, width=8,command=search_bill)
searchButton.grid(row=0, column=6, padx=10, pady=8,)


productFrame = Frame(root)
productFrame.pack()

nonvegFrame = LabelFrame(productFrame, text='NonVeg', font=('times new roman', 15, 'bold'), fg='black', bd=8,
                         relief=GROOVE, bg='tomato')
nonvegFrame.grid(row=0, column=0)

chickenfryLabel = Label(nonvegFrame, text='Chicken Fry', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                        relief=GROOVE, bg='gold')
chickenfryLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

chickenfryEntry = Entry(nonvegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
chickenfryEntry.grid(row=0, column=1, pady=9, padx=10, sticky='w')
chickenfryEntry.insert(0,0)

chickenmasalaLabel = Label(nonvegFrame, text='Chicken Masala', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                           relief=GROOVE, bg='gold')
chickenmasalaLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

chickenmasalaEntry = Entry(nonvegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
chickenmasalaEntry.grid(row=1, column=1, pady=9, padx=10, sticky='w')
chickenmasalaEntry.insert(0,0)

chickencuryLabel = Label(nonvegFrame, text='Chicken Cury', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                         relief=GROOVE, bg='gold')
chickencuryLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

chickencuryEntry = Entry(nonvegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
chickencuryEntry.grid(row=2, column=1, pady=9, padx=10, sticky='w')
chickencuryEntry.insert(0,0)

chickenkolhapuriLabel = Label(nonvegFrame, text='Chicken Kolhapuri', font=('times new roman', 15, 'bold'), fg='black',
                              bd=4, relief=GROOVE, bg='gold')
chickenkolhapuriLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

chickenkolhapuriEntry = Entry(nonvegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
chickenkolhapuriEntry.grid(row=3, column=1, pady=9, padx=10, sticky='w')
chickenkolhapuriEntry.insert(0,0)

muttonmasalaLabel = Label(nonvegFrame, text='Mutton Masala', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                          relief=GROOVE, bg='gold')
muttonmasalaLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

muttonmasalaEntry = Entry(nonvegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
muttonmasalaEntry.grid(row=4, column=1, pady=9, padx=10, sticky='w')
muttonmasalaEntry.insert(0,0)

muttonfryLabel = Label(nonvegFrame, text='Mutton Fry', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                       relief=GROOVE, bg='gold')
muttonfryLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

muttonfryEntry = Entry(nonvegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
muttonfryEntry.grid(row=5, column=1, pady=9, padx=10, sticky='w')
muttonfryEntry.insert(0,0)

muttoncuryLabel = Label(nonvegFrame, text='Mutton Cury', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                        relief=GROOVE, bg='gold')
muttoncuryLabel.grid(row=6, column=0, pady=9, padx=10, sticky='w')

muttoncuryEntry = Entry(nonvegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
muttoncuryEntry.grid(row=6, column=1, pady=9, padx=10, sticky='w')
muttoncuryEntry.insert(0,0)

fishfryLabel = Label(nonvegFrame, text='Fish Fry', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                     relief=GROOVE, bg='gold')
fishfryLabel.grid(row=7, column=0, pady=9, padx=10, sticky='w')

fishfryEntry = Entry(nonvegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
fishfryEntry.grid(row=7, column=1, pady=9, padx=10, sticky='w')
fishfryEntry.insert(0,0)

andamasalaLabel = Label(nonvegFrame, text='Anda Masala', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                        relief=GROOVE, bg='gold')
andamasalaLabel.grid(row=8, column=0, pady=9, padx=10, sticky='w')

andamasalaEntry = Entry(nonvegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
andamasalaEntry.grid(row=8, column=1, pady=9, padx=10, sticky='w')
andamasalaEntry.insert(0,0)
# veg items

vegFrame = LabelFrame(productFrame, text='Veg', font=('times new roman', 15, 'bold'), fg='black', bd=4, relief=GROOVE,
                      bg='spring green')
vegFrame.grid(row=0, column=1)

daalfryLabel = Label(vegFrame, text='Daal Fry', font=('times new roman', 15, 'bold'), fg='black', bd=4, relief=GROOVE,
                     bg='gold')
daalfryLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

daalfryEntry = Entry(vegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
daalfryEntry.grid(row=0, column=1, pady=9, padx=10, sticky='w')
daalfryEntry.insert(0,0)

daalyadakaLabel = Label(vegFrame, text='Daal Tadaka', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                        relief=GROOVE, bg='gold')
daalyadakaLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

daaltadakaEntry = Entry(vegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
daaltadakaEntry.grid(row=1, column=1, pady=9, padx=10, sticky='w')
daaltadakaEntry.insert(0,0)

shevbhajiLabel = Label(vegFrame, text='Shevbhaji', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                       relief=GROOVE, bg='gold')
shevbhajiLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

shevbhajiEntry = Entry(vegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
shevbhajiEntry.grid(row=2, column=1, pady=9, padx=10, sticky='w')
shevbhajiEntry.insert(0,0)

kajucuryLabel = Label(vegFrame, text='KajuCury', font=('times new roman', 15, 'bold'), fg='black', bd=4, relief=GROOVE,
                      bg='gold')
kajucuryLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

kajucuryEntry = Entry(vegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
kajucuryEntry.grid(row=3, column=1, pady=9, padx=10, sticky='w')
kajucuryEntry.insert(0,0)

paneermasalaLabel = Label(vegFrame, text='Paneer Masala', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                          relief=GROOVE, bg='gold')
paneermasalaLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

paneermasalaEntry = Entry(vegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
paneermasalaEntry.grid(row=4, column=1, pady=9, padx=10, sticky='w')
paneermasalaEntry.insert(0,0)

greenpiceLabel = Label(vegFrame, text='Green Pice', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                       relief=GROOVE, bg='gold')
greenpiceLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

greenpiceEntry = Entry(vegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
greenpiceEntry.grid(row=5, column=1, pady=9, padx=10, sticky='w')
greenpiceEntry.insert(0,0)

vegbiryaniLabel = Label(vegFrame, text='Veg Biryani', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                        relief=GROOVE, bg='gold')
vegbiryaniLabel.grid(row=6, column=0, pady=9, padx=10, sticky='w')

vegbiryaniEntry = Entry(vegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
vegbiryaniEntry.grid(row=6, column=1, pady=9, padx=10, sticky='w')
vegbiryaniEntry.insert(0,0)

vegpulauLabel = Label(vegFrame, text='Veg Pulau', font=('times new roman', 15, 'bold'), fg='black', bd=4, relief=GROOVE,
                      bg='gold')
vegpulauLabel.grid(row=7, column=0, pady=9, padx=10, sticky='w')

vegpulauEntry = Entry(vegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
vegpulauEntry.grid(row=7, column=1, pady=9, padx=10, sticky='w')
vegpulauEntry.insert(0,0)

paneerpulauLabel = Label(vegFrame, text='Paneer Pulau', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                         relief=GROOVE, bg='gold')
paneerpulauLabel.grid(row=8, column=0, pady=9, padx=10, sticky='w')

paneerpulauEntry = Entry(vegFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
paneerpulauEntry.grid(row=8, column=1, pady=9, padx=10, sticky='w')
paneerpulauEntry.insert(0,0 )
# Extra Items

extraitemsFrame = LabelFrame(productFrame, text='Extra Items', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                             relief=GROOVE, bg='deep sky blue')
extraitemsFrame.grid(row=0, column=2)

chapatiLabel = Label(extraitemsFrame, text='Chapati', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                     relief=GROOVE, bg='gold')
chapatiLabel.grid(row=0, column=0, pady=9, padx=10)

chapatiEntry = Entry(extraitemsFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
chapatiEntry.grid(row=0, column=1, pady=9, padx=10)
chapatiEntry.insert(0,0)

jowarbhakriLabel = Label(extraitemsFrame, text='Jowar Bhakari', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                         relief=GROOVE, bg='gold')
jowarbhakriLabel.grid(row=1, column=0, pady=9, padx=10)

jowarbhakriEntry = Entry(extraitemsFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
jowarbhakriEntry.grid(row=1, column=1, pady=9, padx=10)
jowarbhakriEntry.insert(0,0)

bajaribhakriLabel = Label(extraitemsFrame, text='Bajari Bhakari', font=('times new roman', 15, 'bold'), fg='black',
                          bd=4, relief=GROOVE, bg='gold')
bajaribhakriLabel.grid(row=2, column=0, pady=9, padx=10)

bajaribhakriEntry = Entry(extraitemsFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
bajaribhakriEntry.grid(row=2, column=1, pady=9)
bajaribhakriEntry.insert(0,0)

tandurrotiLabel = Label(extraitemsFrame, text='Tandur Roti', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                        relief=GROOVE, bg='gold')
tandurrotiLabel.grid(row=3, column=0, pady=9, padx=10)

tandurrotiEntry = Entry(extraitemsFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
tandurrotiEntry.grid(row=3, column=1, pady=9, padx=10)
tandurrotiEntry.insert(0,0)

kadakbhariLabel = Label(extraitemsFrame, text='Kadak Bhakari', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                        relief=GROOVE, bg='gold')
kadakbhariLabel.grid(row=4, column=0, pady=9, padx=10)

kadakbhariEntry = Entry(extraitemsFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
kadakbhariEntry.grid(row=4, column=1, pady=9, padx=10)
kadakbhariEntry.insert(0,0)

buttertandurLabel = Label(extraitemsFrame, text='Butter Tandur', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                          relief=GROOVE, bg='gold')
buttertandurLabel.grid(row=5, column=0, pady=9, padx=10)

buttertandurEntry = Entry(extraitemsFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
buttertandurEntry.grid(row=5, column=1, pady=9, padx=10)
buttertandurEntry.insert(0,0)

ricehalfLabel = Label(extraitemsFrame, text='Half Rice', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                      relief=GROOVE, bg='gold')
ricehalfLabel.grid(row=6, column=0, pady=9, padx=10)

ricehalfEntry = Entry(extraitemsFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
ricehalfEntry.grid(row=6, column=1, pady=9, padx=10)
ricehalfEntry.insert(0,0)

ricefullLabel = Label(extraitemsFrame, text='Full Rice', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                      relief=GROOVE, bg='gold')
ricefullLabel.grid(row=7, column=0, pady=9, padx=10)

ricefullEntry = Entry(extraitemsFrame, font=('time new roman', 15, 'bold'), width=8, bd=4)
ricefullEntry.grid(row=7, column=1, pady=9, padx=10)
ricefullEntry.insert(0,0)

watarbottelLabel = Label(extraitemsFrame, text='Water Bottel', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                         relief=GROOVE, bg='gold')
watarbottelLabel.grid(row=8, column=0, pady=9, padx=10)

watarbottelEntry = Entry(extraitemsFrame, font=('time new roman', 15, 'bold'), width=7, bd=5)
watarbottelEntry.grid(row=8, column=1, pady=9, padx=10)
watarbottelEntry.insert(0,0)

# cold drinks

colddrinksFrame = LabelFrame(productFrame, text='Cold Drinks', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                             relief=GROOVE, bg='hot pink')
colddrinksFrame.grid(row=0, column=3)

stingLabel = Label(colddrinksFrame, text='Sting', font=('times new roman', 15, 'bold'), fg='black', bd=4, relief=GROOVE,
                   bg='gold')
stingLabel.grid(row=0, column=0, pady=9, padx=10)

stingEntry = Entry(colddrinksFrame, font=('time new roman', 15, 'bold'), width=5, bd=5)
stingEntry.grid(row=0, column=1, pady=9, padx=10)
stingEntry.insert(0,0)

spriteLabel = Label(colddrinksFrame, text='Sprite', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                    relief=GROOVE, bg='gold')
spriteLabel.grid(row=1, column=0, pady=9, padx=10)

spriteEntry = Entry(colddrinksFrame, font=('time new roman', 15, 'bold'), width=5, bd=5)
spriteEntry.grid(row=1, column=1, pady=9, padx=10)
spriteEntry.insert(0,0)

frootiLabel = Label(colddrinksFrame, text='Frooti', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                    relief=GROOVE, bg='gold')
frootiLabel.grid(row=2, column=0, pady=9, padx=10)

frootiEntry = Entry(colddrinksFrame, font=('time new roman', 15, 'bold'), width=5, bd=5)
frootiEntry.grid(row=2, column=1, pady=9, padx=10)
frootiEntry.insert(0,0)

maazaLabel = Label(colddrinksFrame, text='Maaza', font=('times new roman', 15, 'bold'), fg='black', bd=4, relief=GROOVE,
                   bg='gold')
maazaLabel.grid(row=3, column=0, pady=9, padx=10)

maazaEntry = Entry(colddrinksFrame, font=('time new roman', 15, 'bold'), width=5, bd=5)
maazaEntry.grid(row=3, column=1, pady=9, padx=10)
maazaEntry.insert(0,0)

cocacolaLabel = Label(colddrinksFrame, text='Coca Cola', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                      relief=GROOVE, bg='gold')
cocacolaLabel.grid(row=4, column=0, pady=9, padx=10)

cocacolaEntry = Entry(colddrinksFrame, font=('time new roman', 15, 'bold'), width=5, bd=5)
cocacolaEntry.grid(row=4, column=1, pady=9, padx=10)
cocacolaEntry.insert(0,0)

pepsiLabel = Label(colddrinksFrame, text='Pepsi', font=('times new roman', 15, 'bold'), fg='black', bd=4, relief=GROOVE,
                   bg='gold')
pepsiLabel.grid(row=5, column=0, pady=9, padx=10)

pepsiEntry = Entry(colddrinksFrame, font=('time new roman', 15, 'bold'), width=5, bd=5)
pepsiEntry.grid(row=5, column=1, pady=9, padx=10)
pepsiEntry.insert(0,0)

jeerasodaLabel = Label(colddrinksFrame, text='Jeera Soda', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                       relief=GROOVE, bg='gold')
jeerasodaLabel.grid(row=6, column=0, pady=9, padx=10)

jeerasodaEntry = Entry(colddrinksFrame, font=('time new roman', 15, 'bold'), width=5, bd=5)
jeerasodaEntry.grid(row=6, column=1, pady=9, padx=10)
jeerasodaEntry.insert(0,0)

mastaniLabel = Label(colddrinksFrame, text='Mastani', font=('times new roman', 15, 'bold'), fg='black', bd=4,
                     relief=GROOVE, bg='gold')
mastaniLabel.grid(row=7, column=0, pady=9, padx=10)

mastaniEntry = Entry(colddrinksFrame, font=('time new roman', 15, 'bold'), width=5, bd=5)
mastaniEntry.grid(row=7, column=1, pady=9, padx=10)
mastaniEntry.insert(0,0)

billframe = Frame(productFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=4,padx=10)

billareaLabel = Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=4, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billframe, height=25, width=47, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'), fg='gold', bd=8, relief=GROOVE,
                           bg='gray20')
billmenuFrame.pack()

nonvegpriceLabel = Label(billmenuFrame, text='NonVeg Price', font=('times new roman', 14, 'bold'), bg='gray20',
                         fg='white')
nonvegpriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')

nonvegpriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
nonvegpriceEntry.grid(row=0, column=1, pady=6, padx=10)

vegpriceLabel = Label(billmenuFrame, text='Veg Price', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
vegpriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')

vegpriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
vegpriceEntry.grid(row=1, column=1, pady=6, padx=10)

extraitemspriceLabel = Label(billmenuFrame, text='Extra Items Price', font=('times new roman', 14, 'bold'), bg='gray20',
                             fg='white')
extraitemspriceLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')

extraitemspriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
extraitemspriceEntry.grid(row=0, column=3, pady=6, padx=10)

colddrinkspriceLabel = Label(billmenuFrame, text='Cold DrinksPrice', font=('times new roman', 14, 'bold'), bg='gray20',
                             fg='white')
colddrinkspriceLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')

colddrinkspriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
colddrinkspriceEntry.grid(row=1, column=3, pady=6, padx=10)

buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                     pady=10, command=total)
totalButton.grid(row=0, column=0, padx=5, pady=20)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                    pady=10, command=bill_area)
billButton.grid(row=0, column=1, padx=5, pady=20)

emailButton = Button(buttonFrame, text='E-mail', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                     pady=10, command=send_email)
emailButton.grid(row=0, column=2, padx=5, pady=20)

printout = Button(buttonFrame, text='PRINT', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                  pady=10, command=print_bill)
printout.grid(row=0, column=3, padx=5, pady=20)

clearbutton = Button(buttonFrame, text='CLEAR', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                     pady=10, command=clear)
clearbutton.grid(row=0, column=4, padx=5, pady=20)

root.mainloop()
