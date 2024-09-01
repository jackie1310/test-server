from pyresparser import ResumeParser
# import nltk
# nltk.download('words')

try: 
    # doc = Document()
    # with open('viet_an_cv.pdf', 'r') as file:
    #     doc.add_paragraph(file.read())
    # doc.save("viet_an_cv.docx")
    data = ResumeParser('viet_an_cv.pdf').get_extracted_data()
    print(data['skills'])
except Exception as e: 
    print(e)