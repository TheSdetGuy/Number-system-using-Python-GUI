import tkinter as tk
from tkinter import Canvas
window = tk.Tk()
window.geometry("540x800")
window.configure(background="powder blue")
window.wm_title("Number System")
Base_Number=""

background_image=tk.PhotoImage(file="1.png")
background_label1=tk.Label(window,image=background_image)
background_label1.place(x=0,y=0,relwidth=1,relheight=1)
#===============================Function to calculate =======================================#
def evaluate(event):
    if Base_Number == "Binary":     #For Binary to another
        try:
            dec = int(Myentry.get(),2)
            mybin=bin(dec).lstrip("0b")
            mydec=str(dec)
            myhex = hex(dec).lstrip("0x")
            myoct=oct(dec).lstrip("0o")
            out1.insert(0.0,mybin)
            out2.insert(0.0,mydec)
            out3.insert(0.0,myoct)
            out4.insert(0.0,myhex)
            
        except ValueError:
            result1.configure(text = "Please enter valid Binary",font="arial 16 bold")
    elif Base_Number == "Decimal":  #For decimal to another
        try:
            dec = int(Myentry.get(),10)
            mybin=bin(dec).lstrip("0b")
            mydec=str(dec)
            myhex = hex(dec).lstrip("0x")
            myoct=oct(dec).lstrip("0o")
            out1.insert(0.0,mybin)
            out2.insert(0.0,mydec)
            out3.insert(0.0,myoct)
            out4.insert(0.0,myhex)
        except ValueError:
            result1.configure(text = "Please enter valid Decimal",font="arial 16 bold")

    elif Base_Number == "Hex":  #For HexaDecimal to another
        try:
            dec =int(Myentry.get(),16)
            mybin=bin(dec).lstrip("0b")
            mydec=str(dec)
            myhex = hex(dec).lstrip("0x")
            myoct=oct(dec).lstrip("0o")
            out1.insert(0.0,mybin)
            out2.insert(0.0,mydec)
            out3.insert(0.0,myoct)
            out4.insert(0.0,myhex)
        except ValueError:
            result1.configure(text = "Please enter valid Hexadecimal",font="arial 16 bold")
    elif Base_Number =="Octal":     #For Octal to another
        try:
            dec =int(Myentry.get(),8)
            mybin=bin(dec).lstrip("0b")
            mydec=str(dec)
            myhex = hex(dec).lstrip("0x")
            myoct=oct(dec).lstrip("0o")
            out1.insert(0.0,mybin)
            out2.insert(0.0,mydec)
            out3.insert(0.0,myoct)
            out4.insert(0.0,myhex)
        except ValueError:
            result1.configure(text = "Please enter valid Octal",font="arial 16 bold")
    else:
        result1.configure(text = "Please select a BASE!",font="arial 18 bold")

#===================================Explanation window==========================================#
def binarywin():
    # create child window
    win = tk.Toplevel()
    # display message
    message = "A Binary number is always of base 2\n and it constists of 0 and 1.\n"
    tk.Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    tk.Button(win, text='OK', command=win.destroy).pack() 

def decwin():
    # create child window
    win = tk.Toplevel()
    # display message
    message = "A Binary number is always of base 10\n and it constists of 0 to 9.\n"
    tk.Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    tk.Button(win, text='OK', command=win.destroy).pack() 

def octalwin():
    # create child window
    win = tk.Toplevel()
    # display message
    message = "A Binary number is always of base 8\n and it constists of 0 to 7.\n"
    tk.Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    tk.Button(win, text='OK', command=win.destroy).pack() 
    
def hexwin():
    # create child window
    win = tk.Toplevel()
    # display message
    message = "A Binary number is always of base 16\n and it constists of 0 to 9 and A to F.\n"
    tk.Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    tk.Button(win, text='OK', command=win.destroy).pack() 
    
#===============================Function to show info about us===========================================#
def aboutus():
    # create child window
    win = tk.Toplevel()
    # display message
    message = "This project is done by Debasis Jana, student of Lovely Professional University of \nComputer Science and Engineering Department"
    tk.Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    tk.Button(win, text='OK', command=win.destroy).pack() 
        
#============================Function to Reset Entry Filed=====================#

    
def e1_delete():
    Myentry.delete(first=0,last=100)
def deltxt():
    out1.delete(1.0,tk.END)
    out2.delete(1.0,tk.END)
    out3.delete(1.0,tk.END)
    out4.delete(1.0,tk.END)
#============================Function for About Project============================#
def aboutpr():
    # create child window
    win = tk.Toplevel()
    # display message
    message = "In this project you will be able to find the other base of a number.\nFor that you have to first choose THE BASE of the number (input field) and then in the input field\ntype the number according to the base and press enter.\n\nFor Explanation click on EXPLAIN button in the result field\n\nCongrats! You got the right answer!"
   
    tk.Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    tk.Button(win, text='OK', command=win.destroy).pack()    

