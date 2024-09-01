from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("https://firebasestorage.googleapis.com/v0/b/bcu-study-space-cded8.appspot.com/o/avatar%2Fviet_an_cv.pdf?alt=media&token=b8313920-7f5a-4c48-a3f0-e60b44f16883")
pages = loader.load_and_split()

print(pages[0])