import pdfkit
from weasyprint import HTML


pdfkit.from_url('https://simplecrm.com.sg/', 'demo1.pdf')