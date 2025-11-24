import requests

class Importer(): 

    def __init__(self):
        pass
    
    def get_pdf(self, url, pdf_name):

        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            output_path = pdf_name
            
            with open(output_path, "wb") as f:
                f.write(response.content)
            print("PDF file downloaded and saved as", output_path)
        else:
            print("Failed to download PDF file. Status code:", response.status_code)