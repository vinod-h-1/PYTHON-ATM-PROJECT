from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class atm:

    def __init__(self,root):
        self.root=root
        blank_space=" "
        self.root.title(110 * blank_space + "ATM system")
        self.root.geometry("774x760+280+0")
        self.root.configure(background='gainsboro')
        MainFrame = Frame(self.root, bd=20, width=784, height=700, relief=RIDGE)
        MainFrame.grid()
        TopFrame1 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame1.grid(row=1, column=0, padx=12)
        TopFrame2 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame2.grid(row=0, column=0, padx=8)

        TopFrame2Left = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Left.grid(row=0, column=0, padx=8)
        TopFrame2Mid = Frame(TopFrame2, bd=5, width=200, height=300, relief=RIDGE)
        TopFrame2Mid.grid(row=0, column=1, padx=8)
        TopFrame2Right = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Right.grid(row=0, column=2, padx=8)


#------------------------------------------------------------------------------------------------------------

        def enter_pin():
            pinNo=self.txtReceipt.get("1.0","end-1c")
            if((pinNo == str("please enter your ATM pin "+d[0]))):
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,'\t\t   ATM' + "\n\n")
                self.txtReceipt.insert(END, 'Withdraw Cash\t\t\t\tLOAN' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Account Details\t\t\t\tDeposit' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Balance\t\t\t\tNew pin' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Mini Statement\t\t\t\tPrintStatement')

                self.img_arrow_Right = PhotoImage(file="rArrow.png")
                self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=loan,
                                         image=self.img_arrow_Right).grid(row=0, column=0, padx=2, pady=2)

                self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=withdrawcash,
                                         image=self.img_arrow_Right).grid(row=1, column=0, padx=2, pady=2)

                self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=newpin,
                                         image=self.img_arrow_Right).grid(row=2, column=0, padx=2, pady=2)

                self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=NORMAL,
                                         command=printministatement, image=self.img_arrow_Right).grid(row=3, column=0,
                                                                                                      padx=2, pady=2)
                self.img_arrow_Left = PhotoImage(file="lArrow.png")

                self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=withdrawcash,
                                         image=self.img_arrow_Left).grid(row=0, column=0, padx=2, pady=2)

                self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=display,
                                         image=self.img_arrow_Left).grid(row=1, column=0, padx=2, pady=2)

                self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=balance,
                                         image=self.img_arrow_Left).grid(row=2, column=0, padx=2, pady=2)

                self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=ministatement,
                                         image=self.img_arrow_Left).grid(row=3, column=0, padx=2, pady=2)
            # -------------------------------------------------------------------------------
            # -------

            else:
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,'Invalid Pin number'+"\n\n")
                '''Cancel = tkinter.messagebox.askyesno("ATM", "please exit and try again")
                if Cancel > 0:
                    self.root.destroy()
                    return'''

        def clear():

            self.txtReceipt = Text(TopFrame2Mid, height=17, width=42, bd=12, font=('arial', 9, 'bold'))
            self.txtReceipt.insert(END, "please enter your ATM pin ")
            self.txtReceipt.grid(row=0, column=0)

            self.img_arrow_Left = PhotoImage(file="lArrow.png")

            self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=withdrawcash,
                                     image=self.img_arrow_Left).grid(row=0, column=0, padx=2, pady=2)

            self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=display,
                                     image=self.img_arrow_Left).grid(row=1, column=0, padx=2, pady=2)

            self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=balance,
                                     image=self.img_arrow_Left).grid(row=2, column=0, padx=2, pady=2)

            self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=ministatement,
                                     image=self.img_arrow_Left).grid(row=3, column=0, padx=2, pady=2)
            # --------------------------------------------------------------------------------------------------------------------
            self.img_arrow_Right = PhotoImage(file="rArrow.png")
            self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=loan,
                                     image=self.img_arrow_Right).grid(row=0, column=0, padx=2, pady=2)

            self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=withdrawcash,
                                     image=self.img_arrow_Right).grid(row=1, column=0, padx=2, pady=2)

            self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=newpin,
                                     image=self.img_arrow_Right).grid(row=2, column=0, padx=2, pady=2)

            self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=printministatement,
                                     image=self.img_arrow_Right).grid(row=3, column=0, padx=2, pady=2)

        # ------
