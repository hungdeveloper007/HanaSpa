from tkinter import *
import parser

# Creat window
root = Tk()
root.title("Calculator in Python")
root.geometry("312x325")
root.resizable(0, 0)

# Add button to the calculator
input_frame = Frame(root, width=312, height=50, highlightbackground="black", highlightthickness=1)
input_frame.pack(side=TOP)
# Creat an input field inside the frame
input_field = Entry(input_frame, font=('arial', 18, 'bold'), width=50, bg="#eee", justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
# Creat a frame containing the buttons
btns_frame = Frame(root, width=312, height=274, bg="grey")
btns_frame.pack()
# Row 0
clear = Button(btns_frame, text="Clear", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: clear_all()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: get_operation("/")).grid(row=0, column=3, padx=1, pady=1)
# Row 1
seven = Button(btns_frame, text="7", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: get_variables(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: get_variables(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: get_variables(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: get_operation("*")).grid(row=1, column=3, padx=1, pady=1)
# Row 2
four = Button(btns_frame, text="4", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: get_variables(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: get_variables(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: get_variables(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: get_operation("-")).grid(row=2, column=3, padx=1, pady=1)
# Row 3
one = Button(btns_frame, text="1", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: get_variables(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: get_variables(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: get_variables(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: get_operation("+")).grid(row=3, column=3, padx=1, pady=1)
# Row 4
zero = Button(btns_frame, text="0", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: get_variables(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text=".", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: get_variables(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: calculate()).grid(row=4, column=3, padx=1, pady=1)
# i keeps the track of current position on the input text field
i = 0


# Receives the digit as parameter and display it on the input field
def get_variables(num):
    global i
    input_field.insert(i, num)
    i += 1


# Mapping the operator buttons
def get_operation(operator):
    global i
    length = len(operator)
    input_field.insert(i, operator)
    i += length


# Mapping the clear button
def clear_all():
    input_field.delete(0, END)


# Mapping the '=' button
def calculate():
    entire_string = input_field.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        input_field.insert(0, result)
    except Exception:
        clear_all()
        input_field.insert(0, "0")


root.mainloop()
