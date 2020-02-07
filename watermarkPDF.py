#Watermark
import PyPDF2
import os
import re

def watermarkPDF(original_PDF_file, watermark_PDF_page, name_of_new_PDF_file):
    template = PyPDF2.PdfFileReader(open(original_PDF_file, "rb"))
    watermark = PyPDF2.PdfFileReader(open(watermark_PDF_page, "rb"))
    output = PyPDF2.PdfFileWriter()
    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)
        with open(name_of_new_PDF_file + ".pdf", 'wb') as file:
            output.write(file)
            
watermarkPDF("superPDF.pdf", "wtr.pdf", "myPDF")

