from PyPDF2 import PdfMerger

pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf', 'file5.pdf', 'file6.pdf', 'file7.pdf', 'file8.pdf',
        'file9.pdf']  # Rename pdf files in same folder as main.py. add/remove here as needed.

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")   # merged pdf file is names this. just rename this whatever you want.
merger.close()
