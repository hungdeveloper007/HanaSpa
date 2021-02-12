import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk


#
class RealTimeCurrencyConverter():
    def __init__(self, url):
        #
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    #
    def convert(self, from_currency, to_currency, amount):
        #
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        #
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class App(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title("Currency Conversion")
        self.currency_converter = converter
        self.geometry("500x200")
        self.resizable(0, 0)
        # Label
        self.intro_label = Label(self, text='Welcome to Real Time Currency Convertor', fg='blue', relief=tk.RAISED,
                                 borderwidth=3)
        self.intro_label.config(font=('Courier', 15, 'bold'))
        self.intro_label.place(x=15, y=0)
        # Dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("AED")
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   font=("Courier", 12, "bold"),
                                                   values=list(self.currency_converter.currencies.keys()),
                                                   justify=tk.CENTER, width=12)
        self.from_currency_dropdown.place(x=30, y=50)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 font=("Courier", 12, "bold"),
                                                 values=list(self.currency_converter.currencies.keys()),
                                                 justify=tk.CENTER, width=12)
        self.to_currency_dropdown.place(x=334, y=50)
        # Entry
        self.amount_field = Entry(self, justify=tk.CENTER, relief=tk.RIDGE, bd=3)
        self.amount_field.place(x=36, y=80)
        self.converted_amount_field_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE,
                                                  justify=tk.CENTER, width=17, bd=3)
        self.converted_amount_field_label.place(x=340, y=80)
        # Button
        self.convert_button = Button(self, text="Convert", fg="black", font=("Courier", 10, "bold"),
                                     command=self.perform)
        self.convert_button.place(x=220, y=65)

        self.date_label = Label(self,
                                text=f"1 {self.from_currency_variable.get()} = {self.currency_converter.convert(self.from_currency_variable.get(), self.to_currency_variable.get(), 1)} {self.to_currency_variable.get()} \n Date : {self.currency_converter.data['date']}",
                                relief=tk.GROOVE, borderwidth=5, width=25)
        self.date_label.place(x=160, y=130)

    def perform(self):
        if self.amount_field.get() > "9":
            self.date_label = Label(self,
                                    text="Please enter again",
                                    relief=tk.GROOVE, borderwidth=5, width=25)
            self.date_label.place(x=160, y=130)
        else:
            self.date_label = Label(self,
                                    text=f"1 {self.from_currency_variable.get()} = {self.currency_converter.convert(self.from_currency_variable.get(), self.to_currency_variable.get(), 1)} {self.to_currency_variable.get()} \n Date : {self.currency_converter.data['date']}",
                                    relief=tk.GROOVE, borderwidth=5, width=25)
            self.date_label.place(x=160, y=130)
            amount = float(self.amount_field.get())
            from_curr = self.from_currency_variable.get()
            to_curr = self.to_currency_variable.get()
            converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
            converted_amount = round(converted_amount, 3)
            self.converted_amount_field_label.config(text=str(converted_amount))
            self.update()

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    a = App(converter)
    mainloop()
