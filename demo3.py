import requests
from docx import Document
from io import BytesIO

def read_docx_from_url(url):
    # Send a GET request to download the file
    response = requests.get(url)
    
    return response

# Example usage
url = '"https://storage.googleapis.com/bcu-study-spaces.appspot.com/23560092%40gm.uit.edu.vn/41d7005d-444a-4825-a75d-6d54a697d73e_Modern%20hospitality%20resume.docx"'
content = read_docx_from_url(url)
print(content)