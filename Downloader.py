from PdfDownloader import Importer
from PdfReader import PdfReader

class Downloader():

	def __init__(self):
		self.pdf_reader = PdfReader()
		self.pdf_downloader = Importer()

	def create_name(self, url):
		#Cria o nome do txt baseado na url do arquivo
		nome = url.split("/")
		nome = nome[-1]
		nome = nome.split(".")
		nome = nome[0]
		return nome

	def run(self, pdfs_to_read):

		#nome do txt contendo todos os pdfs que queiram ser lidos
		#pdfs_to_read = "pdfs_to_read.txt"

		with open(pdfs_to_read, "r") as arquivo:
			for url in arquivo:
				url = url[:-1]

				fileName = self.create_name(url) + ".pdf"

				self.pdf_downloader.get_pdf(url = url, pdf_name = fileName)
				self.pdf_reader.read_pdf(pdf_name = fileName)

if __name__ == "__main__":
	downloader = Downloader()
	downloader.run(pdfs_to_read="pdfs_to_read.txt")