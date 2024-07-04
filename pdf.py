import PyPDF2
import sys  # Can get the arguments / for combine

inputs = sys.argv[1:]  # grab all pdf from the first

with open('dummy.pdf', 'r+b') as file:
    def pdf_combiner(pdf_list):
        merger = PyPDF2.PdfMerger()
        for pdf in pdf_list:
            print(pdf)
            merger.append(pdf)
        merger.write('merged_file.pdf')

    pdf_combiner(inputs)
