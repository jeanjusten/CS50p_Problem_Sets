from fpdf import FPDF
from fpdf import Template, Align

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 32)
        self.cell(80)
        self.cell(30, 20,"CS50 Shirtificate", border=0, align="C")
        self.ln(38)

# Specifications
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(0)
name = f"{input("Name: ")} took CS50"

pdf.image("shirtificate.png", Align.C)

pdf.set_text_color(255, 255, 255)
pdf.set_font("Helvetica", "B", 28)
pdf.cell(30,-295,name,border=0,center="C",align="C")

pdf.output("shirtificate.pdf")