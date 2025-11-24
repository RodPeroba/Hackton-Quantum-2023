import pdfplumber

class PdfReader():

    def __init__(self):
        pass       

    def pdf_to_txt(self, file_path):
        with pdfplumber.open(file_path) as pdf:
            text = ""

            for page in pdf.pages:
                text += page.extract_text()

        return text

    def read_pdf(self, pdf_name):

        file_path = pdf_name
        # Extract text from the PDF file
        text =self.pdf_to_txt(file_path)

        # Save the extracted text to a file
        output_txt = pdf_name[:-4] + ".txt" # retira o .pdf e adiciona .txt
        with open(output_txt, 'w', encoding='utf-8') as file:
            file.write(text)