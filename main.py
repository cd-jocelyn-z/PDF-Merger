from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()
#sorting files in the directory so that the chapters follow the same order in the newly generated pdf
files = os.listdir()
sorted_files = sorted(files)

for file in sorted_files:
    if file.endswith(".pdf"):
        merger.append(file)
        print(file)
        
merger.write("combined.pdf")
merger.close()