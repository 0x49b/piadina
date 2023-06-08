import subprocess
from fpdf import FPDF

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class PongApp(App):
    def build(self):
        # use a (r, g, b, a) tuple
        btn = Button(text="Push Me !",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(300, 250))
        btn.bind(on_press=self.print_receipt)
        return btn

    def print_receipt(self, event):
        filename = 'order.pdf'

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
    PongApp().run()

