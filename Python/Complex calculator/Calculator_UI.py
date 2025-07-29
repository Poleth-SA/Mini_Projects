# calculator with UI
import tkinter as tk
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of a negative number"
    return math.sqrt(x)

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.entry = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons("1", 1,0)
        self.create_buttons("2", 1,1)
        self.create_buttons("3", 1,2)
        self.create_buttons("4", 2,0)
        self.create_buttons("5", 2,1)
        self.create_buttons("6", 2,2)
        self.create_buttons("7", 3,0)
        self.create_buttons("8", 3,1)
        self.create_buttons("9", 3,2)
        self.create_buttons("0", 4,1)
        self.create_buttons(".", 4,2)

        self.create_buttons("+", 1,3)
        self.create_buttons("-", 2,3)
        self.create_buttons("*", 3,3)
        self.create_buttons("/", 4,3)

        self.create_buttons("=", 4,0)
        self.create_buttons("C", 5,0)
        self.create_buttons("CE", 5,1)
        self.create_buttons("(", 5,2)
        self.create_buttons(")", 5,3)

    def create_buttons(self, text, row, column, command=None):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 18),
                      command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def evaluate_expression(self, expression):
        expression = expression.replace(" ", "")
        
        operators = ['+', '-', '*', '/']
        
        for op in operators:
            if op in expression:
                parts = expression.split(op)
                if len(parts) == 2:
                    try:
                        num1 = float(parts[0])
                        num2 = float(parts[1])
                        
                        if op == '+':
                            return add(num1, num2)
                        elif op == '-':
                            return subtract(num1, num2)
                        elif op == '*':
                            return multiply(num1, num2)
                        elif op == '/':
                            result = divide(num1, num2)
                            if isinstance(result, str) and "Error" in result:
                                raise ValueError(result)
                            return result
                    except ValueError:
                        raise ValueError("Invalid expression")
        
        return float(expression)

    def button_click(self, text):
        if text == "=":
            try:
                expression = self.entry.get()
                result = self.evaluate_expression(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                if "Division by zero" in str(e):
                    self.entry.insert(0, "Cannot divide by zero")
                else:
                    self.entry.insert(0, "Error")
        elif text == "C":
            self.entry.delete(0, tk.END)
        elif text == "CE":
            current_text = self.entry.get()
            if current_text:
                self.entry.delete(len(current_text)-1, tk.END)
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text + text)

root = tk.Tk()
app = Calculator(root)
root.mainloop()