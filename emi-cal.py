import tkinter as tk
from tkinter import *
def calculateEMI():
    #print(loanAmountEntry.get(),loanTenureEntry.get(),loanROIEntry.get())
    totalAmount = float(loanAmountEntry.get()) * (pow((1 + float(loanROIEntry.get()) / 100), float(loanTenureEntry.get())))
    emi = int(totalAmount / (float(loanTenureEntry.get()) * 12))
    Label(window,text = "emi in rupees").grid(row=20, column=0)
    Label(window,text = emi).grid(row=20, column=15)
    

window = tk.Tk()
window.title('EMI calculator')
Label(window, text='Loan Amount (Rs)').grid(row=0)
Label(window, text='Loan Tenure (in years)').grid(row=2)
Label(window, text='Rate of Intrest (%)').grid(row=4)
loanAmountEntry = tk.Entry(window)
loanAmountEntry.grid(row=0,column=12)
loanTenureEntry = tk.Entry(window)
loanTenureEntry.grid(row=2,column=12)
loanROIEntry = tk.Entry(window)
loanROIEntry.grid(row=4,column=12)
Button(window,text="Calculate",command = calculateEMI).grid(row=15,column=3)
window.mainloop()