#------------------------------------------------------------------------------------------------------------------

        def insert0():
            value0=0
            self.txtReceipt.insert(END,value0)
        def insert1():
            value1=1
            self.txtReceipt.insert(END,value1)
        def insert2():
            value2=2
            self.txtReceipt.insert(END,value2)
        def insert3():
            value3=3
            self.txtReceipt.insert(END,value3)
        def insert4():
            value4=4
            self.txtReceipt.insert(END,value4)
        def insert5():
            value5=5
            self.txtReceipt.insert(END,value5)
        def insert6():
            value6=6
            self.txtReceipt.insert(END,value6)
        def insert7():
            value7=7
            self.txtReceipt.insert(END,value7)
        def insert8():
            value8=8
            self.txtReceipt.insert(END,value8)
        def insert9():
            value9=9
            self.txtReceipt.insert(END,value9)
        def cancel():
            Cancel=tkinter.messagebox.askyesno("ATM","confitm if you want to cancel")
            if Cancel > 0:
                self.root.destroy()
                return

        def withdrawcash():
            enter_pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.focus_set()

        def loan():
            enter_pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END,'\t\t Welcome to IBANK \n-------------------------------------------------------------------------\n\n\n\n')
            self.txtReceipt.insert(END, 'HOME LOAN \n')
            self.txtReceipt.insert(END, 'VEHICLE LOAN\n')
            self.txtReceipt.insert(END, 'PERSONAL LOAN \n\n\n\n')
            self.txtReceipt.insert(END,"PLEASE VISIT YOUR NEAREST BRANCH \n")
            self.txtReceipt.insert(END,'------------------------------------------------------------------------\n\tThank you for using IBANK \n-------------------------------------------------------------------------\n\n\n\n')
        def next():
            pinNO1=str(self.txtReceipt.get("1.0","end-1c"))
            b=int(pinNO1)
            pinNO4=b+bal[0]
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\t' +str(pinNO4)+' \n')
            self.txtReceipt.insert(END,'\t\t\t\n\n Account Balance'+str(pinNO4)+"\t\t\n\n")
            bal[0] = pinNO4

        def newpin():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\t Welcome to IBANK \n-------------------------------------------------------------------------\n\n\n\n')
            self.txtReceipt.insert(END, 'hello VINOD \n')
            self.txtReceipt.insert(END, 'New pin will sent to your address \n\n\n\n\n\n')
            self.txtReceipt.insert(END, '------------------------------------------------------------------------\n\tThank you for using IBANK \n-------------------------------------------------------------------------\n\n\n\n')
        def display():
            enter_pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, '\t\t Welcome to IBANK \n-------------------------------------------------------------------------\n\n\n\n')
            self.txtReceipt.insert(END, 'ACCOUNT NUMBER : 1903010002433 \n')
            self.txtReceipt.insert(END, 'ACCOUNT NAME   : VINOD H \n')
            self.txtReceipt.insert(END, 'ACCOUNT TYPE   : SAVINGS ACCOUNT \n\n\n\n')
            self.txtReceipt.insert(END, '------------------------------------------------------------------------\n\tThank you for using IBANK \n-------------------------------------------------------------------------\n\n\n\n')

        def balance():
            enter_pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END,'\t\t Welcome to IBANK \n-------------------------------------------------------------------------\n\n\n\n')
            self.txtReceipt.insert(END, '\t\t\t\n\n Account Balance : ' + str(bal[0]) + "\t\t\n\n\n\n\n")
            self.txtReceipt.insert(END,'------------------------------------------------------------------------\n\tThank you for using IBANK \n-------------------------------------------------------------------------\n\n\n\n')


        def ministatement():
            pinNO1=str(self.txtReceipt.get("1.0","end-1c"))
            b=int(pinNO1)
            if b > bal[0]:

                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.insert(END,'\t\t Welcome to IBANK \n-------------------------------------------------------------------------\n\n\n\n')

                self.txtReceipt.insert(END,"\tSORRY INSUFFICIENT BALANCE \n\n\t your current balance "+str(bal[0])+"\n\n\n \n")
                self.txtReceipt.insert(END, '------------------------------------------------------------------------\n\tThank you for using IBANK \n-------------------------------------------------------------------------\n\n\n\n')

            else:
                pinNO4=bal[0]-b
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,'\t\t\t\n\n Account Balance'+str(pinNO4)+"\t\t\n\n")
                self.txtReceipt.insert(END, 'Withdrawed\t\t\t\tRs' + str(pinNO1) + ' \n\n\n')
                self.txtReceipt.insert(END, 'Rent\t\t\t\t Rs 1200' + "\n\n\n")
                self.txtReceipt.insert(END, 'Tesco\t\t\t\t Rs 79' + "\n\n\n")
                self.txtReceipt.insert(END, 'food\t\t\t\t Rs 700' + "\n\n\n")
                self.txtReceipt.insert(END, 'Loan\t\t\t\t Rs 900')
                self.txtReceipt.insert(END, '\t\t Thank you for using IBANK \n')
                bal[0] = pinNO4
        def printministatement():
            pinNO1=str(self.txtReceipt.get("1.0","end-1c"))
            if pinNO1>str(12001):
                self.txtReceipt.insert(END,'sorry insufficients funt')

            pinNO2=str(pinNO1)
            pinNO3=float(pinNO2)
            pinNO4=float(1296-(pinNO3))
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\t' +str(pinNO4)+' \n')
            self.txtReceipt.insert(END,'$1296'+"\n")
            self.txtReceipt.insert(END, 'Withdraw Cash\t\t\t\tLOAN' + "\n\n\n\n")
            self.txtReceipt.insert(END, 'Cash with reciept\t\t\t\tDeposit' + "\n\n\n\n")
            self.txtReceipt.insert(END, 'Balance\t\t\t\tNew pin' + "\n\n\n\n")
            self.txtReceipt.insert(END, 'Mini Statement\t\t\t\tPrintStatement')
            self.txtReceipt.insert(END, '\t\t Thank you for using IBANK \n')

