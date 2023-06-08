import subprocess
from fpdf import FPDF
import tkinter as tk
from tkinter import ttk

#https://www.pythontutorial.net/tkinter/tkinter-button/
#https://www.sqlitetutorial.net/sqlite-python/
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x480')
        self.resizable(0, 0)
        self.title('Login')

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        username = tk.StringVar()
        password = tk.StringVar()

        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, **paddings)

        username_entry = ttk.Entry(self, textvariable=username, **entry_font)
        username_entry.grid(column=1, row=0, sticky=tk.E, **paddings)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        password_entry = ttk.Entry(
            self, textvariable=password, show="*", **entry_font)
        password_entry.grid(column=1, row=1, sticky=tk.E, **paddings)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

    def print_kitchen_receipt(self):
        filename = 'kitchen.pdf'

    def print_customer_receipt(self):
        filename = 'customer.pdf'

        pdf = FPDF('P', 'mm', (57, 90))
        pdf.add_page()
        pdf.image('logo.jpeg', w=35, h=35, x=6, y=5)
        pdf.set_font('Arial', 'B', 24)
        num = '#42'
        swi = pdf.get_string_width(num)
        pdf.set_y(48)
        pdf.set_x((52 / 2) - (swi / 2))
        pdf.cell(w=43, h=0, txt=num)
        pdf.image('instagram.jpeg', w=5, h=5, x=0, y=55)
        pdf.set_font('Arial', '', 12)
        pdf.set_y(57.5)
        pdf.set_x(6)
        ist = 'neophytbadenfahrt'
        iwi = pdf.get_string_width(ist)
        pdf.cell(w=iwi, h=0, txt=ist)
        pdf.write('\n\n\n')
        pdf.output(filename, 'F')
        subprocess.run(["lp", filename])


if __name__ == '__main__':
    app = App()
    app.mainloop()
