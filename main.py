import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()

files = os.listdir()
#print(files)

sorted_files = sorted(files)
#print(sorted_files)


for file in sorted_files:
    if file.endswith(".pdf"):
        print(file)
        merger.append(file)
        
merger.write("combined.pdf")
merger.close()