#-------------------------------------------------------------------------------------------------------------------------------------
        self.txtReceipt=Text(TopFrame2Mid,height=17,width=42,bd=12,font=('arial',9,'bold'))
        self.txtReceipt.insert(END,"please enter your ATM pin ")
        self.txtReceipt.grid(row=0,column=0)

        self.img_arrow_Left=PhotoImage(file ="lArrow.png")

        self.btnArrowL1=Button(TopFrame2Left,width=160,height=60, state=DISABLED,command=withdrawcash,image=self.img_arrow_Left).grid(row=0,column=0,padx=2,pady=2)

        self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60,state=DISABLED,command=display, image=self.img_arrow_Left).grid(row=1, column=0, padx=2, pady=2)

        self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60,state=DISABLED, command=balance,image=self.img_arrow_Left).grid(row=2, column=0, padx=2, pady=2)

        self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60,state=DISABLED,  command=ministatement,image=self.img_arrow_Left).grid(row=3, column=0, padx=2, pady=2)
#--------------------------------------------------------------------------------------------------------------------
        self.img_arrow_Right = PhotoImage(file="rArrow.png")
        self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60,state=DISABLED, command=loan,image=self.img_arrow_Right).grid(row=0, column=0, padx=2, pady=2)

        self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60,state=DISABLED,command=withdrawcash,  image=self.img_arrow_Right).grid(row=1, column=0, padx=2, pady=2)

        self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60,state=DISABLED,command=newpin, image=self.img_arrow_Right).grid(row=2, column=0, padx=2, pady=2)

        self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60,state=DISABLED, command=printministatement,image=self.img_arrow_Right).grid(row=3, column=0, padx=2, pady=2)
