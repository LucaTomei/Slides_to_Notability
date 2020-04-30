from PyPDF2 import PdfFileReader, PdfFileWriter

# Aggiunge una pagina bianca per ogni pagina del documento

pdf_document = pdffile = '/Users/lucasmac/Downloads/ML_Notes.pdf'
pdf = PdfFileReader(pdf_document)

output_filename = pdf_document.replace('.pdf','') + '_Blank.pdf'

pdf_writer = PdfFileWriter()

for page in range(pdf.getNumPages()):
	if page <= 3:
		current_page = pdf.getPage(page)
		pdf_writer.addPage(current_page)
	else:
		current_page = pdf.getPage(page)
		pdf_writer.addPage(current_page)
		pdf_writer.addBlankPage()
    

with open(output_filename, "wb") as out:
     pdf_writer.write(out)
     print("created", output_filename)