#=====================================Global Variable Declaration==========================================#

def calcStyle():
    global Base_Number
    Base_Number=base.get()
    #print(base.get())
#===================================================================================================#
MyTitle = tk.Label(window)
MyTitle.pack()
#==================================Entry Field======================================================#
Myentry=tk.Entry(window,font="arial 26 bold",fg='white',bg='green',
                 justify='right',bd=50)
Myentry.bind("<Return>", evaluate)
Myentry.pack()
#====================================Label========================================#
label1=tk.Label(window,text="Enter value and press Enter",font="arial 14 bold",fg="brown",bg="powder blue",pady=10,padx=20)
label1.place(x=127,y=170)
result1=tk.Label(window,text="Choose a Base",font="arial 26 bold",bg="blue",fg="white",pady=10,padx=20)
result1.place(x=125,y=220)
#=========================Button to choose base of the number===========================================#

base = tk.StringVar()

btn1=tk.Radiobutton(window,padx=61,pady=3,bd=8,fg='black',font="arial 15 bold",bg="powder blue",
                   text='Binary',variable=base,value="Binary",command=calcStyle).place(x=45,y=300)

btn2=tk.Radiobutton(window,padx=32,pady=3,bd=8,fg='black',font="arial 15 bold",bg="powder blue",
                   text='Decimal',variable=base,value="Decimal",command=calcStyle).place(x=285,y=300)

btn3=tk.Radiobutton(window,padx=27,pady=3,bd=8,fg='black',font="arial 15 bold",bg="powder blue",
                   text='Hexa Decimal',variable=base,value="Hex",command=calcStyle).place(x=45,y=350)


btn4=tk.Radiobutton(window,padx=45,pady=3,bd=8,fg='black',font="arial 15 bold",bg="powder blue",
                   text='Octal',variable=base,value="Octal",command=calcStyle).place(x=285,y=350)

label2=tk.Label(window,text="Result",font="arial 15 bold",bg="black",fg="white",pady=10,padx=20)
label2.place(x=250,y=420)

#==================================Output Text Box Field=========================================================================#

l1=tk.Label(window,text="Binary",font="arial 15 bold",bg="green",fg="white",pady=8,padx=52)
l1.place(x=10,y=470)
out1=tk.Text(window,width=18,height=2,font="arial 15 bold",fg="purple",bg="pink")
out1.place(x=200,y=470)
tk.Button(window, text='Explain',padx=27,pady=10,bd=8,fg='white',font="arial 8 bold",bg="black", command=binarywin).place(x=425,y=470)

l2=tk.Label(window,text="Decimal",font="arial 15 bold",bg="green",fg="white",pady=8,padx=45)
l2.place(x=10,y=520)
out2=tk.Text(window,width=18,height=2,font="arial 15 bold",fg="purple")
out2.place(x=200,y=520)
tk.Button(window, text='Explain',padx=27,pady=10,bd=8,fg='white',font="arial 8 bold",bg="black", command=decwin).place(x=425,y=520)

l3=tk.Label(window,text="Octal",font="arial 15 bold",bg="green",fg="white",pady=8,padx=57)
l3.place(x=10,y=570)
out3=tk.Text(window,width=18,height=2,font="arial 15 bold",fg="purple",bg="pink")
out3.place(x=200,y=570)
tk.Button(window, text='Explain',padx=27,pady=10,bd=8,fg='white',font="arial 8 bold",bg="black", command=octalwin).place(x=425,y=570)

l4=tk.Label(window,text="Hexa Decimal",font="arial 15 bold",bg="green",fg="white",pady=8,padx=18)
l4.place(x=10,y=620)
out4=tk.Text(window,width=18,height=2,font="arial 15 bold",fg="purple")
out4.place(x=200,y=620)
tk.Button(window, text='Explain',padx=27,pady=10,bd=8,fg='white',font="arial 8 bold",bg="black", command=hexwin).place(x=425,y=620)

#=================================Reset Button=====================================================#
tk.Button(window, text='Reset',padx=10,pady=4,bd=5,fg='white',font="arial 8 bold",bg="Orange", command=lambda:[e1_delete(),deltxt()]).place(x=255,y=680)

#=================================About Us=========================================#
tk.Button(window, text='About Us',padx=10,pady=4,bd=5,fg='white',font="arial 8 bold",bg="Orange", command=aboutus).place(x=170,y=680)

#===============================About Project ===================================#
tk.Button(window, text='About Project',padx=10,pady=4,bd=5,fg='white',font="arial 8 bold",bg="Orange", command=aboutpr).place(x=320,y=680)
#==================================================================================#
window.mainloop()
#====================================END of Program===============================#