#------------------------------------------------------pin numbers-----------------------------------------------------------
        self.img1 = PhotoImage(file="one.png")
        self.btn1 = Button(TopFrame1, width=160, height=60,command=insert1,image=self.img1).grid(row=2, column=0, padx=4, pady=4)
        self.img2 = PhotoImage(file="two.png")
        self.btn2 = Button(TopFrame1, width=160, height=60, command=insert2,image=self.img2).grid(row=2, column=1, padx=4, pady=4)
        self.img3 = PhotoImage(file="three.png")
        self.btn3 = Button(TopFrame1, width=160, height=60, command=insert3,image=self.img3).grid(row=2, column=2, padx=4, pady=4)
        self.imgce=PhotoImage(file="cancel.png")
        self.btncancel = Button(TopFrame1, width=160, height=60,command=cancel ,image=self.imgce).grid(row=2, column=3, padx=4, pady=4)

        self.img4 = PhotoImage(file="four.png")
        self.btn4 = Button(TopFrame1, width=160, height=60, command=insert4,image=self.img4).grid(row=3, column=0, padx=4, pady=4)
        self.img5 = PhotoImage(file="five.png")
        self.btn5 = Button(TopFrame1, width=160, height=60,command=insert5, image=self.img5).grid(row=3, column=1, padx=4, pady=4)
        self.img6 = PhotoImage(file="six.png")
        self.btn6 = Button(TopFrame1, width=160, height=60, command=insert6,image=self.img6).grid(row=3, column=2, padx=4, pady=4)
        self.imgcl=PhotoImage(file="clear.png")
        self.btnclear = Button(TopFrame1, width=160, height=60, command=clear,image=self.imgcl).grid(row=3, column=3, padx=4, pady=4)

        self.img7 = PhotoImage(file="seven.png")
        self.btn7 = Button(TopFrame1, width=160, height=60,command=insert7, image=self.img7).grid(row=4, column=0, padx=4, pady=4)
        self.img8 = PhotoImage(file="eight.png")
        self.btn8 = Button(TopFrame1, width=160, height=60, command=insert8,image=self.img8).grid(row=4, column=1, padx=6, pady=4)
        self.img9 = PhotoImage(file="nine.png")
        self.btn9 = Button(TopFrame1, width=160, height=60, command=insert9,image=self.img9).grid(row=4, column=2, padx=6, pady=4)
        self.imgenter = PhotoImage(file="enter.png")
        self.btnenter = Button(TopFrame1, width=160, height=60,command=enter_pin, image=self.imgenter).grid(row=4, column=3, padx=6, pady=4)

        self.img10 = PhotoImage(file="empty.png")
        self.btnspl = Button(TopFrame1, width=160, height=60,command=next ,image=self.img10).grid(row=5, column=0, padx=4, pady=4)
        self.img12 = PhotoImage(file="zero.png")
        self.btnempty = Button(TopFrame1, width=160, height=60, command=insert0,image=self.img12).grid(row=5, column=1, padx=4, pady=4)
        self.img13 = PhotoImage(file="empty.png")
        self.btnzero = Button(TopFrame1, width=160, height=60, image=self.img13).grid(row=5, column=2, padx=4, pady=4)

        self.img11 = PhotoImage(file="empty.png")
        self.btnzero = Button(TopFrame1, width=160, height=60, image=self.img11).grid(row=5, column=3, padx=4, pady=4)
#class atm1(atm):


if __name__=='__main__':
    root=Tk()
    application=atm(root)
    d=['2213']
    bal=[12200]
    root.mainloop()