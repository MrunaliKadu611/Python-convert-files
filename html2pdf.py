import pdfkit
import os
config = pdfkit.configuration(wkhtmltopdf='C:\\Python36\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
pdfkit.from_file('test.html', 'output.pdf')


