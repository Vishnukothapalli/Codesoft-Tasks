import tkinter as tk
import math

root = tk.Tk()
root.title('Simple Calculator')
root.configure(bg='#0000FF')
root.resizable(width=False, height=False)

ent_field = tk.Entry(root, bg='#ADD8E6', fg='#000080', font=('Arial', 25), borderwidth=10, justify="right")
ent_field.grid(row=0, columnspan=4, padx=10, pady=10, sticky='nsew')
ent_field.insert(0, '0')

FONT = ('Arial', 12, 'bold')

class SimpleCalculator:
    def __init__(self):
        self.current = ''
        self.inp_value = True

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        firstnum = ent_field.get()
        if self.inp_value:
            self.current = str(num)
            self.inp_value = False
        else:
            self.current = firstnum + str(num)
        self.Entry(self.current)

    def Operation(self, op):
        self.current = ent_field.get() + op
        self.Entry(self.current)

    def Calculate(self):
        try:
            result = str(eval(ent_field.get()))
            self.Entry(result)
        except Exception:
            self.Entry('Error')

    def Clear(self):
        self.Entry('0')
        self.inp_value = True

    def SQ_Root(self):
        try:
            self.current = math.sqrt(float(ent_field.get()))
            self.Entry(self.current)
        except Exception:
            self.Entry('Error')

    def Sin(self):
        try:
            self.current = math.sin(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except Exception:
            self.Entry('Error')

calc = SimpleCalculator()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text.isdigit() or text == '.':
        btn = tk.Button(root, text=text, font=FONT, command=lambda x=text: calc.Enter_Num(x))
    elif text == '=':
        btn = tk.Button(root, text=text, font=FONT, command=calc.Calculate)
    else:
        btn = tk.Button(root, text=text, font=FONT, command=lambda x=text: calc.Operation(x))
    btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

tk.Button(root, text='C', font=FONT, command=calc.Clear).grid(row=5, column=0, sticky='nsew', padx=5, pady=5)
tk.Button(root, text='√', font=FONT, command=calc.SQ_Root).grid(row=5, column=1, sticky='nsew', padx=5, pady=5)
tk.Button(root, text='sin', font=FONT, command=calc.Sin).grid(row=5, column=2, sticky='nsew', padx=5, pady=5)

root.mainloop()
